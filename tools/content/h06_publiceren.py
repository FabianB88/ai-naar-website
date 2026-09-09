# -*- coding: utf-8 -*-
"""Publiceren op Firebase Hosting, bijwerken, en terug als het misgaat."""


def bouw(p):
    p.tekst(
        'Van een bestand naar een adres',
        '<p>Publiceren betekent hier: je bestanden komen op een server van Google te '
        'staan en krijgen een webadres. Iedereen met dat adres kan je pagina openen, op '
        'elk apparaat, zonder dat jouw laptop aan hoeft te staan.</p>'
        '<p>Je krijgt twee adressen die allebei naar hetzelfde wijzen: '
        '<code>jouw-project.web.app</code> en <code>jouw-project.firebaseapp.com</code>. '
        'Gebruik de eerste, die is korter. Een eigen domeinnaam kan ook, maar dat kost '
        'geld en dat gaan we niet doen.</p>'
        '<p>De verbinding is meteen beveiligd met https, daar hoef je niets voor te '
        'regelen.</p>')

    p.tekst(
        'Stappenplan: publiceren',
        '<p>Drie stappen, en één prompt doet de eerste twee. Voer dit uit in dezelfde '
        'map als je repository uit hoofdstuk 5.</p>'
        '<ol>'
        '<li><b>Laat je assistent Hosting inrichten.</b> Hij schrijft twee kleine '
        'bestanden en verplaatst je pagina naar de juiste map.</li>'
        '<li><b>Publiceren.</b> Eén commando, en je krijgt je adres terug.</li>'
        '<li><b>Vastleggen.</b> Zodat je repository klopt met wat er online staat.</li>'
        '</ol>')

    p.commando(
        'Stap 1: de prompt',
        '',
        beide=[
            'Richt Firebase Hosting in voor dit project. Maak een map public,',
            'verplaats mijn index.html daarheen, en schrijf firebase.json en',
            '.firebaserc met mijn project-id erin. Geen single-page app en geen',
            'GitHub Actions.',
            '',
            'Gebruik de init-wizard niet, schrijf de bestanden gewoon zelf.',
            'Laat me daarna zien wat erin staat.',
        ],
        na='Die laatste instructie is belangrijk. "firebase init hosting" is een wizard '
           'die op antwoorden wacht, en daar loopt een assistent op vast. De twee '
           'bestanden die de wizard maakt, kan hij prima zelf schrijven.')

    p.commando(
        'Wat er dan in firebase.json staat',
        '<p>Je hoeft dit niet uit je hoofd te kennen, maar je moet het wel kunnen '
        'herkennen. Er staat: neem alles uit de map <code>public</code>, behalve deze '
        'drie dingen.</p>',
        beide=[
            '{',
            '  "hosting": {',
            '    "public": "public",',
            '    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"]',
            '  }',
            '}',
        ],
        na='In .firebaserc staat alleen welk project erbij hoort. Allebei horen ze gewoon '
           'in je repository — er zit niets geheims in.')

    p.aandacht(
        'Wat niet in public staat, komt niet online',
        '<p>Dat is precies de bedoeling, en het is meteen je vangnet. Je aantekeningen, '
        'je ruwe data en je losse notities staan buiten die map en gaan dus niet mee, ook '
        'niet per ongeluk.</p>'
        '<p>Omgekeerd: heb je afbeeldingen of een los CSS-bestand, dan moeten die '
        'wél in <code>public</code>. Staat je pagina online zonder opmaak, dan is dit '
        'bijna altijd de reden.</p>')

    p.commando(
        'Stap 2: publiceren',
        '',
        beide='firebase deploy --only hosting',
        na='Na een halve minuut staat er "Deploy complete!" met daaronder je Hosting URL. '
           'Open die meteen even, ook op je telefoon.')

    p.commando(
        'Stap 3: vastleggen',
        '<p>Er zijn bestanden bijgekomen en je pagina is verplaatst. Leg dat vast, anders '
        'loopt je repository achter op wat er online staat.</p>',
        beide=[
            'git add .',
            'git commit -m "Firebase Hosting ingericht en eerste versie gepubliceerd"',
            'git push',
        ],
        na='Ook dit kun je in één zin aan je assistent vragen: leg vast en publiceer.')

    p.aandacht(
        'Publiceren en vastleggen zijn twee dingen',
        '<p>Dit is de verwarring die het vaakst voorkomt. <code>git push</code> zet je '
        'code op GitHub. <code>firebase deploy</code> zet je pagina online. Ze hebben '
        'niets met elkaar te maken.</p>'
        '<p>Je kunt dus publiceren zonder te committen — dan staat er iets online dat '
        'in geen enkele versie is vastgelegd. En je kunt committen zonder te '
        'publiceren — dan is de site nog de oude. Doe ze allebei, in die volgorde: '
        'eerst vastleggen, dan publiceren. Dan hoort bij elke live versie een commit '
        'die je kunt terugvinden.</p>')

    p.commando(
        'De bijwerklus',
        '<p>Vanaf nu ziet elke wijziging er zo uit. Je assistent kan deze drie in één '
        'keer voor je doen als je zegt: leg vast en publiceer.</p>',
        beide=[
            'git add .',
            'git commit -m "Demontagestappen toegevoegd"',
            'git push',
            'firebase deploy --only hosting',
        ])

    p.accordeon(
        'Twee dingen die je een keer nodig hebt',
        '<p>Niet nu, maar wel op het moment dat je ze nodig hebt — en dan wil je weten '
        'dat ze bestaan.</p>',
        [
            {'title': 'Een voorbeeldversie delen zonder te publiceren',
             'body': '<p>Wil je je opdrachtgever iets laten zien dat nog niet af is, '
                     'zet het dan op een <b>preview-kanaal</b>. Dat geeft een apart, '
                     'moeilijk te raden adres dat vanzelf verloopt. Je echte site '
                     'blijft ongewijzigd.</p>'
                     '<p><code>firebase hosting:channel:deploy voorbeeld --expires '
                     '7d</code></p>'
                     '<p>Zeven dagen is de standaard, dertig dagen is het maximum. '
                     'Precies goed voor een sprintreview.</p>'},
            {'title': 'Terug naar een vorige versie',
             'body': '<p>Er is geen commando voor. Terugdraaien doe je in de '
                     'Firebase-console: ga naar <i>Hosting</i>, kijk in de lijst met '
                     'releases, en kies bij de versie die het wel deed voor '
                     '<i>Terugdraaien</i>. Binnen een paar seconden staat die er weer '
                     'op.</p>'
                     '<p>Moet de site helemaal uit de lucht, bijvoorbeeld omdat er per '
                     'ongeluk vertrouwelijke gegevens op staan, dan is '
                     '<code>firebase hosting:disable</code> de snelste weg. Daarna kun '
                     'je rustig repareren.</p>'},
        ])

    p.tekst(
        'Vier plekken om het neer te zetten',
        '<p>Firebase Hosting is niet de enige route, en het is goed om te weten wanneer '
        'je wat kiest. Deze vier zijn allemaal gratis en vragen geen betaalgegevens. Ze '
        'verschillen in wat ze kunnen dráaien: alleen bestanden, of ook code.</p>'
        '<p>De korte versie:</p>'
        '<ul>'
        '<li>Alleen een pagina, en hij mag openbaar &mdash; <b>GitHub Pages</b>.</li>'
        '<li>Een pagina die ook gegevens bewaart &mdash; <b>Firebase Hosting</b>, wat we '
        'hier doen.</li>'
        '<li>Je hebt echte servercode nodig, en het is je eigen project &mdash; '
        '<b>Vercel</b>.</li>'
        '<li>Je wilt een draaiende server even uitproberen &mdash; <b>Render</b>.</li>'
        '</ul>'
        '<p>Kies er één en leer die goed. Wisselen halverwege kost je meer tijd dan het '
        'oplevert, en aan je opdrachtgever kun je toch niet uitleggen waarom het adres '
        'ineens anders is.</p>')

    p.accordeon(
        'De vier naast elkaar',
        '<p>Per optie: wat je krijgt, en waar hij ophoudt.</p>',
        [
            {'title': 'GitHub Pages — het snelst, als je alleen een pagina hebt',
             'body': '<p>Je hebt er geen tweede account voor nodig: je code staat er al. '
                     'Zet je bestanden in een map <code>docs</code>, en zet in de '
                     'instellingen van je repository Pages aan op branch '
                     '<code>main</code> en die map. Je adres wordt '
                     '<code>jouwnaam.github.io/projectnaam</code>.</p>'
                     '<p><b>Waar het ophoudt:</b> het serveert alleen bestanden. Geen '
                     'database, geen formulier dat iets bewaart, geen code die op een '
                     'server draait. En op de gratis laag moet je repository openbaar '
                     'zijn — bij gegevens van je opdrachtgever is dat meteen een '
                     'probleem.</p>'},
            {'title': 'Firebase Hosting — als er iets bewaard moet worden',
             'body': '<p>Wat we in dit hoofdstuk doen. Iets meer opzetwerk, maar je zit '
                     'meteen naast Firestore, en dat scheelt je in hoofdstuk 7 een hoop '
                     'gedoe. Je repository mag gewoon privé blijven. Je krijgt '
                     'preview-kanalen om iets voor te leggen zonder te publiceren.</p>'
                     '<p><b>Waar het ophoudt:</b> je eigen servercode draaien kan hier '
                     'niet zonder Cloud Functions, en die vragen het betaalplan. Voor '
                     'een formulier dat gegevens wegschrijft heb je dat niet nodig — de '
                     'browser praat rechtstreeks met de database, beveiligd door de '
                     'regels uit hoofdstuk 7.</p>'},
            {'title': 'Vercel — als je echte backendcode wilt',
             'body': '<p>Je koppelt je GitHub-repository en Vercel publiceert bij elke '
                     'push automatisch. Je krijgt een adres op <code>vercel.app</code>, '
                     'en per pull request een eigen voorbeeldadres. Je kunt er '
                     'serverless functies op draaien, dus je kunt echte backendcode '
                     'kwijt zonder een server te beheren. Het gratis Hobby-plan vraagt '
                     'geen betaalgegevens en stuurt je ook geen rekening: ga je over een '
                     'grens, dan pauzeert dat onderdeel ongeveer een maand.</p>'
                     '<p><b>Let op, en dit is voor jullie relevant:</b> Hobby is volgens '
                     'de voorwaarden alleen voor persoonlijke, niet-commerciële '
                     'projecten. Bouw je iets voor een echte opdrachtgever die er zijn '
                     'werk mee doet, dan wringt dat met die voorwaarden. Voor een '
                     'prototype in je studie zit je goed; voor een product dat je '
                     'oplevert en dat blijft draaien, kies je iets anders of overleg je '
                     'het.</p>'},
            {'title': 'Render — om een echte server te testen',
             'body': '<p>Statische sites zijn er gratis, en je kunt er ook een echte '
                     'webservice draaien: Node, Python, wat je wilt, met een database '
                     'ernaast. Geen betaalgegevens nodig. Dat maakt het de handigste '
                     'plek om iets uit te proberen wat meer moet doen dan bestanden '
                     'serveren.</p>'
                     '<p><b>Waar het ophoudt:</b> een gratis webservice valt na een '
                     'kwartier zonder verkeer in slaap en doet er dan dertig tot zestig '
                     'seconden over om wakker te worden. Wie erop klikt, kijkt zolang '
                     'naar een lege pagina. Prima om zelf te testen of live iets te '
                     'demonstreren, niet om een adres aan je opdrachtgever te geven. De '
                     'gratis database verloopt bovendien na dertig dagen — zet daar '
                     'niets in wat je nodig hebt.</p>'},
        ])

    p.invulvelden(
        'Oefening: jouw site online',
        '<p>Publiceer je eigen pagina en vul dit in.</p>',
        [
            ('h06-url', 'Wat is je Hosting-adres geworden?', 'De .web.app-versie'),
            ('h06-telefoon', 'Hoe ziet hij eruit op een telefoon?',
             'Echt even kijken, niet alleen het venster smal maken'),
            ('h06-verschil', 'Wat is het verschil tussen git push en firebase deploy?',
             'In je eigen woorden'),
            ('h06-delen', 'Deel je een preview of het echte adres? Waarom?',
             'Concept-cijfers horen niet op het open web'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Zet je adres in je aantekeningen en stuur het nog niet rond. In hoofdstuk 8 '
        'staat de lijst die je eerst langsloopt.</p>')

    p.vraag(
        'Even checken',
        'Je hebt een tekst aangepast, gecommit en gepusht. Je opent je Hosting-adres en '
        'ziet nog de oude tekst. Wat is er aan de hand?',
        [
            ('Je hebt nog niet gepubliceerd. Committen en pushen zetten je code op '
             'GitHub, maar veranderen niets aan de live site.', True),
            ('De wijziging is niet goed opgeslagen.', False),
            ('Firebase heeft tijd nodig; morgen staat het er wel op.', False),
            ('Je moet je repository openbaar maken.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Twee gescheiden dingen: GitHub bewaart je '
                       'geschiedenis, Firebase serveert je pagina. Draai '
                       '<code>firebase deploy --only hosting</code> en ververs. Zie je '
                       'het dan nog niet, ververs dan hard met Ctrl+F5 — dan zit je '
                       'browser je in de weg.</p>',
            '_incorrect': {'final': '<p>Nog niet. Er is niets stuk en je hoeft niet te '
                                    'wachten. Je hebt je code vastgelegd maar niet '
                                    'gepubliceerd; dat zijn twee losse handelingen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
