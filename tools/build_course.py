# -*- coding: utf-8 -*-
"""Zet de cursus in elkaar uit de losse pagina's in tools/content/.

Draaien:  python tools/build_course.py
Daarna:   npx grunt build

Elke pagina is een eigen bestand in tools/content/. De volgorde en de titels
staan in tools/content/cursus.py. Voeg je een pagina toe, dan zet je hem daar
in de lijst — verder hoef je niets te wijzigen.
"""
import importlib
import io
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.dirname(HIER)
UIT = os.path.join(WORTEL, 'src', 'course', 'nl')
sys.path.insert(0, HIER)

from bouwstenen import Pagina  # noqa: E402
from content import cursus     # noqa: E402


def schrijf(naam, data):
    pad = os.path.join(UIT, naam)
    io.open(pad, 'w', encoding='utf-8').write(
        json.dumps(data, indent=2, ensure_ascii=False))


# ------------------------------------------------------------------- course
course = {
    '_id': 'course', '_type': 'course', '_courseId': cursus.ID,
    'title': cursus.TITEL, 'displayTitle': cursus.TITEL,
    'subtitle': cursus.ONDERTITEL, 'description': cursus.OMSCHRIJVING,
    'body': cursus.INLEIDING, 'instruction': '',
    '_buttons': {
        '_submit': {'buttonText': 'Nakijken', 'ariaLabel': 'Kijk mijn antwoord na'},
        '_reset': {'buttonText': 'Opnieuw', 'ariaLabel': 'Probeer deze vraag opnieuw'},
        '_showCorrectAnswer': {'buttonText': 'Toon antwoord', 'ariaLabel': 'Toon het juiste antwoord'},
        '_hideCorrectAnswer': {'buttonText': 'Mijn antwoord', 'ariaLabel': 'Toon mijn eigen antwoord'},
        '_showFeedback': {'buttonText': 'Toelichting', 'ariaLabel': 'Toon de toelichting'}
    },
    '_globals': {
        '_menu': {'_boxMenu': {'durationLabel': 'Tijd:'}},
        '_accessibility': {'_ariaLabels': {
            'skipNavigation': 'Ga direct naar de inhoud', 'navigation': 'Hoofdnavigatie',
            'previous': 'Vorige', 'next': 'Volgende', 'close': 'Sluiten',
            'closeDrawer': 'Sluit het zijpaneel', 'drawer': 'Extra informatie',
            'complete': 'Afgerond', 'incomplete': 'Nog niet afgerond',
            'correct': 'Goed', 'incorrect': 'Fout',
            'selectedAnswer': 'gekozen', 'unselectedAnswer': 'niet gekozen',
            'answeredIncorrectly': 'Je antwoord was fout',
            'answeredCorrectly': 'Je antwoord was goed',
            'selectAnswer': 'Kies een antwoord', 'done': 'Klaar'
        }}
    }
}

contentObjects, articles, blocks, components = [], [], [], []

