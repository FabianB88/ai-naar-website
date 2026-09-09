# -*- coding: utf-8 -*-
"""Van een map op je bureaublad naar een repository met geschiedenis."""


def bouw(p):
    p.tekst(
        'Wat een repository je oplevert',
        '<p>Een <b>repository</b> is je projectmap plus zijn geschiedenis. Je legt zelf '
        'vast wanneer er een moment bewaard moet worden — dat heet een <b>commit</b> — '
        'en je zet er in één zin bij wat je hebt veranderd.</p>'
        '<p>Vanaf dat moment verdwijnt niets meer. Je kunt zien wat je vorige week '
        'anders deed, twee versies naast elkaar leggen, en terug naar hoe het was '
        'voordat je verfijnde in de verkeerde richting. Dat is precies het probleem uit '
        'hoofdstuk 1, en dit is de oplossing.</p>'
        '<p>Er is nog een reden. Je assistent werkt veel prettiger in een map met '
        'versiebeheer: gaat een wijziging de mist in, dan kun je hem in één commando '
        'terugdraaien in plaats van te hopen dat je nog weet wat er stond.</p>')

    p.tekst(
        'Stappenplan: je pagina in een repository',
        '<p>Vijf stappen. Je assistent kan ze allemaal uitvoeren, maar lees mee — '
        'vooral stap 3.</p>'
        '<ol>'
        '<li><b>Maak een map met een nette naam</b> en zet je <code>index.html</code> '
        'uit hulpmiddel 15 erin. Gebruik kleine letters en streepjes, geen spaties: '
        '<code>materialenpaspoort-w3</code>.</li>'
        '<li><b>Begin de geschiedenis.</b> Eén commando, en Git houdt vanaf nu de map '
        'in de gaten.</li>'
        '<li><b>Zeg wat er níet in mag.</b> Voordat je je eerste commit maakt, want een '
        'bestand dat er eenmaal in zit, krijg je er lastig weer uit.</li>'
        '<li><b>Maak je eerste commit</b> met een boodschap die iets zegt.</li>'
        '<li><b>Zet hem op GitHub</b> met één commando dat de repository aanmaakt en '
        'meteen uploadt.</li>'
        '</ol>')

    p.commando(
        'Stap 2: de geschiedenis beginnen',
        '<p>Voer dit uit in je projectmap.</p>',
        beide='git init -b main',
        na='De -b main geeft je hoofdlijn de naam main. Zonder die toevoeging heet hij '
           'op oudere Git-versies master, en dan sluit hij later niet aan op wat GitHub '
           'verwacht.')

    p.tekst(
        'Stap 3: zeggen wat er niet in mag',
        '<p>Dit is het moment om even na te denken, want een repository is een '
        'geschiedenis: iets weghalen in een latere commit betekent niet dat het uit de '
        'geschiedenis verdwijnt. Wie terugbladert, vindt het gewoon terug. Bij een '
        'openbare repository vindt de hele wereld het terug.</p>'
        '<p>Maak daarom eerst een bestand met de naam <code>.gitignore</code> — met een '
        'punt ervoor — met daarin wat Git moet negeren.</p>')

    p.commando(
        '',
        '<p>De inhoud van dat bestand. Je assistent maakt hem in één keer voor je aan '
        'als je hem dit geeft.</p>',
        beide=[
            '# Instellingen van je editor en je systeem',
            '.vscode/',
            '.DS_Store',
            'Thumbs.db',
            '',
            '# Sleutels en instellingen die niet openbaar mogen',
            '.env',
            '*.key',
            'serviceAccount*.json',
            '',
            '# Firebase-werkbestanden',
            '.firebase/',
            'firebase-debug.log',
            '',
            '# Ruwe gegevens van je opdrachtgever',
            'data-ruw/',
        ],
        na='Die laatste map is een gewoonte die je jezelf aanleert: alles wat je ongefilterd '
           'van je opdrachtgever krijgt, zet je in een map die nooit meegaat.')

    p.aandacht(
        'Wat er nooit in een commit hoort',
        '<p>Vier dingen, en de eerste twee zijn niet terug te draaien als het misgaat.</p>'
        '<ul>'
        '<li><b>Sleutels en wachtwoorden.</b> Ook niet tijdelijk, ook niet in een '
        'private repository. Wordt hij ooit openbaar, dan staat het er nog.</li>'
        '<li><b>Persoonsgegevens.</b> Namen, e-mailadressen, respondentenlijsten. Een '
        'repository is geen plek voor gegevens over mensen.</li>'
        '<li><b>Ruwe gegevens van je opdrachtgever.</b> Cijfers die je mag gebruiken in '
        'je analyse mag je nog niet zomaar publiceren.</li>'
        '<li><b>Grote bestanden die je niet nodig hebt.</b> Een map met foto’s van vijf '
        'megabyte per stuk maakt je repository traag en levert niets op.</li>'
        '</ul>'
        '<p>Twijfel je bij een bestand? Laat het weg. Toevoegen kan altijd nog.</p>')

    p.commando(
        'Stap 4: je eerste commit',
        '<p>Twee commando’s: alles klaarzetten, en dan vastleggen met een boodschap.</p>',
        beide=[
            'git add .',
            'git commit -m "Eerste versie van de one-pager uit hulpmiddel 15"',
        ],
        na='Schrijf in de boodschap wát er veranderd is, niet dát er iets veranderd is. '
           '"Aanbeveling boven de tabel gezet" helpt je over drie weken; "update" niet.')

    p.commando(
        'Stap 5: op GitHub zetten',
        '<p>Eén commando maakt de repository aan, koppelt hem aan je map en uploadt '
        'alles.</p>',
        beide='gh repo create materialenpaspoort-w3 --private --source=. --push',
        na='Vervang de naam door die van jou. Je krijgt het adres van je nieuwe '
           'repository terug; open dat even in je browser om te zien dat je bestanden '
           'er staan.')

    p.accordeon(
        'Privé of openbaar?',
        '<p>Die keuze in het commando hierboven is geen detail. Je kunt hem later wel '
        'omzetten, maar wat openbaar is geweest, kan gekopieerd zijn.</p>',
        [
            {'title': 'Kies --private als',
             'body': '<p>Er gegevens van je opdrachtgever in zitten, ook al zijn ze '
                     'geanonimiseerd. Als je nog niet hebt gevraagd of het openbaar '
                     'mag. Als er cijfers in staan die nog concept zijn.</p>'
                     '<p>Dit is de standaard tijdens het project. Je kunt hem aan het '
                     'eind alsnog openzetten als je opdrachtgever akkoord is.</p>'},
            {'title': 'Kies --public als',
             'body': '<p>Alles op de pagina van jou is of openbaar mag zijn, en je '
                     'opdrachtgever ja heeft gezegd. Voordeel: je kunt de repository in '
                     'je portfolio of een sollicitatie laten zien, en je kunt gratis '
                     'GitHub Pages gebruiken.</p>'
                     '<p>Bij twijfel begin je privé. Openzetten is één klik; '
                     'terughalen wat er gekopieerd is, niet.</p>'},
            {'title': 'Wat je opdrachtgever eigenlijk moet weten',
             'body': '<p>Dat de code op GitHub staat, of hij openbaar is, en wat er '
                     'aan gegevens in zit. Dat is een gesprek van twee minuten '
                     '(hulpmiddel 06) en het voorkomt het ongemakkelijke moment '
                     'waarop hij het zelf ontdekt.</p>'},
        ])

    p.commando(
        'Vanaf nu: de lus',
        '<p>Elke keer dat je iets verandert, doe je deze drie. Meer is het niet.</p>',
        beide=[
            'git add .',
            'git commit -m "Wat je hebt veranderd"',
            'git push',
        ],
        na='Wil je zien wat je tot nu toe hebt vastgelegd: git log --oneline geeft je de '
           'lijst, nieuwste bovenaan.')

    p.invulvelden(
        'Oefening: je eigen repository',
        '<p>Doe de vijf stappen op je eigen pagina en vul daarna dit in.</p>',
        [
            ('h05-naam', 'Hoe heet je repository?', 'Kleine letters, streepjes'),
            ('h05-zichtbaar', 'Privé of openbaar, en waarom?',
             'Bij gegevens van je opdrachtgever: privé'),
            ('h05-negeren', 'Wat staat er in je .gitignore?',
             'En waarom staat het daarin?'),
            ('h05-commit', 'Wat was je eerste commitboodschap?',
             'Zegt hij wát er is veranderd?'),
            ('h05-url', 'Wat is het adres van je repository?',
             'github.com/jouwnaam/jouwproject'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Staat je pagina op GitHub? Dan kun je vanaf nu nooit meer iets kwijtraken '
        'wat je hebt vastgelegd. In het volgende hoofdstuk komt hij online.</p>')

    p.vraag(
        'Even checken',
        'Je hebt per ongeluk een bestand met de contactgegevens van tien respondenten '
        'gecommit en gepusht naar een privérepository. Wat klopt?',
        [
            ('Het bestand in een nieuwe commit weghalen is niet genoeg — het blijft in '
             'de geschiedenis staan. Meld het en overleg wat er moet gebeuren.', True),
            ('Geen probleem: je haalt het bestand weg en commit opnieuw.', False),
            ('Geen probleem, want de repository staat op privé.', False),
            ('Je maakt de repository openbaar zodat je hem kunt laten '
             'controleren.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt, en dit is waarom stap 3 vóór stap 4 komt. De '
                       'geschiedenis bewaart alles; een latere commit haalt het uit de '
                       'huidige versie maar niet uit het verleden. Bij persoonsgegevens '
                       'is dit een datalek, ook in een privérepository — meld het bij '
                       'je docent en je opdrachtgever.</p>',
            '_incorrect': {'final': '<p>Nog niet. Een commit weghalen verwijdert het '
                                    'bestand uit de nieuwste versie, maar wie '
                                    'terugbladert vindt het gewoon. Dat is precies de '
                                    'eigenschap die versiebeheer nuttig maakt, en hier '
                                    'werkt hij tegen je.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
