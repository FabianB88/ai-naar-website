# E-learning startsjabloon

Kale opzet voor een e-learning in het Green Office-design. Draait als website
(GitHub Pages of eigen server) én als SCORM-pakket in een LMS — dezelfde build.

Gebouwd op [Adapt Framework](https://github.com/adaptlearning/adapt_framework)
v5.56.2 (GPL-3.0).

## Beginnen

```bash
npm install
npx adapt install
python tools/build_course.py
npx grunt build
```

De cursus staat daarna in `build/`. Open `build/index.html` via een webserver,
niet rechtstreeks vanaf schijf — Adapt laadt zijn inhoud via HTTP.

## Een cursus schrijven

De inhoud staat **niet** in de JSON-bestanden onder `src/course/nl/`. Die worden
gegenereerd en overschreven. Je schrijft in `tools/content/`.

| Bestand | Waarvoor |
|---|---|
| `tools/content/cursus.py` | Titel van de cursus en de lijst met pagina's, in volgorde |
| `tools/content/pNN_naam.py` | Eén pagina |
| `tools/bouwstenen.py` | De blokken die je in een pagina kunt gebruiken |
| `tools/build_course.py` | Zet alles in elkaar. Hier hoef je niets aan te wijzigen |

Een pagina toevoegen: maak een bestand in `tools/content/`, en zet hem in de
lijst `PAGINAS` in `cursus.py`. Verplaatsen doe je door de regel te verschuiven —
de id's en de doorgaan-knoppen lopen automatisch mee.

Een pagina ziet er zo uit:

```python
def bouw(p):
    p.tekst('Kop', '<p>Tekst in HTML.</p>')
    p.aandacht('Let op', '<p>Blok met accentrand.</p>')
    p.beeld('schema.svg', alt='Beschrijf wat er te zien is.')
    p.accordeon('Kop', '<p>Intro.</p>', [{'title': '...', 'body': '<p>...</p>'}])
    p.vraag('Kop', 'Vraagtekst', [('goed', True), ('fout', False)], feedback={...})
    p.invulvelden('Kop', '<p>Uitleg.</p>', [('veld-id', 'Label', 'Hint')])
    p.knoppenrij('Meenemen', '<p>Uitleg.</p>')
```

Draai daarna `python tools/build_course.py && npx grunt build`.

### Een toets

Zet `TOETS = 'een-id'` bovenin een paginabestand. Alle vragen op die pagina
vormen dan samen één toets. Voeg een functie `uitslag(p)` toe met
`p.uitslag(TOETS)` erin; die komt in een eigen artikel onder de vragen.

## Publiceren

**Als website:**

```bash
rm -rf docs && cp -r build docs && touch docs/.nojekyll
git add -A && git commit -m "update" && git push
```

Zet GitHub Pages op branch `main`, map `/docs`.

**In een LMS:** zip de *inhoud* van `build/` — niet de map zelf. `imsmanifest.xml`
moet in de root van het zipbestand staan, anders weigert het LMS de import.

De voortgang wordt ook zonder LMS bewaard: `window.ISCOOKIELMS` staat op `true`
in `src/extensions/adapt-contrib-spoor/required/index.html`, waardoor spoor een
nep-LMS start die de voortgang in een cookie zet.

## Toegankelijkheid

Als bekostigde onderwijsinstelling val je onder het Tijdelijk besluit digitale
toegankelijkheid: **WCAG 2.1 AA is verplicht**, en digitale leermiddelen vallen
daaronder. Adapt levert het meeste (labels, focusbeheer, live regions,
toetsenbordnavigatie) uit zichzelf. Wat jij zelf moet doen:

- **Altijd een `alt` bij een afbeelding.** `bouwstenen.py` weigert een beeld
  zonder alt-tekst. Beschrijf wat er te zien is, niet dát het een schema is.
- **Kleur nooit als enige onderscheid.** In diagrammen ook een stippellijn,
  een label of een vorm gebruiken.
- **Contrast.** Het palet is nagerekend: `#5C7A5A` op wit haalt 4,79:1 en
  `#7A6E66` haalt 4,61:1 — beide net boven de AA-grens. `#B0A49A` haalt het
  níet; alleen voor lijnen en pijlen gebruiken, nooit voor tekst.

## Wat er is aangepast aan Adapt, en waarom

Dit zijn bewuste afwijkingen. Draai je later `adapt update`, controleer ze dan.

- **Invulvelden zijn gewone `textarea`'s**, geen vraagcomponent
  (`src/theme/.../js/canvasOpslag.js`). De `textInput`-component bewaart alleen
  een antwoord-index en geeft vrije tekst na herladen terug als `******`
  (zie `textInputModel.js:66`), en zou het antwoord bovendien fout rekenen.
- **De doorgaan-knop is een gewone link**, geen trickle-knop. Die laatste gaat
  pas aan als Adapt de pagina als gezien markeert, wat afhangt van
  zichtbaarheidsdetectie en lastig te testen is.
- **Onderschriften staan ónder de afbeelding.** Vanilla zet ze standaard als
  halftransparante zwarte balk eroverheen, precies over de legenda van een schema.
- **Blokken hebben geen `displayTitle`.** Anders staat elke kop dubbel: één keer
  op het blok en één keer op de component eronder.
- **Kleuren** zitten in `src/theme/adapt-contrib-vanilla/less/_defaults/_colors.less`
  (`@blue` is het accent) en `less/project/cursus.less`.
- **`.github/` is genegeerd.** Adapt en zijn plugins brengen eigen CI-workflows
  mee die een push blokkeren zonder `workflow`-scope.

## Bij een grotere e-learning werkt dit anders

Deze opzet is getest op een cursus van negen pagina's. Groeit het verder, dan
loop je tegen het volgende aan:

**Vanaf ongeveer vijftien pagina's — groepeer in modules.** Een platte lijst van
twintig items in het hoofdmenu is niet meer te overzien. Adapt kan submenu's:
een `contentObject` van het type `menu` met pagina's eronder. Dat vraagt een
aanpassing in `build_course.py`, want die gaat nu uit van één niveau.

**Vanaf ongeveer dertig pagina's — knip het op in losse cursussen.** Eén grote
cursus wordt traag om te bouwen (nu al twee minuten voor negen pagina's), traag
om te laden, en de deelnemer verliest het overzicht. Meerdere kleinere cursussen
die naar elkaar linken werken beter, en je kunt ze los bijwerken zonder de rest
opnieuw uit te rollen.

**Bij een echte toets — gebruik vragenbanken.** Adapt kan vragen trekken uit een
bank en de volgorde per poging wisselen (`_banks`, `_randomisation` in het
assessment-blok). Voor een kennischeck van vijf vragen is dat overdreven; voor
een toets die telt is het nodig.

**Bij meerdere auteurs — overweeg de authoring-tool.** Deze opzet gaat ervan uit
dat één iemand de inhoud schrijft in Python-bestanden. Moeten meerdere mensen
tegelijk redigeren zonder Git te gebruiken, dan is
[adapt_authoring](https://github.com/adaptlearning/adapt_authoring) een betere
basis — dat is een server met een webinterface.

**Bij video — niet meeleveren in de repo.** Een SCORM-pakket met video erin wordt
al snel honderden megabytes en veel LMS'en weigeren dat. Host video extern en
verwijs ernaar.
