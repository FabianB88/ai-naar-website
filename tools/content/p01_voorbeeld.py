# -*- coding: utf-8 -*-
"""Voorbeeldpagina — laat elk soort blok zien.

Verwijder dit bestand zodra je eigen pagina's staan, en haal hem uit
PAGINAS in cursus.py.
"""


def bouw(p):
    p.tekst(
        'Een gewoon tekstblok',
        '<p>Dit is een tekstblok. De kop staat op de component, niet op het blok — '
        'anders staat hij dubbel op de pagina.</p>'
        '<p>In de body gebruik je gewone HTML: <b>vet</b>, <i>cursief</i>, en '
        'alinea\'s in <code>&lt;p&gt;</code>-tags. Schrijf liever meerdere korte '
        'alinea\'s dan één lange.</p>')

    p.aandacht(
        'Een aandachtsblok',
        '<p>Zelfde als een tekstblok, maar met een gekleurde rand ernaast. Gebruik '
        'dit spaarzaam: voor een waarschuwing, een kanttekening of iets wat de '
        'deelnemer echt moet weten voor hij verder gaat.</p>')

    # Zet je afbeelding in src/course/nl/images/ en verwijs naar de bestandsnaam.
    # De alt-tekst is verplicht: zonder alternatieve tekst is de pagina niet
    # toegankelijk, en dat is voor een onderwijsinstelling geen vrije keuze.
    #
    # p.beeld('mijn-diagram.svg',
    #         alt='Beschrijf wat er te zien is, niet dat het een diagram is. '
    #             'Bij een schema: benoem de onderdelen en hun samenhang.',
    #         onderschrift='Korte regel onder de afbeelding.',
    #         kop='Kop boven de afbeelding')

    p.accordeon(
        'Een accordeon',
        '<p>Voor uitleg die niet iedereen tegelijk hoeft te lezen.</p>',
        [
            {'title': 'Eerste item',
             'body': '<p>De inhoud van het eerste item.</p>'},
            {'title': 'Tweede item',
             'body': '<p>De inhoud van het tweede item.</p>'}
        ])

    p.vraag(
        'Een tussenvraag',
        'Stel een vraag over een situatie, niet over een definitie. '
        'Toepassen onthoudt beter dan opzeggen.',
        [
            ('Het juiste antwoord', True),
            ('Een plausibel maar fout antwoord', False),
            ('Nog een fout antwoord', False),
        ],
        feedback={
            'title': 'Een tussenvraag',
            'correct': '<p>Klopt. Leg in één zin uit wáárom het klopt.</p>',
            '_incorrect': {'final': '<p>Niet juist. Leg uit wat er misgaat in de '
                                    'denkfout, niet alleen wat het goede antwoord is.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.invulvelden(
        'Invulvelden',
        '<p>Vrije tekstvelden. Wat de deelnemer typt wordt bewaard in zijn eigen '
        'browser en blijft staan als hij later terugkomt.</p>',
        [
            ('vb-veld-1', 'Label boven het veld', 'Grijze hint in het veld'),
            ('vb-veld-2', 'Nog een veld', 'Nog een hint'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Onder een reeks invulvelden zet je deze knoppen, zodat de deelnemer '
        'zijn antwoorden kan kopiëren naar zijn eigen bestanden.</p>')
