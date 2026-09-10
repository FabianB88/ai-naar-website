# -*- coding: utf-8 -*-
"""Van een map op je bureaublad naar een repository met geschiedenis."""


def bouw(p):
    p.tekst(
        'Wat een repository je oplevert',
        '<p>Een <b>repository</b> is je projectmap plus zijn geschiedenis. Elke keer dat '
        'je iets vastlegt — een <b>commit</b> — wordt er een moment bewaard, met één zin '
        'erbij over wat er veranderd is.</p>'
        '<p>Vanaf dat moment verdwijnt niets meer. Je kunt terug naar hoe het was '
        'voordat je de verkeerde kant op verfijnde, en je assistent kan een mislukte '
        'wijziging in één commando terugdraaien. Dat is precies het probleem uit '
        'hoofdstuk 1, en dit is de oplossing.</p>')

    p.tekst(
        'Wat jij beslist, en wat je assistent doet',
        '<p>Het werk in dit hoofdstuk — de repository beginnen, een uitsluitlijst '
        'schrijven, vastleggen, op GitHub zetten — doet je assistent in één keer. Aan '
        'jou zijn twee <b>beslissingen</b> en één <b>controle</b>:</p>'
        '<ul>'
        '<li><b>Hoe heet het?</b> Kleine letters en streepjes, want de naam komt in je '
        'adres te staan: <code>materialenpaspoort-w3</code>.</li>'
        '<li><b>Privé of openbaar?</b> Zie hieronder. Bij twijfel: privé.</li>'
        '<li><b>Wat gaat er mee?</b> Voordat er iets wordt vastgelegd, laat je '
        'assistent je de lijst met bestanden zien. Die lees jij. Dit is de enige stap '
        'in dit hoofdstuk die je niet mag overslaan.</li>'
        '</ul>')

    p.commando(
        'De prompt',
        '<p>Zet je <code>index.html</code> uit hulpmiddel 15 in een lege map, open daar '
        'je assistent, en geef dit — met jouw naam en jouw keuze erin.</p>',
        beide=[
            'Zet deze map onder versiebeheer en publiceer hem op GitHub:',
            '',
            '1. Stel mijn Git-naam in als dat nog niet is gebeurd, en gebruik als',
            '   e-mailadres mijn GitHub-noreply-adres. Haal dat op via gh api user.',
            '2. Begin een repository met de hoofdlijn main.',
            '3. Schrijf een .gitignore die in elk geval uitsluit: .env, sleutels,',
            '   serviceAccount-bestanden, .firebase/, logbestanden en de map data-ruw/.',
            '4. Laat me de lijst zien van alles wat in de eerste commit gaat, en',
            '   wacht op mijn akkoord.',
            '5. Leg het vast met een boodschap die zegt wat erin zit.',
            '6. Maak op GitHub de repository materialenpaspoort-w3 aan als PRIVE',
            '   en push. Geef me daarna het adres.',
        ],
        na='Stap 4 is de reden dat deze prompt zo lang is. Zonder die regel legt je '
           'assistent gewoon alles vast wat in de map staat — ook dat ene bestand dat '
           'je vergeten was.')

    p.aandacht(
        'Die lijst lees je echt',
        '<p>Een repository is een geschiedenis: iets weghalen in een latere commit '
        'haalt het niet uit het verleden. Wie terugbladert, vindt het gewoon terug. Bij '
        'een openbare repository vindt de hele wereld het terug.</p>'
        '<p>Loop de lijst dus na op vier dingen, en zeg nee als er iets tussen staat:</p>'
        '<ul>'
        '<li><b>Sleutels en wachtwoorden</b>, ook niet tijdelijk.</li>'
        '<li><b>Persoonsgegevens</b>: namen, e-mailadressen, respondentenlijsten.</li>'
        '<li><b>Ruwe gegevens van je opdrachtgever.</b> Cijfers die je mag gebruiken in '
        'je analyse, mag je nog niet zomaar publiceren.</li>'
        '<li><b>Grote bestanden die je niet nodig hebt</b>, zoals een map met foto’s '
        'van vijf megabyte per stuk.</li>'
        '</ul>'
        '<p>Twijfel je bij een bestand? Laat het weg. Toevoegen kan altijd nog.</p>')

    p.commando(
        'Wat hij dan uitvoert',
        '<p>Ter herkenning, niet om over te tikken. Loopt je assistent ergens vast, dan '
        'zie je hier waar hij was.</p>',
        beide=[
            'gh api user --jq ".id, .login"',
            'git config --global user.name "Jelle Bakker"',
            'git config --global user.email "1234567+jellebakker@users.noreply.github.com"',
            'git init -b main',
            'git add .',
            'git status',
            'git commit -m "Eerste versie van het materialenpaspoort"',
            'gh repo create materialenpaspoort-w3 --private --source=. --push',
        ],
        na='git status is het moment waarop hij je de lijst laat zien. Het '
           'noreply-adres zorgt dat je echte e-mailadres niet in elke commit komt te '
           'staan, ook niet als de repository later openbaar wordt.')

    p.accordeon(
        'Privé of openbaar?',
        '<p>Je kunt het later omzetten, maar wat openbaar is geweest, kan gekopieerd '
        'zijn.</p>',
        [
            {'title': 'Kies privé als',
             'body': '<p>Er gegevens van je opdrachtgever in zitten, ook als ze '
                     'geanonimiseerd zijn. Als je nog niet hebt gevraagd of het openbaar '
                     'mag. Als er cijfers in staan die nog concept zijn.</p>'
                     '<p>Dit is de standaard tijdens het project. Openzetten kan aan het '
                     'eind, als je opdrachtgever akkoord is.</p>'},
            {'title': 'Kies openbaar als',
             'body': '<p>Alles op de pagina van jou is of openbaar mag zijn, en je '
                     'opdrachtgever ja heeft gezegd. Voordeel: je kunt de repository in je '
                     'portfolio laten zien, en je kunt gratis GitHub Pages gebruiken.</p>'
                     '<p>Wil je dat, vervang dan PRIVE in de prompt door OPENBAAR.</p>'},
            {'title': 'Wat je opdrachtgever moet weten',
             'body': '<p>Dat de code op GitHub staat, of hij openbaar is, en wat er aan '
                     'gegevens in zit. Een gesprek van twee minuten (hulpmiddel 09), en '
                     'het voorkomt het moment waarop hij het zelf ontdekt.</p>'},
        ])

    p.commando(
        'Vanaf nu: één zin',
        '<p>Heb je iets veranderd, dan zeg je tegen je assistent:</p>',
        beide='Leg vast wat ik net heb veranderd en push het.',
        na='Hij kiest zelf een boodschap. Zegt die "update", vraag dan om een betere: '
           '"Demontagestappen toegevoegd" helpt je over drie weken, "update" niet. Wil je '
           'terugzien wat er is vastgelegd, vraag dan om de geschiedenis.')

    p.invulvelden(
        'Oefening: je eigen repository',
        '<p>Geef de prompt voor je eigen pagina en vul daarna dit in.</p>',
        [
            ('h05-naam', 'Hoe heet je repository?', 'Kleine letters, streepjes'),
            ('h05-zichtbaar', 'Privé of openbaar, en waarom?',
             'Bij gegevens van je opdrachtgever: privé'),
            ('h05-lijst', 'Stond er iets in de lijst dat je hebt tegengehouden?',
             'Wat, en waarom?'),
            ('h05-commit', 'Welke commitboodschap koos je assistent?',
             'Zegt hij wát er is veranderd?'),
            ('h05-url', 'Wat is het adres van je repository?',
             'github.com/jouwnaam/jouwproject'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Staat je pagina op GitHub? Dan raak je vanaf nu niets meer kwijt wat je hebt '
        'vastgelegd. In het volgende hoofdstuk komt hij online.</p>')

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
            'correct': '<p>Klopt, en dit is waarom je de lijst leest vóórdat er iets '
                       'wordt vastgelegd. De geschiedenis bewaart alles; een latere '
                       'commit haalt het uit de huidige versie maar niet uit het '
                       'verleden. Bij persoonsgegevens is dit een datalek, ook in een '
                       'privérepository — meld het bij je docent en je '
                       'opdrachtgever.</p>',
            '_incorrect': {'final': '<p>Nog niet. Een commit weghalen verwijdert het '
                                    'bestand uit de nieuwste versie, maar wie '
                                    'terugbladert vindt het gewoon. Dat is precies de '
                                    'eigenschap die versiebeheer nuttig maakt, en hier '
                                    'werkt hij tegen je.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
