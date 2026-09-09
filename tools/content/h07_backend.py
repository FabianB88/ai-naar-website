# -*- coding: utf-8 -*-
"""Een reactieformulier dat in Firestore landt, met dichte beveiligingsregels."""


def bouw(p):
    p.tekst(
        'Waarom je hier een backend voor nodig hebt',
        '<p>Je pagina staat online, maar hij vergeet alles. Zet er een formulier op en '
        'vul dat in, dan gebeurt er niets: er is geen plek waar het antwoord heen '
        'kan.</p>'
        '<p>Daar is een <b>database</b> voor. Bij Firebase heet die <b>Firestore</b>, en '
        'je kunt hem zien als een verzameling laatjes. Elk laatje — een '
        '<i>collection</i> — bevat losse briefjes, en elk briefje is een '
        '<i>document</i> met velden erin. Voor ons project is er één laatje, '
        '<code>meldingen</code>, met per conditiemelding één briefje.</p>'
        '<p>We bouwen het voorbeeld af. Wie de stoel beheert, meldt op de pagina in '
        'welke staat hij is — goed, sleets of kapot — en zet er één zin bij. Dat komt '
        'in Firestore te staan, en jij leest het terug in de console. Zo blijft het '
        'paspoort kloppen zonder dat iemand een bestand hoeft bij te werken.</p>')

    p.aandacht(
        'Dit is het hoofdstuk waar je moet opletten',
        '<p>Alles hiervoor kon hooguit niet werken. Hier kun je iets kapotmaken dat je '
        'niet meteen ziet: een database die openstaat voor de hele wereld.</p>'
        '<p>Firestore vraagt bij het aanmaken of je in <i>testmodus</i> wilt beginnen. '
        'Dat betekent: iedereen mag alles lezen, schrijven en weggooien, dertig dagen '
        'lang, en daarna gaat je site stuk omdat de regels verlopen. Kies het niet, ook '
        'niet "even om te proberen". Het kost je hieronder twee minuten om het meteen '
        'goed te doen.</p>')

    p.tekst(
        'Stappenplan: de database aanmaken',
        '<ol>'
        '<li><b>Ga in de Firebase-console naar <i>Firestore Database</i></b> en klik op '
        '<i>Database maken</i>.</li>'
        '<li><b>Kies een locatie in Europa</b>, bijvoorbeeld <code>eur3</code> of '
        '<code>europe-west4</code>. Je gegevens staan dan binnen de EU, wat je bij '
        'gegevens over mensen sowieso wilt. Let op: de locatie ligt daarna vast en is '
        'niet meer te wijzigen.</li>'
        '<li><b>Kies <i>Beginnen in productiemodus</i></b>, niet testmodus. Alles zit '
        'dan dicht, en dat is precies goed: in de volgende stap zetten we exact één '
        'deurtje open.</li>'
        '<li><b>Registreer je pagina als web-app.</b> Ga naar Projectinstellingen → '
        '<i>Jouw apps</i> → het <code>&lt;/&gt;</code>-icoon, geef hem een naam, en '
        'kopieer het configuratieblok dat je krijgt. Dat heb je zo nodig.</li>'
        '</ol>')

    p.accordeon(
        'Die apiKey in je config is geen wachtwoord',
        '<p>Bijna iedereen struikelt hierover, en sommige AI-assistenten geven hier '
        'verkeerd advies. Lees dit even.</p>',
        [
            {'title': 'Wat er in dat configuratieblok staat',
             'body': '<p>Een <code>apiKey</code>, je project-id en een paar '
                     'adressen. Het ziet eruit als een geheim, en dat is het niet. Het '
                     'is een <b>naamplaatje</b>: het vertelt Firebase welk project je '
                     'bedoelt.</p>'
                     '<p>Deze gegevens horen in je pagina te staan en zijn zichtbaar '
                     'voor iedereen die je site opent. Dat kan niet anders — de '
                     'browser van je bezoeker moet ermee kunnen werken. Google '
                     'documenteert het zelf ook zo.</p>'},
            {'title': 'Waar de beveiliging dan wél zit',
             'body': '<p>In de <b>beveiligingsregels</b>, hieronder. Die staan op de '
                     'server van Firebase, niet in je pagina, en bepalen wat er met je '
                     'gegevens mag gebeuren. Iemand die je apiKey overtypt, kan alleen '
                     'wat jouw regels toestaan.</p>'
                     '<p>Vandaar dat testmodus zo gevaarlijk is: dan staan de regels '
                     'open, en dan is die zichtbare sleutel ineens wél genoeg om je '
                     'database leeg te halen.</p>'},
            {'title': 'Wat wél geheim is',
             'body': '<p>Een <i>service account</i>-bestand — meestal een json met '
                     '<code>private_key</code> erin. Dat geeft volledige toegang en '
                     'omzeilt alle regels. Dat bestand hoort nooit in je pagina en '
                     'nooit in een commit; het staat daarom al in je '
                     '<code>.gitignore</code> uit hoofdstuk 5.</p>'
                     '<p>Voor deze cursus heb je het niet nodig. Stelt je assistent '
                     'voor om er een te downloaden, vraag dan eerst waarom.</p>'},
        ])

    p.tekst(
        'De beveiligingsregels',
        '<p>Dit is het belangrijkste stuk code van de hele cursus. Het zegt: op het '
        'laatje <code>meldingen</code> mag iedereen een briefje léggen, mits het er '
        'precies zo uitziet als afgesproken. Niemand mag briefjes lézen, wijzigen of '
        'weghalen — jij leest ze in de console, en die valt buiten deze regels. En al '
        'het andere in de database zit potdicht.</p>')

    p.commando(
        '',
        '<p>Plak dit in de Firebase-console onder <i>Firestore Database</i> → '
        '<i>Regels</i>, en klik op <i>Publiceren</i>.</p>',
        beide=[
            "rules_version = '2';",
            'service cloud.firestore {',
            '  match /databases/{database}/documents {',
            '',
            '    match /meldingen/{meldingId} {',
            '      // Aanmaken mag, mits het briefje er precies zo uitziet',
            '      allow create: if request.resource.data.keys()',
            "                       .hasOnly(['staat', 'toelichting', 'moment'])",
            '        && request.resource.data.staat is string',
            "        && request.resource.data.staat in ['goed', 'sleets', 'kapot']",
            '        && request.resource.data.toelichting is string',
            '        && request.resource.data.toelichting.size() <= 500',
            '        && request.resource.data.moment == request.time;',
            '',
            '      // Lezen, wijzigen en weggooien: door niemand, via de site',
            '      allow read, update, delete: if false;',
            '    }',
            '',
            '    // De rest van de database zit dicht',
            '    match /{document=**} {',
            '      allow read, write: if false;',
            '    }',
            '  }',
            '}',
        ],
        na='Pas de drie waarden goed, sleets en kapot aan naar jouw eigen opties, en 500 '
           'naar de maximale lengte die je wilt toestaan.')

    p.accordeon(
        'Wat elke regel tegenhoudt',
        '<p>De moeite waard om door te lezen, want dit is het patroon dat je bij elk '
        'volgend formulier hergebruikt.</p>',
        [
            {'title': 'hasOnly — geen extra velden',
             'body': '<p>Zonder deze regel kan iemand een document aanmaken met '
                     'honderd velden erin, of met een veld waarin een hele tekst '
                     'staat. Nu mogen er exact drie velden in, en niets anders.</p>'},
            {'title': 'in en size() — geen onzin en geen romans',
             'body': '<p>De gemelde staat moet een van jouw drie waarden zijn, en de '
                     'toelichting mag '
                     'niet langer dan 500 tekens. Daarmee sluit je af dat iemand je '
                     'database volpompt met tekst tot je gratis ruimte op is.</p>'},
            {'title': 'moment == request.time — geen verzonnen tijdstip',
             'body': '<p>De tijd wordt door de server gezet, niet door de browser van '
                     'de bezoeker. Je weet dus zeker wanneer een reactie echt binnenkwam '
                     'en niet wat iemand beweert. In je pagina gebruik je daarvoor '
                     '<code>serverTimestamp()</code>.</p>'},
            {'title': 'allow read: if false — niemand leest mee',
             'body': '<p>Dit is de regel die je beschermt tegen het vervelendste '
                     'scenario: bezoeker A die de antwoorden van bezoeker B kan '
                     'opvragen. Jouw pagina hoeft ze niet te tonen, dus mag niemand ze '
                     'ophalen.</p>'
                     '<p>Wil je later toch een overzicht op de site, dan is dat een '
                     'ander gesprek — en dan komt Authentication erbij.</p>'},
        ])

    p.tekst(
        'Het formulier laten bouwen',
        '<p>Nu de regels staan, mag je assistent de code schrijven. Geef hem deze '
        'opdracht, en plak je eigen configuratieblok uit de console eronder.</p>')

    p.commando(
        '',
        '',
        beide=[
            'Voeg aan public/index.html onderaan een conditiemelding-formulier toe met:',
            '- een keuze uit drie waarden: goed, sleets of kapot',
            '- een tekstveld voor een toelichting, maximaal 500 tekens',
            '- een verzendknop, en een bevestiging na verzenden',
            '',
            'Sla het op in Firestore in de collection "meldingen", met precies de',
            'velden staat, toelichting en moment. Gebruik serverTimestamp() voor',
            'moment. Gebruik de modulaire web-SDK via de gstatic-CDN.',
            '',
            'Vraag geen naam, geen e-mailadres en geen andere persoonsgegevens.',
            'Zet mijn firebaseConfig erin zoals hieronder. Lees niets terug uit',
            'de database: de regels staan alleen aanmaken toe.',
            '',
            '<hier plak je je eigen firebaseConfig uit de console>',
        ],
        na='De laatste twee alinea’s zijn de belangrijkste. Zonder die instructies '
           'bouwt een assistent al snel een naamveld en een overzichtslijst erbij, en '
           'dan botst je pagina op je eigen regels — of erger, dan vraag je '
           'persoonsgegevens die je niet nodig hebt.')

    p.commando(
        'Waar je op let in de code die je terugkrijgt',
        '<p>Je hoeft het niet zelf te kunnen schrijven, wel te herkennen. Bovenaan het '
        'script hoort zoiets te staan.</p>',
        beide=[
            "import { initializeApp } from",
            "  'https://www.gstatic.com/firebasejs/12.18.0/firebase-app.js';",
            "import { getFirestore, collection, addDoc, serverTimestamp } from",
            "  'https://www.gstatic.com/firebasejs/12.18.0/firebase-firestore.js';",
        ],
        na='Het versienummer wisselt; neem dat over uit het snippet dat de console je '
           'geeft. Zie je in plaats hiervan getDocs of onSnapshot staan, dan probeert '
           'je pagina te lézen — dat gaat botsen met je regels, en dat is precies de '
           'bedoeling.')

    p.tekst(
        'Testen, publiceren en teruglezen',
        '<p>Het formulier uit het voorbeeld laat zien hoe het eruit hoort te zien: drie '
        'duidelijke keuzes, één tekstveld met een tekenteller, en een bevestiging na '
        'verzenden. Bouw dat na, en houd het net zo klein.</p>'
        '<p>Publiceer met <code>firebase deploy --only hosting</code>, open je site, en '
        'vul het formulier één keer in. Ga daarna in de console naar <i>Firestore '
        'Database</i> → tabblad <i>Gegevens</i>. Daar hoort je laatje '
        '<code>meldingen</code> te staan, met één briefje erin.</p>'
        '<p>Doe daarna de tegenproef, want een regel die je niet hebt zien werken, weet '
        'je niet zeker. Vraag je assistent om in de browserconsole te proberen de '
        'meldingen op te halen. Dat hoort te mislukken met <i>Missing or insufficient '
        'permissions</i>. Krijg je wél gegevens terug, dan staan je regels nog open — '
        'ga terug naar de vorige stap.</p>')

    p.aandacht(
        'Vraag niets wat je niet nodig hebt',
        '<p>Zodra je een naam of een e-mailadres vraagt, verwerk je persoonsgegevens. '
        'Dan gelden er regels: je moet kunnen uitleggen waarom je ze nodig hebt, wat je '
        'ermee doet en hoelang je ze bewaart. Voor een studieproject is dat zelden de '
        'moeite waard.</p>'
        '<p>Heb je toch een reactie van een specifieke persoon nodig, vraag die dan per '
        'mail in plaats van via een openbaar formulier. En wil je het echt op de '
        'pagina: zet erbij wie je bent, waarvoor je het gebruikt en wanneer je het '
        'weggooit, en overleg het met je opdrachtgever en je docent.</p>')

    p.invulvelden(
        'Oefening: jouw formulier',
        '<p>Bouw het formulier voor je eigen pagina en controleer het daarna.</p>',
        [
            ('h07-collection', 'Hoe heet je collection, en welke velden zitten erin?',
             'Zo min mogelijk velden'),
            ('h07-opties', 'Welke waarden staan er in je regels?',
             'Ze moeten precies matchen met je formulier'),
            ('h07-locatie', 'In welke regio staat je database?',
             'Binnen de EU, en niet meer te wijzigen'),
            ('h07-lezen', 'Wat gebeurde er bij de tegenproef?',
             'Hier hoort "insufficient permissions" te staan'),
            ('h07-persoons', 'Vraag je persoonsgegevens? Zo ja, waarom is dat nodig?',
             'Het beste antwoord is nee'),
            ('h07-bewaren', 'Hoelang bewaar je de meldingen, en wie ruimt ze op?',
             'Zet er een datum bij'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Je hebt nu een werkende toepassing. In het laatste hoofdstuk loop je de '
        'lijst langs voordat je hem laat zien.</p>')

    p.vraag(
        'Even checken',
        'Je assistent zegt: "je apiKey staat in je HTML, dat is onveilig — ik zet hem in '
        'een apart bestand dat we niet committen". Wat klopt hiervan?',
        [
            ('Niets. De apiKey hoort zichtbaar te zijn; hij identificeert je project. '
             'De beveiliging zit in je Firestore-regels.', True),
            ('Klopt, een apiKey is een wachtwoord en hoort nooit in je code.', False),
            ('Klopt half: het mag in je code, maar dan moet de repository privé '
             'blijven.', False),
            ('Klopt, maar alleen als je database persoonsgegevens bevat.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt, en dit is een fout die je vaker zult zien. De '
                       'browser van je bezoeker moet met die sleutel kunnen werken, dus '
                       'verstoppen kán niet eens. Wat je wél verstopt is een service '
                       'account-bestand — dat omzeilt alle regels.</p>'
                       '<p>Ga bij twijfel niet af op wat je assistent zegt, maar kijk '
                       'wat je regels toestaan. Dat is de enige plek waar het echt '
                       'geregeld wordt.</p>',
            '_incorrect': {'final': '<p>Nog niet. De web-apiKey is een naamplaatje, geen '
                                    'wachtwoord: hij zegt welk project je bedoelt. '
                                    'Verstoppen heeft geen zin, want de pagina van je '
                                    'bezoeker heeft hem nodig. Je beveiliging zit in de '
                                    'regels op de server.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
