# -*- coding: utf-8 -*-
"""Kennischeck, de controlelijst voor oplevering, en opruimen na afloop."""

TOETS = 'kennischeck-ai-naar-website'
DREMPEL = 75


def bouw(p):
    p.tekst(
        'Kennischeck',
        '<p>Zes vragen over de hele cursus. Het zijn situaties, geen definities: bij '
        'elke vraag moet je kiezen wat je doet.</p>'
        '<p>Je hebt %d%% nodig om te slagen en je mag het zo vaak proberen als je wilt. '
        'Je uitslag verschijnt onderaan zodra je alle vragen hebt ingestuurd.</p>'
        % DREMPEL)

    p.vraag(
        'Vraag 1 — gratis blijven',
        'Je wilt het logo van je opdrachtgever op de pagina zetten. Je assistent stelt '
        'voor om Cloud Storage aan te zetten, en meldt dat daarvoor het Blaze-plan met '
        'een betaalmethode nodig is. Wat doe je?',
        [
            ('Niet doen. Zet de afbeelding gewoon bij je pagina in de map public; dan '
             'heb je Storage niet nodig en blijft alles gratis.', True),
            ('Blaze aanzetten, want binnen de gratis grenzen kost het toch niets.', False),
            ('Je opdrachtgever vragen of hij zijn creditcard wil koppelen.', False),
            ('Het logo weglaten.', False),
        ],
        feedback={
            'title': 'Vraag 1',
            'correct': '<p>Precies. Storage is voor bestanden die bezoekers uploaden. '
                       'Een logo dat jij zelf plaatst, is gewoon een bestand in je '
                       'repository — dat wordt meegepubliceerd en kost niets.</p>',
            '_incorrect': {'final': '<p>Nog niet. Een betaalmethode koppelen voor een '
                                    'studieproject hoeft nooit, en het logo weglaten is '
                                    'te snel opgegeven. Zet de afbeelding bij je pagina '
                                    'in public.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 2 — wat leg je vast',
        'Welk bestand hoort thuis in een commit?',
        [
            ('firebase.json, met de instellingen van je Hosting.', True),
            ('Een serviceAccount.json met een private_key erin.', False),
            ('Een spreadsheet met de contactgegevens van je respondenten.', False),
            ('Een .env-bestand met een sleutel die je nog moet gebruiken.', False),
        ],
        feedback={
            'title': 'Vraag 2',
            'correct': '<p>Klopt. Configuratie zonder geheimen hoort er juist in: dan '
                       'kan iemand anders je project draaien. De andere drie horen in '
                       'je .gitignore, en dat regel je vóór je eerste commit.</p>',
            '_incorrect': {'final': '<p>Nog niet. Alle drie de andere bevatten iets dat '
                                    'geheim of persoonlijk is. Onthoud dat een '
                                    'geschiedenis niet vergeet: weghalen in een latere '
                                    'commit is niet genoeg.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.koppelvraag(
        'Vraag 3 — welk commando doet wat',
        'Koppel elk commando aan wat het doet.',
        rijen=[
            ('git commit', 'Legt een versie vast op je eigen computer'),
            ('git push', 'Stuurt je vastgelegde versies naar GitHub'),
            ('firebase deploy', 'Zet je pagina live op je echte adres'),
            ('firebase hosting:channel:deploy',
             'Maakt een tijdelijk adres om iets voor te leggen'),
        ],
        opties=['Legt een versie vast op je eigen computer',
                'Stuurt je vastgelegde versies naar GitHub',
                'Zet je pagina live op je echte adres',
                'Maakt een tijdelijk adres om iets voor te leggen'],
        feedback={
            'title': 'Vraag 3',
            'correct': '<p>Goed. Merk op dat de eerste twee niets aan je site '
                       'veranderen en de laatste twee niets aan je geschiedenis. Dat is '
                       'de verwarring die je het vaakst zult tegenkomen.</p>',
            '_incorrect': {'final': '<p>Nog niet. Vraag je per commando af: gaat dit '
                                    'over mijn geschiedenis of over wat bezoekers '
                                    'zien?</p>'},
            '_partlyCorrect': {'final': '<p>Deels goed. Kijk nog eens naar de regels die '
                                        'je fout had.</p>'}
        })

    p.vraag(
        'Vraag 4 — testmodus',
        'Bij het aanmaken van je database biedt Firestore aan om in testmodus te '
        'beginnen. Waarom sla je dat over?',
        [
            ('Omdat dan iedereen alles mag lezen, schrijven en weggooien — en omdat de '
             'regels na dertig dagen verlopen, waardoor je site dan stukgaat.', True),
            ('Omdat testmodus geld kost.', False),
            ('Omdat je in testmodus geen gegevens kunt opslaan.', False),
            ('Omdat testmodus alleen op een betaald plan werkt.', False),
        ],
        feedback={
            'title': 'Vraag 4',
            'correct': '<p>Precies, en let op dat tweede deel. Het eerste probleem ziet '
                       'niemand, want alles werkt. Het tweede merk je pas een maand '
                       'later, meestal net als je het aan iemand wilt laten zien.</p>',
            '_incorrect': {'final': '<p>Nog niet. Testmodus is gratis en werkt prima — '
                                    'dat is juist het verraderlijke. Het probleem is dat '
                                    'je database intussen voor iedereen openstaat.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 5 — hoe weet je dat het dichtzit',
        'Je hebt beveiligingsregels gepubliceerd die lezen verbieden. Hoe weet je zeker '
        'dat het werkt?',
        [
            ('Door het te proberen: vraag de meldingen op vanuit de browser en '
             'controleer dat je een permissiefout terugkrijgt.', True),
            ('Doordat de regels zonder foutmelding gepubliceerd zijn.', False),
            ('Doordat je pagina de reacties nergens laat zien.', False),
            ('Doordat je repository op privé staat.', False),
        ],
        feedback={
            'title': 'Vraag 5',
            'correct': '<p>Klopt. Een regel die je niet hebt zien werken, weet je niet '
                       'zeker. De andere drie zeggen alleen iets over jouw pagina, en '
                       'iemand anders hoeft jouw pagina niet te gebruiken om bij je '
                       'database te komen.</p>',
            '_incorrect': {'final': '<p>Nog niet. Dat je site de gegevens niet toont, '
                                    'houdt niemand tegen die zelf een verzoek stuurt. '
                                    'Doe de tegenproef: probeer te lezen en zorg dat het '
                                    'mislukt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 6 — de vraag van je opdrachtgever',
        'Je opdrachtgever vraagt of je op de pagina ook het e-mailadres van reageerders '
        'kunt vragen, "voor als we willen doorvragen". Wat is het beste antwoord?',
        [
            ('Vragen waarvoor het precies nodig is, en of het ook zonder kan — want '
             'zodra je adressen verzamelt, moet je uitleggen wat je ermee doet en '
             'hoelang je ze bewaart.', True),
            ('Gewoon toevoegen; het is zijn project, dus zijn keuze.', False),
            ('Toevoegen, maar het veld optioneel maken.', False),
            ('Weigeren; persoonsgegevens verzamelen mag nooit.', False),
        ],
        feedback={
            'title': 'Vraag 6',
            'correct': '<p>Goed. Het is geen ja of nee maar een gesprek: wat is het '
                       'doel, kan het minder, en wie ruimt het straks op. Vaak blijkt '
                       'doorvragen ook per mail te kunnen, buiten je formulier om.</p>',
            '_incorrect': {'final': '<p>Nog niet. Het is niet verboden, maar het is ook '
                                    'niet vrijblijvend: je moet kunnen uitleggen waarom '
                                    'je het vraagt en wat ermee gebeurt. Optioneel maken '
                                    'verandert daar niets aan.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.tekst(
        'De lijst voor je het laat zien',
        '<p>Hulpmiddel 15 heeft een controlelijst voor de <i>inhoud</i> van je pagina: '
        'kloppen de cijfers, staat er niets verzonnen op, is het leesbaar op een '
        'telefoon. Loop die eerst langs.</p>'
        '<p>Daar komt nu bij wat met publiceren te maken heeft.</p>'
        '<ul>'
        '<li>Je site opent op het adres dat je gaat doorsturen, ook op een telefoon en '
        'ook bij iemand die niet is ingelogd.</li>'
        '<li>Je laatste wijziging staat er echt op: je hebt na je laatste commit ook '
        'gepubliceerd.</li>'
        '<li>Het formulier werkt, en je ziet de reactie in de console terug.</li>'
        '<li>De tegenproef is gedaan: reacties opvragen levert een permissiefout '
        'op.</li>'
        '<li>Er staan geen persoonsgegevens en geen vertrouwelijke cijfers op de '
        'pagina, en die zitten ook niet in je repository.</li>'
        '<li>Je opdrachtgever weet dat de pagina online staat, of hij openbaar is, en '
        'wat er wordt opgeslagen.</li>'
        '<li>Je hebt afgesproken hoelang de site blijft staan en wie hem daarna '
        'weghaalt.</li>'
        '</ul>')

    p.accordeon(
        'Opruimen als het project klaar is',
        '<p>Het laatste stukje beroepshouding: iets dat online staat, is van iemand. '
        'Spreek af van wie, of haal het weg.</p>',
        [
            {'title': 'De site uit de lucht halen',
             'body': '<p><code>firebase hosting:disable</code> zet je adres uit zonder '
                     'iets te verwijderen. Je kunt hem later opnieuw publiceren. Dit is '
                     'de nette manier om een demo af te sluiten.</p>'
                     '<p>Moet alles weg, dan verwijder je het hele project in de '
                     'console onder Projectinstellingen. Dat is definitief, inclusief '
                     'de reacties in je database — dus exporteer eerst wat je nodig '
                     'hebt voor je verslag.</p>'},
            {'title': 'Uitloggen op een computer die niet van jou is',
             'body': '<p><code>gh auth logout</code> en <code>firebase logout</code>. '
                     'Doe dit zeker op een schoollaptop of een geleende computer: '
                     'zolang die tokens er staan, kan iemand anders namens jou '
                     'publiceren.</p>'
                     '<p>Ben je de computer kwijt, trek de toegang dan in bij GitHub '
                     '(Settings → Applications) en Google '
                     '(myaccount.google.com/permissions).</p>'},
            {'title': 'Wat je overdraagt',
             'body': '<p>Blijft de site bestaan na jouw project, dan hoort je '
                     'opdrachtgever te weten waar hij staat, onder welk account, en wat '
                     'er nodig is om hem te wijzigen. Zet dat in je overdracht (zie '
                     'hulpmiddel 18).</p>'
                     '<p>Draag het niet over onder jouw persoonlijke account. Dan '
                     'ligt het bij jou zodra jij niet meer reageert, en dat is voor '
                     'allebei ongemakkelijk.</p>'},
        ])

    p.invulvelden(
        'Van gepubliceerd naar opgeleverd',
        '<p>Vul dit in en kopieer het naar je aantekeningen. Dit is wat je in je '
        'overdracht en je projectpaper nodig hebt.</p>',
        [
            ('h08-url', 'Op welk adres staat je site?', ''),
            ('h08-repo', 'Waar staat je code, en is die repository privé of openbaar?',
             ''),
            ('h08-akkoord', 'Wie heeft akkoord gegeven op publiceren, en wanneer?',
             'Naam en datum'),
            ('h08-opgeslagen', 'Wat wordt er van bezoekers opgeslagen?',
             'In één zin, zoals je het aan je opdrachtgever uitlegt'),
            ('h08-tegenproef', 'Heb je de tegenproef gedaan? Wat kwam eruit?',
             'Permissiefout is goed nieuws'),
            ('h08-tot', 'Tot wanneer blijft de site staan, en wie haalt hem weg?',
             'Met een datum'),
            ('h08-overdracht', 'Wat draag je over, en aan wie?',
             'Adres, account, en hoe je het wijzigt'),
            ('h08-volgende', 'Wat zou je bij een volgend project anders doen?',
             'Eén ding is genoeg'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Kopieer je antwoorden. De eerste zes regels zijn precies wat er in je '
        'overdracht hoort te staan.</p>')


def uitslag(p):
    """Komt in een eigen artikel onder de vragen te staan."""
    p.uitslag(
        TOETS, drempel=DREMPEL,
        voldoende='Voldoende. Je kunt nu een pagina publiceren, bijwerken en '
                  'terugdraaien, en je weet waar de beveiliging van je database echt '
                  'zit. Loop de controlelijst hierboven langs en lever op.',
        onvoldoende='Dat is nog niet voldoende. Kijk terug bij de hoofdstukken van de '
                    'vragen die je fout had — vooral hoofdstuk 7, want daar zit het '
                    'verschil tussen werkt het en is het veilig. Je mag het zo vaak '
                    'proberen als je wilt.')
