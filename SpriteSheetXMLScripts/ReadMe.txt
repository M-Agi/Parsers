Python script:

SpriteSheet scaler

Be kell olvasni egy XML sprite-sheet-et és adatokat kell manipulálni benne (számokat szorzni/változtatni) majd kiírni az eredményt.

High-level requirementek:
1.: kell mindenképp megadható path az XML file-hoz amin dolgozik a script (az eredmény mehet drótozott file-ba, v. %input%.result nevűbe vagy valami hasonló megoldás).
2.: nem összerakni kéne egy új XML stringet és kiírni, hanem a beolvasott XML fán kéne dolgozni és azt a módosítások után kiírni (csak egyes részeit kell bizgetni és a többinek érintetlenül kell maradni)!

A feladat lényegében annyi lesz, hogy át kell nyálazni egy specifikus fajta XML file-t és abban bizonyos feltételeknek megfelelő node-okban a számokat (pl ha valahol a szöveg egy valid integer, pl.: 24) meg kell szorozni egy drótozott értékkel (esetünkben ez 4, de nem árt ha van azért rá egy konstans "SCALE", h. könnyű legyen átírni az értéket).

Milyen XML file-okat kéne beolvasni:

* Minden sprite-sheet XML file root-ja a következő formájú:
<SpriteSheet texture="valami\valami.png">
	<!-- ... -->
</SpriteSheet>

* A következő fajta közvetlen gyerkőcei lehetnek amiket mind át kell majd kutatni:
<DefaultSpriteProperties>
<SpriteTable>
<AnimationTable>
<NinePatchTable>

* Itt egy "DefaultSpriteProperties" példa amiben bármilyen gyerek node értéke egy valid integer akkor be kell szorozni a skálázással (ebben az esetben a "SourceHorizontal" 32-es értékét 128-ra kell átvarázsolni):
	<DefaultSpriteProperties>
		<SourceHorizontal>32</SourceHorizontal>
		<SourceVertical>32</SourceVertical>
		<OriginX>16</OriginX>
		<OriginY>16</OriginY>
	</DefaultSpriteProperties>

* A másik fajta gyerkőcök hasonlóak (SpriteTable, AnimationTable, NinePatchTable). Mindegyikben egy jó adag "Entry" node található:
		<Entry name="valami">
			<!-- ... -->
		</Entry>

* Az "Entry" node-kat is mind át kell vizsgálni de nem minden esetben. Csak akkor érdekesek ezek a node-ok, ha van egy "Overwrite" gyerekük, ekkor viszont az "Overwrite" gyerek minden node-ját (rekurzívan) meg kell nézni, h. van-é benne valami szöveg és az egy valid integer-é. Ezesetben pedig szorozni kell.
		<Entry name="CrouchSprite">
			<Overwrite>
				<!-- ... -->
			</Overwrite>
		</Entry>

Ez lenne a feladat.
Találsz egy példa input file-t amihez csináltam egy elvárt eredményt.