for index, regel in enumerate(cursus.PAGINAS, start=1):
    module_naam, titel, samenvatting, tijd = regel
    co_id, art_id = 'co-%d' % index, 'a-%d' % index

    contentObjects.append({
        '_id': co_id, '_parentId': 'course', '_type': 'page', '_classes': '',
        'title': titel, 'displayTitle': titel, 'body': samenvatting,
        'pageBody': '', 'linkText': 'Bekijken', 'duration': tijd,
        '_graphic': {'alt': '', 'src': ''},
        '_pageLevelProgress': {'_isEnabled': True, '_isCompletionIndicatorEnabled': True}
    })

    artikel = {'_id': art_id, '_parentId': co_id, '_type': 'article',
               '_classes': '', 'title': titel, 'displayTitle': '',
               'body': '', 'instruction': ''}

    module = importlib.import_module('content.' + module_naam)

    # Een pagina met vragen die samen een toets vormen, zet TOETS op een id.
    toets = getattr(module, 'TOETS', None)
    if toets:
        artikel['_assessment'] = {
            '_isEnabled': True, '_id': toets,
            '_questions': {'_resetType': 'soft', '_canShowFeedback': True},
            '_scoreToPass': getattr(module, 'DREMPEL', 75), '_isPercentageBased': True,
            '_includeInTotalScore': True, '_assessmentWeight': 1,
            '_attempts': 'infinite', '_allowResetIfPassed': True,
            '_banks': {'_isEnabled': False}, '_randomisation': {'_isEnabled': False}
        }
    articles.append(artikel)

    pagina = Pagina(index, art_id)
    module.bouw(pagina)

    # Navigatie naar het volgende onderdeel. Bewust een gewone link en geen
    # trickle-knop: die gaat pas aan als Adapt de pagina als gezien markeert,
    # en dat hangt aan zichtbaarheidsdetectie die niet betrouwbaar te testen is.
    home = ('<a class="paginanav__knop paginanav__knop--stil" href="#/">'
            '<span class="paginanav__label">Terug naar</span>'
            '<span class="paginanav__titel">Overzicht</span></a>')

    volgende = cursus.PAGINAS[index] if index < len(cursus.PAGINAS) else None
    if volgende:
        link = ('<a class="paginanav__knop" href="#/id/co-%d">'
                '<span class="paginanav__label">Volgende onderdeel</span>'
                '<span class="paginanav__titel">%s</span></a>' % (index + 1, volgende[1]))
    else:
        link = ('<a class="paginanav__knop" href="#/id/co-1">'
                '<span class="paginanav__label">Terug naar het begin</span>'
                '<span class="paginanav__titel">%s</span></a>' % cursus.PAGINAS[0][1])
    pagina.tekst('', '<div class="paginanav__rij">%s%s</div>'
                 % (home, link)).update({'_classes': 'paginanav'})
    pagina.blokken[-1]['_classes'] = 'separator paginanav'

    # Dezelfde weg terug, maar dan bovenaan. Onderaan alleen is te weinig: je
    # moet dan eerst een heel hoofdstuk doorscrollen om bij het overzicht te
    # komen. Het blok wordt achteraan gebouwd en daarna vooraan gezet.
    pagina.tekst('', '<a class="terugnaar" href="#/">'
                     '<span class="terugnaar__pijl" aria-hidden="true">&#8592;</span>'
                     'Overzicht</a>').update({'_classes': 'terugnaar-blok'})
    pagina.blokken[-1]['_classes'] = 'terugnaar-blok'
    pagina.blokken.insert(0, pagina.blokken.pop())
    pagina.componenten.insert(0, pagina.componenten.pop())

    blocks.extend(pagina.blokken)
    components.extend(pagina.componenten)

    # De uitslag van een toets hoort in een eigen artikel, anders telt hij mee
    # als vraag in de toets zelf.
    if toets and hasattr(module, 'uitslag'):
        uit_art = art_id + '-uitslag'
        articles.append({'_id': uit_art, '_parentId': co_id, '_type': 'article',
                         '_classes': '', 'title': 'Uitslag', 'displayTitle': '',
                         'body': '', 'instruction': ''})
        uitslagpagina = Pagina(index * 10, uit_art)
        module.uitslag(uitslagpagina)
        blocks.extend(uitslagpagina.blokken)
        components.extend(uitslagpagina.componenten)

# controle op dubbele veld-id's: die zouden elkaars opgeslagen tekst overschrijven
veld_ids = []
for c in components:
    for stuk in c.get('body', '').split('id="')[1:]:
        vid = stuk.split('"')[0]
        if 'js-canvas-veld' in c.get('body', ''):
            veld_ids.append(vid)
dubbel = {v for v in veld_ids if veld_ids.count(v) > 1}
assert not dubbel, 'dubbele veld-id(s): %s' % dubbel

for naam, data in [('course.json', course), ('contentObjects.json', contentObjects),
                   ('articles.json', articles), ('blocks.json', blocks),
                   ('components.json', components)]:
    schrijf(naam, data)

tekens = sum(len(c.get('body', '')) for c in components)
print("%d pagina's, %d artikelen, %d blokken, %d componenten, ~%d tekens"
      % (len(contentObjects), len(articles), len(blocks), len(components), tekens))
