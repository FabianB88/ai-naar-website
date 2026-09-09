# -*- coding: utf-8 -*-
"""De drie momenten waarop jij inlogt en de assistent alleen meekijkt."""


def bouw(p):
    p.tekst(
        'Waarom je dit zelf doet',
        '<p>De installatie kon je uitbesteden. Het inloggen niet, en dat is geen '
        'toeval.</p>'
        '<p>Beide inlogcommando’s openen een browser en wachten daar op jou. Ze zijn '
        '<b>interactief</b>: ze stellen vragen en verwachten dat er iemand zit. Een '
        'assistent die zo’n commando in een achtergrondvenster start, krijgt geen '
        'antwoord terug en blijft hangen — je ziet dan een sessie die minutenlang '
        'niets doet.</p>'
        '<p>Praktisch werkt het zo: je assistent zet klaar en legt uit, jij tikt het '
        'inlogcommando in je <b>eigen</b> terminal en maakt het af in de browser. '
        'Daarna kan de assistent weer verder, want vanaf dat moment ligt er een token '
        'op je computer waarmee hij namens jou mag werken.</p>')

    p.aandacht(
        'Er komt nergens een wachtwoord aan te pas',
        '<p>Bij geen van beide routes tik je een wachtwoord in een terminal. GitHub '
        'geeft je een code van acht tekens die je in de browser invult, en Firebase '
        'stuurt je naar de gewone Google-inlogpagina.</p>'
        '<p>Vraagt iets in dit proces om je wachtwoord in een venster dat er anders '
        'uitziet dan je gewend bent, stop dan. Dat hoort niet, ook niet als je '
        'assistent zegt dat het klopt.</p>')

    p.tekst(
        'Moment 0: vertel Git wie je bent',
        '<p>Strikt genomen geen inloggen, maar het moet wel voordat je iets kunt '
        'vastleggen. Git zet bij elke opgeslagen versie een naam en een e-mailadres. '
        'Doe je dit niet, dan weigert je eerste commit met een melding waar je even op '
        'zit te kijken.</p>')

    p.commando(
        '',
        '<p>Vervang de naam en het adres door die van jezelf.</p>',
        beide=[
            'git config --global user.name "Jelle Bakker"',
            'git config --global user.email "1234567+jellebakker@users.noreply.github.com"',
        ],
        na='Dat rare adres is geen typefout: GitHub geeft je een noreply-adres zodat je '
           'echte e-mailadres niet in elke commit belandt. Je vindt het onder Settings '
           '→ Emails, bij "Keep my email addresses private". Gebruik anders gewoon je '
           'eigen adres — het is dan wel openbaar terug te vinden.')

    p.tekst(
        'Moment 1: inloggen bij GitHub',
        '<p>Tik dit in je eigen terminal. Niet in het venster van je assistent.</p>')

    p.commando(
        '',
        '',
        beide='gh auth login',
        na='Daarna volgt een wizard met vier vragen.')

    p.tekst(
        '',
        '<p>De antwoorden die je geeft:</p>'
        '<ol>'
        '<li><b>Where do you use GitHub?</b> → <code>GitHub.com</code></li>'
        '<li><b>What is your preferred protocol?</b> → <code>HTTPS</code>. Dat werkt '
        'zonder dat je sleutels hoeft te maken.</li>'
        '<li><b>Authenticate Git with your GitHub credentials?</b> → <code>Yes</code>. '
        'Hiermee regel je in één keer dat ook <code>git push</code> straks werkt.</li>'
        '<li><b>How would you like to authenticate?</b> → <code>Login with a web '
        'browser</code></li>'
        '</ol>'
        '<p>Dan verschijnt er een <b>eenmalige code</b> van acht tekens, bijvoorbeeld '
        '<code>A1B2-C3D4</code>. Kopieer die, druk op Enter, en je browser opent '
        '<code>github.com/login/device</code>. Plak de code, en geef toestemming.</p>'
        '<p>Dit is het moment waarop je assistent kan helpen: laat hem die pagina '
        'openen terwijl jij de code bij de hand houdt. De code zelf tik jij in.</p>')

    p.commando(
        'Controleren',
        '<p>Terug in je terminal.</p>',
        beide='gh auth status',
        na='Je ziet dan "Logged in to github.com account" met je gebruikersnaam erachter. Staat daar iets '
           'anders, dan ben je in de browser met het verkeerde account ingelogd — dat '
           'gebeurt vaker dan je denkt als je nog een schoolaccount open hebt staan.')

    p.tekst(
        'Moment 2: inloggen bij Firebase',
        '<p>Zelfde idee, andere route: hier opent je browser meteen.</p>')

    p.commando(
        '',
        '',
        beide='firebase login',
        na='Eerst vraagt hij of Firebase gebruiksgegevens van de CLI mag verzamelen. '
           'Je mag daar rustig nee op zeggen; het werkt gewoon.')

    p.tekst(
        '',
        '<p>Daarna opent je browser. Kies je Google-account — hetzelfde als je in '
        'hoofdstuk 2 hebt opgeschreven — en geef de Firebase CLI '
        'toestemming. Je krijgt een pagina te zien dat het gelukt is, en in je terminal '
        'staat dat je bent ingelogd.</p>'
        '<p>Zit je in je browser standaard met een ander Google-account ingelogd, kies '
        'dan bewust. Dit is de tweede plek waar mensen per ongeluk hun schoolaccount '
        'pakken en zich later afvragen waarom hun project onvindbaar is.</p>')

    p.commando(
        'Controleren',
        '<p>Werkt de koppeling?</p>',
        beide='firebase projects:list',
        na='Heb je nog geen projecten, dan is de lijst leeg — dat klopt, die maak je '
           'hieronder aan. Het gaat er hier alleen om dat het commando antwoordt en '
           'niet om een inlogfout vraagt.')

    p.tekst(
        'En nu neemt je assistent het over',
        '<p>Dit was het handwerk. Vanaf hier kan alles via een prompt, want de CLI’s '
        'mogen nu namens jou werken. Het eerste dat je laat doen is je Firebase-project '
        'aanmaken — dat hoeft dus niet in de console.</p>')

    p.commando(
        '',
        '<p>Geef dit aan Claude Code of Codex, met je eigen projectnaam erin.</p>',
        beide=[
            'Maak een Firebase-project aan met de id materialenpaspoort-w3 en',
            'zet het als actief project voor deze map. Controleer daarna dat het',
            'in de lijst staat en laat me de uitvoer zien.',
            '',
            'Zet geen extra diensten aan en koppel geen betaalmethode: we blijven',
            'op het gratis Spark-plan.',
        ],
        na='Krijg je terug dat de id al bezet is, kies dan een andere. Project-id’s zijn '
           'wereldwijd uniek, dus algemene namen zijn meestal al weg.')

    p.commando(
        'Wat hij dan uitvoert',
        '<p>Twee commando’s. De eerste maakt het project, de tweede onthoudt in deze '
        'map welk project erbij hoort.</p>',
        beide=[
            'firebase projects:create materialenpaspoort-w3 --display-name "Materialenpaspoort W3"',
            'firebase use materialenpaspoort-w3',
        ],
        na='De eerste regel is lang; laat hem gerust doorlopen in plaats van hem af te '
           'breken, want Windows en macOS breken regels op verschillende manieren af.')

    p.aandacht(
        'Controleer of je op Spark zit',
        '<p>Dit is het ene moment waarop het de moeite waard is om wél even in de '
        '<a href="https://console.firebase.google.com" target="_blank" '
        'rel="noopener">console</a> te kijken. Open je nieuwe project en zoek linksonder '
        'welk plan er staat. Daar hoort <b>Spark</b> te staan.</p>'
        '<p>Een project dat via de CLI wordt aangemaakt staat standaard op het gratis '
        'plan, dus het hoort goed te zijn. Maar het is de enige instelling in deze '
        'cursus die geld kan kosten als hij verkeerd staat, en dat is dertig seconden '
        'kijken waard.</p>')

    p.accordeon(
        'Wat er nu op je computer staat',
        '<p>Nuttig om te weten, al was het maar om het straks weer weg te '
        'halen.</p>',
        [
            {'title': 'Een token, geen wachtwoord',
             'body': '<p>Allebei de CLI’s hebben nu een toegangssleutel opgeslagen. '
                     'Die geeft toegang tot jouw accounts, maar is niet je wachtwoord: '
                     'je kunt hem intrekken zonder ergens je wachtwoord te '
                     'veranderen.</p>'
                     '<p>Op een gedeelde of ingeleverde computer log je dus uit met '
                     '<code>gh auth logout</code> en <code>firebase logout</code>. '
                     'Doe dat ook aan het eind van je project.</p>'},
            {'title': 'Je assistent mag er nu bij',
             'body': '<p>Vanaf nu kan Claude Code of Codex namens jou een repository '
                     'aanmaken, pushen en publiceren, zonder dat hij je wachtwoord '
                     'kent. Dat is precies de bedoeling.</p>'
                     '<p>Het betekent ook dat je zijn commando’s moet blijven lezen '
                     'voordat je ze goedkeurt. Een <code>git push --force</code> of een '
                     'verwijderde repository is met deze toegang net zo makkelijk als '
                     'een gewone publicatie.</p>'},
            {'title': 'Als je later toegang wilt intrekken',
             'body': '<p>Bij GitHub: Settings → Applications → Authorized OAuth Apps, '
                     'daar staat GitHub CLI tussen. Bij Google: '
                     '<a href="https://myaccount.google.com/permissions" '
                     'target="_blank" rel="noopener">myaccount.google.com/permissions</a>, '
                     'zoek Firebase CLI.</p>'
                     '<p>Handig om te weten als je laptop kwijtraakt: daar zet je de '
                     'toegang uit, niet in je terminal.</p>'},
        ])

    p.invulvelden(
        'Oefening: leg je koppeling vast',
        '<p>Twee regels uitvoer, maar wel de twee die bepalen of de rest van de cursus '
        'werkt.</p>',
        [
            ('h04-gh', 'Wat zegt gh auth status precies?',
             'Welk account staat erbij?'),
            ('h04-fb', 'Welke projecten geeft firebase projects:list terug?',
             'Staat jouw project-id ertussen?'),
            ('h04-account', 'Is dat allebei je eigen account, niet je HAN-account?',
             'Controleer het echt, dit is de klassieke fout'),
            ('h04-project', 'Welke project-id heeft je assistent aangemaakt?',
             'Die komt terug in je webadres'),
            ('h04-plan', 'Staat je project op Spark?',
             'Linksonder in de console; de enige instelling die geld kan kosten'),
            ('h04-uitloggen', 'Wanneer log je weer uit, en op welke computer?',
             'Zeker doen op een gedeelde of geleende laptop'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Werken beide controlecommando’s en staat je project er? Dan is de voorbereiding '
        'klaar. Er komt nog één handeling in de console, in hoofdstuk 7, en verder gaat '
        'alles via prompts.</p>')

    p.vraag(
        'Even checken',
        'Je assistent zegt: "ik voer <code>gh auth login</code> voor je uit". Er gebeurt '
        'daarna een minuut niets. Wat is er aan de hand?',
        [
            ('Het commando wacht op antwoorden die alleen jij kunt geven. Voer het in '
             'je eigen terminal uit en maak het af in de browser.', True),
            ('De GitHub-servers zijn traag; even wachten.', False),
            ('De GitHub CLI is verkeerd geïnstalleerd.', False),
            ('Je internetverbinding is weg.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Het is een interactief commando: het stelt vragen '
                       'en wacht op een mens. In een achtergrondvenster komt dat '
                       'antwoord nooit. Onderbreek het en doe het zelf.</p>',
            '_incorrect': {'final': '<p>Nog niet. Er is niets stuk en het internet doet '
                                    'het prima — het commando wacht gewoon op iemand '
                                    'die de vragen beantwoordt. Dat ben jij.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
