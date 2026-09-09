# -*- coding: utf-8 -*-
"""Wie de cursus is en welke pagina's erin zitten, in deze volgorde.

Deze cursus sluit aan op hulpmiddel 15 "AI naar website" uit de
studentenhandleiding van de minor Circulaire Economie. Dat hulpmiddel brengt je
tot één werkend HTML-bestand op je eigen laptop. Hier gaat het verder: in
versiebeheer, online, en met een database eronder.

Bewust binnen het gratis Spark-plan van Firebase gehouden. Cloud Storage zit er
daarom niet in: dat vraagt sinds februari 2026 een gekoppelde betaalmethode.
"""

ID = 'ai-naar-website'
TITEL = 'AI naar website'
ONDERTITEL = 'Van één HTML-bestand naar een gepubliceerde site met een backend'
OMSCHRIJVING = 'Minor Circulaire Economie'
INLEIDING = ('Hulpmiddel 15 brengt je tot een werkende pagina op je eigen laptop. '
             'Deze cursus brengt hem online, met versiegeschiedenis en met een '
             'database eronder die antwoorden van bezoekers bewaart. Je laat Claude '
             'Code of Codex het meeste werk doen en leert precies welke drie '
             'stappen je zelf moet zetten. Alles gratis en zonder betaalgegevens.')

# (bestandsnaam zonder .py, titel, samenvatting voor het menu, geschatte tijd)
PAGINAS = [
    ('h01_waarom', 'Waar hulpmiddel 15 ophoudt',
     'Wat een los HTML-bestand niet kan, wat je hier gaat bouwen, en welke drie '
     'stappen de AI niet voor je mag doen.', '15 min'),
    ('h02_accounts', 'Twee accounts aanmaken',
     'GitHub en Firebase, met je eigen account en niet met dat van school — en '
     'waarom je van het Blaze-plan afblijft.', '15 min'),
    ('h03_installeren', 'Git, Node en de twee CLI’s',
     'Wat elk onderdeel doet, en de prompt waarmee je het allemaal laat '
     'installeren.', '15 min'),
    ('h04_inloggen', 'Koppelen: de drie inlogmomenten',
     'gh auth login, firebase login en je projectkeuze. Hier tikt de AI mee, maar '
     'log jij in.', '15 min'),
    ('h05_repo', 'Je pagina in een repository',
     'Van een map op je bureaublad naar versiegeschiedenis op GitHub, en wat er '
     'juist níet in mag.', '15 min'),
    ('h06_publiceren', 'Publiceren op een echt adres',
     'Firebase Hosting in vier commando’s, de bijwerklus, en hoe je terugdraait '
     'als het misgaat.', '15 min'),
    ('h07_backend', 'De backend: antwoorden bewaren',
     'Een reactieformulier dat in Firestore terechtkomt, met beveiligingsregels '
     'die dichtzitten in plaats van open.', '20 min'),
    ('h08_afronden', 'Controleren en opleveren',
     'Kennischeck, de controlelijst voor je het aan je opdrachtgever laat zien, en '
     'wat je achteraf opruimt.', '15 min'),
]
