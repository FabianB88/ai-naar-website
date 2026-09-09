# -*- coding: utf-8 -*-
"""Git, Node en de twee CLI's installeren, het liefst door je assistent."""


def bouw(p):
    p.tekst(
        'Vier onderdelen, en wat ze doen',
        '<p>Voor je iets kunt publiceren, moet er vier keer iets op je computer staan. '
        'Je hoeft niet te snappen hoe ze werken, wel waarvoor ze er zijn — anders weet '
        'je bij een foutmelding niet welke van de vier je moet aankijken.</p>'
        '<ul>'
        '<li><b>Git</b> houdt de geschiedenis van je bestanden bij. Elke keer dat je '
        'iets vastlegt, kun je daar later naar terug.</li>'
        '<li><b>Node.js</b> is de motor waar de Firebase CLI op draait. Je gebruikt '
        'het zelf niet direct.</li>'
        '<li><b>GitHub CLI</b> (het commando <code>gh</code>) laat je vanaf de '
        'opdrachtregel met GitHub praten: inloggen, een repository aanmaken, '
        'pushen.</li>'
        '<li><b>Firebase CLI</b> (het commando <code>firebase</code>) doet hetzelfde '
        'voor Firebase: inloggen, je project kiezen, publiceren.</li>'
        '</ul>')

    p.aandacht(
        'Laat je assistent dit doen',
        '<p>Dit hele hoofdstuk kun je uitbesteden. Claude Code en Codex draaien '
        'commando’s op jouw computer en kunnen deze vier zelf installeren, controleren '
        'en repareren als er iets misgaat.</p>'
        '<p>De commando’s staan er hieronder toch bij. Niet omdat je ze moet '
        'overtikken, maar zodat je kunt volgen wat er gebeurt en het zelf kunt doen als '
        'je assistent ergens vastloopt. Dat is het verschil tussen iets laten doen en '
        'iets uitbesteden zonder te weten wat je uitbesteedt.</p>')

    p.tekst(
        'De prompt',
        '<p>Open je terminal in de map van je project, start Claude Code of Codex, en '
        'geef deze opdracht. Hij is expres uitgeschreven: hij zegt wat er moet gebeuren, '
        'wat er níet mag, en hoe je assistent moet controleren of het gelukt is.</p>')

    p.commando(
        '',
        '',
        beide=[
            'Installeer op deze computer: Git, Node.js LTS, de GitHub CLI (gh)',
            'en de Firebase CLI (firebase-tools). Gebruik winget op Windows of',
            'Homebrew op macOS, en npm voor firebase-tools.',
            '',
            'Controleer daarna van alle vier het versienummer en laat mij de',
            'uitvoer zien.',
            '',
            'Log nergens in en maak geen accounts aan: dat doe ik zelf in de',
            'volgende stap. Vul nooit betaalgegevens in.',
        ],
        na='Kopieer deze prompt en plak hem in je assistent. Hij vraagt onderweg om '
           'toestemming per commando — lees die even door voor je goedkeurt.')

    p.commando(
        'Wat hij dan uitvoert: installeren',
        '<p>Op Windows via winget, dat standaard op Windows 11 staat. Op macOS via '
        '<a href="https://brew.sh" target="_blank" rel="noopener">Homebrew</a>; heb je '
        'dat nog niet, dan installeert je assistent het eerst.</p>',
        windows=[
            'winget install --id Git.Git -e --source winget',
            'winget install --id OpenJS.NodeJS.LTS -e --source winget',
            'winget install --id GitHub.cli -e --source winget',
            'npm install -g firebase-tools',
        ],
        mac=[
            'brew install git',
            'brew install node',
            'brew install gh',
            'npm install -g firebase-tools',
        ],
        na='De laatste regel is op beide hetzelfde: de Firebase CLI komt via npm, en '
           'npm krijg je met Node.js mee.')

    p.commando(
        'Wat hij dan uitvoert: controleren',
        '<p>Vier versienummers. Komt er bij een van de vier een foutmelding, dan is '
        'juist díe niet gelukt — dan weet je meteen waar je moet zoeken.</p>',
        beide=[
            'git --version',
            'node --version',
            'gh --version',
            'firebase --version',
        ],
        na='Je ziet dan zoiets als git version 2.55.0, v24.19.0, gh version 2.100.0 '
           'en 15.13.0. De exacte nummers doen er niet toe, als er maar een nummer '
           'staat.')

    p.accordeon(
        'Als er iets misgaat',
        '<p>Vier meldingen die je waarschijnlijk gaat zien, en wat ze betekenen.</p>',
        [
            {'title': '"is niet herkend als de naam van een cmdlet" of "command not '
                      'found"',
             'body': '<p>Verreweg de meest voorkomende, en bijna nooit een echt '
                     'probleem. Een pas geïnstalleerd programma komt pas in een '
                     '<i>nieuwe</i> terminal beschikbaar; het venster dat al openstond '
                     'weet nog van niets.</p>'
                     '<p>Sluit je terminal helemaal af, open een nieuwe, en probeer het '
                     'versiecommando opnieuw. Werkt het dan nog niet, dan is de '
                     'installatie echt mislukt.</p>'},
            {'title': 'winget wordt niet gevonden',
             'body': '<p>Je zit op een oudere Windows, of op een beheerde laptop waar '
                     'de App Installer ontbreekt. Installeer <i>App Installer</i> uit '
                     'de Microsoft Store, of haal Git en de GitHub CLI op als gewone '
                     'installatiebestanden van <a href="https://git-scm.com" '
                     'target="_blank" rel="noopener">git-scm.com</a> en '
                     '<a href="https://cli.github.com" target="_blank" '
                     'rel="noopener">cli.github.com</a>.</p>'},
            {'title': 'npm geeft een rechtenfout (EACCES) op macOS',
             'body': '<p>Je probeert iets te installeren in een map waar je niet bij '
                     'mag. Zet <code>sudo</code> er niet zomaar voor: dat werkt wel, '
                     'maar geeft later nieuwe problemen.</p>'
                     '<p>De nettere weg is Node via Homebrew installeren in plaats van '
                     'via de installer van nodejs.org, want dan staat npm in een map '
                     'die van jou is. Laat je assistent dit uitzoeken en leg hem de '
                     'exacte foutmelding voor.</p>'},
            {'title': 'De schoollaptop laat niets installeren',
             'body': '<p>Op een beheerde laptop kan installeren geblokkeerd zijn. Werk '
                     'dan op je eigen laptop, of vraag ICT om de vier onderdelen te '
                     'plaatsen.</p>'
                     '<p>Wat je niet doet, is beveiligingsinstellingen omzeilen omdat '
                     'een AI-assistent daar een manier voor weet. Dat is geen '
                     'technisch probleem maar een afspraak.</p>'},
        ])

    p.invulvelden(
        'Oefening: leg je installatie vast',
        '<p>Noteer wat er bij jou uitkwam. Loop je later vast, dan zie je hier meteen '
        'of het aan de installatie ligt.</p>',
        [
            ('h03-os', 'Werk je op Windows of macOS?', ''),
            ('h03-versies', 'Welke vier versienummers kwamen eruit?',
             'git, node, gh, firebase'),
            ('h03-fout', 'Ging er iets mis? Wat stond er precies?',
             'De letterlijke melding, niet je samenvatting ervan'),
            ('h03-oplossing', 'Hoe is het opgelost?',
             'Zodat je het over drie maanden terugvindt'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Werken alle vier de versiecommando’s? Dan is het zware deel voorbij. De '
        'rest van de cursus gaat over gebruiken wat er nu staat.</p>')

    p.vraag(
        'Even checken',
        'Je hebt net de GitHub CLI geïnstalleerd, maar <code>gh --version</code> geeft '
        '"command not found". Wat is de eerste die je probeert?',
        [
            ('Je terminal sluiten en een nieuwe openen — een nieuw geïnstalleerd '
             'commando is pas in een nieuw venster bekend.', True),
            ('De installatie nog een keer draaien.', False),
            ('Je computer opnieuw opstarten.', False),
            ('Een andere manier van installeren zoeken.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies, en het scheelt je een hoop tijd. Je terminal leest '
                       'bij het opstarten één keer waar hij programma’s moet zoeken. '
                       'Wat daarna wordt geïnstalleerd, ziet hij pas in een nieuw '
                       'venster.</p>',
            '_incorrect': {'final': '<p>Nog niet. Opnieuw installeren of herstarten '
                                    'werkt soms toevallig, maar je doet dan veel te '
                                    'veel. Begin met een nieuwe terminal: dat is de '
                                    'oorzaak in negen van de tien gevallen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
