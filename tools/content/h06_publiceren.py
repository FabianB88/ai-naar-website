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
        'Stappenplan: publiceren in vier stappen',
        '<p>Voer dit uit in dezelfde map als je repository uit hoofdstuk 5.</p>'
        '<ol>'
        '<li><b>Zet Hosting klaar</b> met de init-wizard. Dat doe je één keer per '
        'project.</li>'
        '<li><b>Verplaats je pagina</b> naar de map die de wizard heeft gemaakt.</li>'
        '<li><b>Publiceer.</b> Eén commando, en je krijgt je adres terug.</li>'
        '<li><b>Leg de nieuwe bestanden vast</b> in een commit, zodat je repository '
        'klopt met wat er online staat.</li>'
        '</ol>')

    p.commando(
        'Stap 1: Hosting klaarzetten',
        '',
        beide='firebase init hosting',
        na='Ook dit is een wizard met vragen. De antwoorden staan hieronder.')

    p.tekst(
        '',
        '<ol>'
        '<li><b>Please select an option</b> → <code>Use an existing project</code>, en '
        'kies dan het project uit hoofdstuk 2.</li>'
        '<li><b>What do you want to use as your public directory?</b> → '
        '<code>public</code>. Dat is de map waarvan de inhoud online komt; alles '
        'daarbuiten blijft privé.</li>'
        '<li><b>Configure as a single-page app?</b> → <code>No</code>. Dat is voor '
        'webapps met eigen navigatie; jij hebt losse pagina’s.</li>'
        '<li><b>Set up automatic builds and deploys with GitHub?</b> → <code>No</code>. '
        'Kan later; nu wil je eerst begrijpen wat er gebeurt als je zelf '
        'publiceert.</li>'
        '<li><b>File public/index.html already exists. Overwrite?</b> → <code>No</code>, '
        'als je je eigen pagina daar al had staan. Anders maakt hij er een '
        'welkomstpagina overheen.</li>'
        '</ol>'
        '<p>Je hebt nu twee nieuwe bestanden: <code>firebase.json</code> met de '
        'instellingen, en <code>.firebaserc</code> waarin staat welk project erbij '
        'hoort. Die horen allebei gewoon in je repository.</p>')

    p.commando(
        'Stap 2: je pagina op de goede plek',
        '<p>Alles wat online moet komen, gaat in <code>public</code>. Staat je pagina '
        'nog in de hoofdmap, verplaats hem dan.</p>',
        windows='Move-Item index.html public\\index.html -Force',
        mac='mv index.html public/index.html',
        na='Heb je ook afbeeldingen of een los CSS-bestand, dan gaan die mee in dezelfde '
           'map. Wat niet in public staat, komt niet online.')

    p.commando(
        'Stap 3: publiceren',
        '',
        beide='firebase deploy --only hosting',
        na='Na een halve minuut staat er "Deploy complete!" met daaronder je Hosting '
           'URL. Open die meteen even, ook op je telefoon.')

    p.commando(
        'Stap 4: vastleggen',
        '<p>De wizard heeft bestanden gemaakt en je hebt dingen verplaatst. Leg dat '
        'vast, anders loopt je repository achter op wat er online staat.</p>',
        beide=[
            'git add .',
            'git commit -m "Firebase Hosting ingericht en eerste versie gepubliceerd"',
            'git push',
        ])

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
            'git commit -m "Aanbeveling boven de tabel gezet"',
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

    p.accordeon(
        'Had het ook met GitHub Pages gekund?',
        '<p>Ja, en het is de moeite waard om te weten wanneer je wat kiest.</p>',
        [
            {'title': 'GitHub Pages',
             'body': '<p>Gratis, en je hebt er geen tweede account voor nodig. Zet je '
                     'bestanden in een map <code>docs</code>, en zet in de instellingen '
                     'van je repository Pages aan op de branch main en die map. Klaar. '
                     'Je adres wordt <code>jouwnaam.github.io/projectnaam</code>.</p>'
                     '<p>De beperking: het serveert alleen bestanden. Geen database, '
                     'geen formulier dat iets bewaart. En de repository moet openbaar '
                     'zijn, tenzij je een betaald plan hebt.</p>'},
            {'title': 'Firebase Hosting',
             'body': '<p>Ook gratis, iets meer opzetwerk, maar je zit meteen naast '
                     'Firestore. Dat is de reden dat we het hier gebruiken: in het '
                     'volgende hoofdstuk gaan we gegevens opslaan, en dan heb je een '
                     'backend nodig.</p>'
                     '<p>Bouw je alleen een pagina zonder formulier, dan is GitHub '
                     'Pages sneller. Weet je nu al dat er iets bewaard moet worden, '
                     'begin dan meteen hier.</p>'},
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
