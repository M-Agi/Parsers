Python script able to convert from a directory of *.resx files with a special structure (*1) to one *.csv file (*2) (and back *3) to help localization efforts.

***

*1.:
A directory contains all the locales/localizations and each locale can be found in a sub-directory with an ISO locale code as the directory name, e.g.: en (directory for the english locale), hu-HU (directory for the Hungarian + Hungary locale), fr-CA (directory for French + Canada locale).
All locale sub-directories must contain the same files. Files with matching names (e.g.: en/Speech.resx, hu-HU/Speech.resx) are the localized versions for a set of strings.
Full example.:
RootDir/
RootDir/en-US/
RootDir/en-US/Speech.resx
RootDir/en-US/Text.resx
RootDir/hu-HU/
RootDir/hu-HU/Speech.resx
RootDir/hu-HU/Text.resx

*2.:
The matching files all contain the same localized string keys.
Example:
RootDir/en-US/Text.resx XML:
...
<data name="StringKey1">
	<value>Localized Text en-US</value>
</data>
...
RootDir/hu-HU/Text.resx XML:
...
<data name="StringKey1">
	<value>Localized Text hu-HU</value>
</data>
...
From all the matching files the entries have to be parsed (preferable with keeping the key ordering!) and a *.csv has to be written out which contains all the locales in a separate column and all the keys with localized entries in rows.
Example:
Text.csv:
name,en-US,hu-HU,
StringKey1,Localized Text en-US,Localized Text hu-HU

*3.:
A reverse operation must be supported. The script (or another script) must be able to parse a *.csv file with the mentioned format (*2) and should produce the appropriate directory structure containing *.resx files.



!!! Extras:
The first 3 points are perfectly enough as a start, but a few extras are needed later on:
The resx format needs an extra attribute in the "data" XML node to be parsed with keeping special white-space characters (e.g.: new lines, tabs etc...). If an localized string entry in the *.csv file contains a new-line character the attribute should be added to the output!
Example:

<data name="StringKey2" xml:space="preserve">
	<value>Text with a
new line character</value>
</data>

Some data nodes may contain "comment" child nodes. It would be helpful to collect these and add their value to the *.csv file in the second column. It is ok to add only the first occurrence (or the last does not matter) in any of the locale files for a key. The reverse operation should add it the *.resx files too.
Example:

RootDir/en-US/Text.resx XML:
...
<data name="StringKey3">
	<value>Localized Text en-US</value>
	<comment>This is a comment</comment>
</data>
...

Text.csv:
name,comment,en-US
...
StringKey3,This is a comment,Localized Text en-US
...