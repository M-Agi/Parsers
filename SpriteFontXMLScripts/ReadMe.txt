Python script:

SpriteFont scaler (nagyon hasonló a SpriteSheet scaler-re)

Be kell olvasni egy XML sprite-font-ot és adatokat kell manipulálni benne (számokat szorzni/változtatni) majd kiírni az eredményt.

High-level requirementek:
1.: kell mindenképp megadható path az XML file-hoz amin dolgozik a script (az eredmény mehet drótozott file-ba, v. %input%.result nevűbe vagy valami hasonló megoldás).
2.: nem összerakni kéne egy új XML stringet és kiírni, hanem a beolvasott XML fán kéne dolgozni és azt a módosítások után kiírni (csak egyes részeit kell bizgetni és a többinek érintetlenül kell maradni)!

A feladat lényegében annyi lesz, hogy át kell nyálazni egy specifikus fajta XML file-t és abban bizonyos feltételeknek megfelelő node-okban a számokat (pl ha valahol a szöveg egy valid integer, pl.: 24) meg kell szorozni egy drótozott értékkel (esetünkben ez 4, de nem árt ha van azért rá egy konstans "SCALE", h. könnyű legyen átírni az értéket).

Milyen XML file-okat kéne beolvasni:

* Minden sprite-font XML file root-ja a következő formájú:
<Font texture="Valami.png" height="123">
	<!-- ... -->
</Font>
Itt a "height" attribútum értékét kell felszorozni.

* Sok eltérő típusú közvetlen gyerkőcei lehetnek amiket mind meg kell majd vizsgálni:
<SpaceWidth>
<TabWidth>
<MinimumLineHeight>
<PlaceholderGlyph>
A szabály ezekre mindig a következő:
Amennyiben nincs gyerek node-juk csak valami text értékük pl.:
	<SpaceWidth>5</SpaceWidth>
	<!-- ... -->
	<PlaceholderGlyph>167 16 5 15</PlaceholderGlyph>
Akkor ezeket meg kell próbálni felszorozni. A "SpaceWidth" node adja magát, a "PlaceholderGlyph" azonben egy picit bonyolultabb. Az utóbbi node-nál meg kell próbálni splittelni a text-et whitespace-ek mentén és ha minden elem valid integer mindegyiket be kell szorozni majd ugyan ilyen formában eltárolni (joint(" ")).

* Van egy jóval bonyolultabb gyerkőc node amiben kutakodni is kell. Lesz a "Font" root node-on belül egy "GlyphTable" node aminek ugyancsak összetett gyerkőcei lesznek és ezeken kell komolyabb transzformációt véghez vinni:
	<GlyphTable>
		<Glyph number="32" advance="5">87 32 3 15</Glyph>
		<Glyph number="33" advance="3">126 32 2 15</Glyph>
		<Glyph number="34" advance="6">131 16 5 15</Glyph>
		<!-- ... -->
	</GlyphTable>
Itt minden "Glyph" gyerek node-ot meg kell vizsgálni. Az "advance" attribútum értékét kell felszorozni, illetve hasonlóan kell eljárni a node text-jével mint a "PlaceholderGlyph" node esetben. A szöveget whitespace-ek mentén splittelni kell és az integer értéket be kell szorozni majd ugyan ilyen formában eltárolni (joint(" ")).

Ez lenne a feladat.
Találsz egy példa input file-t amihez csináltam egy elvárt eredményt.
Az xml_scaler scriptedet is nézd át elötte ugyanis ahhoz elég hasonló scriptet kéne készíteni, talán egyes részek (függvények) meg is fognak egyezni.