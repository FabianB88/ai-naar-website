# -*- coding: utf-8 -*-
"""De twee accounts die je nodig hebt, en de valkuilen bij het aanmaken."""


def bouw(p):
    p.tekst(
        'Twee accounts, allebei van jezelf',
        '<p>Je hebt er twee nodig: een <b>GitHub-account</b> voor je code en de '
        'geschiedenis daarvan, en een <b>Google-account</b> waarmee je bij Firebase '
        'kunt voor het publiceren en de database.</p>'
        '<p>Gebruik voor allebei je eigen, persoonlijke account. Niet je '
        'HAN-schoolaccount, en later in je werk niet je zakelijke account. Daar zijn '
        'twee redenen voor. Je schoolaccount vervalt als je klaar bent met de minor, en '
        'daarmee zou je je eigen werk kwijtraken. En op een instellingsaccount rusten '
        'beperkingen die je halverwege tegenkomen op het vervelendste moment: een '
        'geblokkeerde koppeling, een beheerder die toestemming moet geven.</p>'
        '<p>Heb je al een GitHub-account uit een eerder vak, gebruik dat dan gewoon '
        'verder.</p>')

    p.tekst(
        'Stappenplan: GitHub-account aanmaken',
        '<p>Reken op tien minuten, waarvan de helft voor de tweestapsverificatie.</p>'
        '<ol>'
        '<li><b>Ga naar <a href="https://github.com/signup" target="_blank" '
        'rel="noopener">github.com/signup</a></b> en vul je e-mailadres, een wachtwoord '
        'en een gebruikersnaam in.</li>'
        '<li><b>Kies je gebruikersnaam met zorg.</b> Die komt in het adres van alles '
        'wat je publiceert te staan, dus <code>jelle-bakker</code> leest prettiger dan '
        '<code>xX_jelle_2004_Xx</code>. Je kunt hem later wel wijzigen, maar dan breken '
        'je oude links.</li>'
        '<li><b>Bevestig je e-mailadres</b> met de code die je krijgt toegestuurd.</li>'
        '<li><b>Zet tweestapsverificatie aan.</b> GitHub verplicht dit voor iedereen '
        'die code bijdraagt, dus je ontkomt er niet aan. Kies een '
        'authenticator-app — Microsoft Authenticator, Google Authenticator of de '
        'ingebouwde in je wachtwoordmanager.</li>'
        '<li><b>Bewaar je herstelcodes.</b> Je krijgt een lijstje eenmalige codes. Zet '
        'die ergens waar je erbij kunt als je je telefoon kwijt bent — niet alleen op '
        'die telefoon zelf. Zonder herstelcodes en zonder telefoon ben je je account '
        'kwijt, en GitHub kan daar weinig aan doen.</li>'
        '</ol>')

    p.aandacht(
        'Die herstelcodes, echt even doen',
        '<p>Dit is de stap die iedereen overslaat en waar elk jaar iemand op vastloopt: '
        'telefoon stuk of vervangen, geen toegang meer tot het account waar het hele '
        'project in staat, drie weken voor de deadline.</p>'
        '<p>Vijf minuten nu. Print ze, of zet ze in je wachtwoordmanager.</p>')

    p.tekst(
        'En een Google-account voor Firebase',
        '<p>Firebase draait op een Google-account. Heb je er een, dan ben je klaar — een '
        'privé-account, niet je HAN-account. Zo niet, maak er dan een aan op '
        '<a href="https://accounts.google.com/signup" target="_blank" '
        'rel="noopener">accounts.google.com</a>.</p>'
        '<p>Meer hoef je hier niet te doen. Het <b>project</b> zelf maak je niet met de '
        'hand aan in de console: dat doet je assistent straks met één commando, zodra '
        'je in hoofdstuk 4 bent ingelogd. Dat scheelt je een wizard met vragen waar je '
        'toch moet gokken, en je houdt de naam en de instellingen in je eigen '
        'aantekeningen in plaats van in een browsertabblad.</p>')

    p.aandacht(
        'Dit zijn de enige twee dingen die je met de hand doet',
        '<p>Accounts aanmaken kan een assistent niet voor je doen, en dat hoort ook niet: '
        'er komt een e-mailbevestiging aan te pas, een CAPTCHA, en een code op je '
        'telefoon. Alles wat daarná komt — projecten, databases, instellingen, '
        'publiceren — gaat via een prompt.</p>'
        '<p>Kom je later in deze cursus een instructie tegen om ergens in een console te '
        'gaan klikken, dan staat erbij waarom dat niet anders kan. Dat gebeurt precies '
        'twee keer, en allebei alleen om ergens naar te <i>kijken</i>.</p>')

    p.accordeon(
        'Wat je in de console beter laat staan',
        '<p>De Firebase-console laat veel meer zien dan je nodig hebt. Dit zijn de '
        'knoppen waar je vanaf blijft.</p>',
        [
            {'title': 'Upgrade naar Blaze',
             'body': '<p>Het betaalplan. Het vraagt om een gekoppelde betaalmethode, '
                     'en dat hoeft niet: Hosting en Firestore zitten allebei in het '
                     'gratis Spark-plan, ruim boven wat een studieproject '
                     'gebruikt.</p>'
                     '<p>Het gratis plan heeft nog een voordeel dat je niet moet '
                     'onderschatten. Op Spark stopt de dienst als je over de grens '
                     'gaat. Op Blaze loopt hij door en krijg je een rekening. Voor een '
                     'project dat je maar half in de gaten houdt, is stoppen '
                     'veiliger.</p>'},
            {'title': 'Storage',
             'body': '<p>Voor het opslaan van bestanden die bezoekers uploaden. '
                     'Sinds februari 2026 vraagt dit onderdeel een gekoppelde '
                     'betaalmethode, ook binnen de gratis grenzen.</p>'
                     '<p>We gebruiken het daarom niet. Heb je toch afbeeldingen nodig, '
                     'zet die dan gewoon bij je pagina in de repository — dat werkt '
                     'prima en kost niets.</p>'},
            {'title': 'Authentication',
             'body': '<p>Voor pagina’s waar bezoekers moeten inloggen. Dat maakt je '
                     'project meteen een stuk ingewikkelder, en voor een '
                     'reactieformulier heb je het niet nodig.</p>'
                     '<p>Wil je dat later toch, dan is dit het eerste dat je erbij '
                     'zet — maar begin er niet mee.</p>'},
            {'title': 'Alle overige onderdelen',
             'body': '<p>Functions, App Hosting, Data Connect, Remote Config, '
                     'Extensions, en wat er dit jaar bij komt. Stuk voor stuk nuttig '
                     'in een echt product, en stuk voor stuk overbodig hier.</p>'
                     '<p>Vraagt je AI-assistent om er een aan te zetten, vraag dan '
                     'eerst waaróm. Meestal blijkt het antwoord dat het ook zonder '
                     'kan.</p>'},
        ])

    p.invulvelden(
        'Oefening: leg je gegevens vast',
        '<p>Vul dit in zodra je beide accounts hebt. Je hebt deze gegevens de rest van '
        'de cursus nodig, en je zoekt ze anders elke keer opnieuw op.</p>',
        [
            ('h02-github', 'Je GitHub-gebruikersnaam', 'Zoals hij in je adressen komt'),
            ('h02-mail', 'Met welk e-mailadres staat dat account geregistreerd?',
             'Je eigen adres, niet je schooladres'),
            ('h02-2fa', 'Waar staan je GitHub-herstelcodes?',
             'Niet alleen op je telefoon'),
            ('h02-google', 'Met welk Google-account ga je Firebase gebruiken?',
             'Privé, en onthoud welke als je er meerdere hebt'),
            ('h02-naam', 'Hoe wil je je Firebase-project noemen?',
             'Kleine letters en streepjes; je assistent maakt hem in hoofdstuk 4'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Twee accounts, meer niet. In het volgende hoofdstuk laat je je assistent '
        'het gereedschap installeren.</p>')

    p.vraag(
        'Even checken',
        'Waarom gebruik je voor deze accounts je eigen adres en niet je HAN-account?',
        [
            ('Omdat je schoolaccount vervalt als je klaar bent — en omdat er '
             'beperkingen op kunnen zitten die je halverwege blokkeren.', True),
            ('Omdat de HAN het verbiedt om code op GitHub te zetten.', False),
            ('Omdat het met een schoolaccount geld kost.', False),
            ('Dat maakt niet uit; neem gewoon wat het snelst werkt.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. Je bouwt hier iets waar je na de minor nog naar wilt '
                       'kunnen verwijzen, bijvoorbeeld in een sollicitatie. Dat lukt '
                       'niet als het account waarin het staat is opgeheven.</p>',
            '_incorrect': {'final': '<p>Nog niet. Het gaat niet om verboden of om '
                                    'kosten, maar om toegang op de lange termijn: een '
                                    'schoolaccount is tijdelijk, en je werk zou dat '
                                    'niet moeten zijn.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
