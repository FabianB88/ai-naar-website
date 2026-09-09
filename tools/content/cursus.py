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
             'database eronder die antwoorden van bezoekers bewaart. Claude Code of '
             'Codex doet vrijwel alles; er zijn precies vier momenten waarop jij aan '
             'de beurt bent. Alles gratis en zonder betaalgegevens.')

# (bestandsnaam zonder .py, titel, samenvatting voor het menu, geschatte tijd)
PAGINAS = [
    ('h01_waarom', 'Waar hulpmiddel 15 ophoudt',
     'Wat een los HTML-bestand niet kan, wat je hier gaat bouwen, en de vier '
     'momenten waarop jij aan de beurt bent.', '15 min'),
    ('h02_accounts', 'Twee accounts aanmaken',
     'De enige twee dingen die je met de hand doet, en waarom je van het '
     'Blaze-plan afblijft.', '10 min'),
    ('h03_installeren', 'Git, Node en de twee CLI’s',
     'Wat elk onderdeel doet, en de prompt waarmee je het allemaal laat '
     'installeren.', '15 min'),
    ('h04_inloggen', 'Koppelen, en dan neemt de AI het over',
     'De twee inlogstappen die je zelf moet doen — en daarna je Firebase-project '
     'via één prompt.', '15 min'),
    ('h05_repo', 'Je pagina in een repository',
     'Van een map op je bureaublad naar versiegeschiedenis op GitHub, en wat er '
     'juist níet in mag.', '15 min'),
    ('h06_publiceren', 'Publiceren op een echt adres',
     'Hosting via één prompt, de bijwerklus, en de vier plekken waar je het neer '
     'kunt zetten.', '15 min'),
    ('h07_backend', 'De backend: antwoorden bewaren',
     'Database, regels en formulier via prompts — en waarom je die regels wél zelf '
     'moet lezen.', '20 min'),
    ('h08_afronden', 'Controleren en opleveren',
     'Kennischeck, de controlelijst voor je het aan je opdrachtgever laat zien, en '
     'wat je achteraf opruimt.', '15 min'),
]
