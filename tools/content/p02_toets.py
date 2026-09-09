# -*- coding: utf-8 -*-
"""Voorbeeld van een toetspagina.

TOETS zet een id: daarmee worden alle vragen op deze pagina samen één toets,
en kan de uitslag eronder de score tonen. Laat TOETS weg op gewone pagina's,
dan tellen de vragen niet mee voor een score.
"""

TOETS = 'kennischeck'
DREMPEL = 75


def bouw(p):
    p.tekst(
        'Kennischeck',
        '<p>Beantwoord de vragen hieronder. Je uitslag verschijnt onderaan zodra '
        'je ze allemaal hebt ingestuurd.</p>'
        '<p>Je hebt %d%% nodig om te slagen, en je mag het zo vaak proberen als '
        'je wilt.</p>' % DREMPEL)

    p.vraag(
        'Vraag 1',
        'Een vraag over een situatie uit de praktijk.',
        [
            ('Het juiste antwoord', True),
            ('Een plausibel alternatief', False),
            ('Nog een alternatief', False),
            ('En nog een', False),
        ],
        feedback={
            'title': 'Vraag 1',
            'correct': '<p>Goed.</p>',
            '_incorrect': {'final': '<p>Onjuist. Leg uit waar de denkfout zit.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet.</p>'}
        })

    p.koppelvraag(
        'Vraag 2',
        'Koppel elke uitspraak aan de categorie waar hij bij hoort.',
        rijen=[
            ('Een uitspraak die bij A hoort', 'Categorie A'),
            ('Een uitspraak die bij B hoort', 'Categorie B'),
        ],
        opties=['Categorie A', 'Categorie B'],
        feedback={
            'title': 'Vraag 2',
            'correct': '<p>Goed.</p>',
            '_incorrect': {'final': '<p>Onjuist. Benoem het onderscheid nog een keer.</p>'},
            '_partlyCorrect': {'final': '<p>Deels goed.</p>'}
        })


def uitslag(p):
    """Komt in een eigen artikel onder de vragen te staan."""
    p.uitslag(
        TOETS, drempel=DREMPEL,
        voldoende='Voldoende. Je hebt de stof te pakken.',
        onvoldoende='Dat is nog niet voldoende. Loop de stof nog eens door '
                    'en probeer het daarna opnieuw.')
