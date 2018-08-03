
import os
import sys
import csv
import xml.etree.ElementTree as ET
import collections

import utility


def ensure_list_len(list, index):
    while len(list) <= index:
        list.append("")


def prepare_localization_list(table, name, lang_index):
    localization = None
    if not name in table:
        localization = []
        ensure_list_len(localization, lang_index)
        table[name] = localization
    else:
        localization = table[name]
    return localization


def parse_file(lang_index, filename, table):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # prepare localization lists!
    # if lang_index == 2 (3rd language), than expand lists:
    # K1 => ["", "", ""]
    # ...
    # Kn => ["", "", ""]
    for localization in table.itervalues():
        ensure_list_len(localization, lang_index)
    
    for data in root.findall(utility.XML_DATA):
        name = data.get(utility.XML_NAME)
        print name
        value = data.find(utility.XML_VALUE)
        localization = prepare_localization_list(table, name, lang_index)
        localization[lang_index] = str(value.text.encode(encoding="utf-8", errors="ignore"))


def collect_lang_codes(directory):
    lang_codes = []
    for entry in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, entry)):
            lang_codes.append(entry)
    return lang_codes


def output_table(table, lang_codes, filename):
    lang_codes.insert(0, utility.NAME)
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(lang_codes)
        for key, localization in table.iteritems():
            localization.insert(0, key)
            writer.writerow(localization)


if len(sys.argv) != 3:
    print "Not enough argument added"
else:
    directory = sys.argv[1]
    tablename = sys.argv[2]
    if not os.path.isdir(directory):
        print "Not a directory:", directory
    else:
        lang_codes = collect_lang_codes(directory)
        localization_table = collections.OrderedDict()
        for lang_index in xrange(len(lang_codes)):
            lang_code = lang_codes[lang_index]
            filename = utility.prep_resx_name(directory, lang_code, tablename)
            parse_file(lang_index, filename, localization_table)
        
        output_table(localization_table, lang_codes, tablename + utility.CSV)


