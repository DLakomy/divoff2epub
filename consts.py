# -*- coding: utf-8 -*-

import re

DIVOFF_DIR = '/Users/mmolenda/prv/divinum-officium/web/www/missa/Polski/'

EXCLUDE_SECTIONS = (
    'Evangelium1',
    'Evangelium2',
    'Evangelium3',
    'Evangelium4',
    'Lectio1',
    'Prelude(rubrica 1570)',
    'Rank1570',
    'Rank1960',
    'RankNewcal',
    'RankTrident',
    'Rank',
    'Rank (rubrica 1955 aut rubrica 1960)',
    'Rank (rubrica 1960)',
    'Rank (rubrica innovata)',
    'Rank (si rubrica 1960)',
    'Rank (si rubrica innovata)',
    'Rule',
    'Tractus1',
    'Munda Cor Passionis',
    'GradualeF'
)
EXCLUDE_SECTIONS_TITLES = (
    'Commemoratio Oratio',
    'Commemoratio Postcommunio',
    'Commemoratio Secreta',
    'Comment',
    'Prelude',
    'Prelude(rubrica 1960)',
    'Maundi',
    'Post Missam'
)


TRANSLATION = {
'Communicantes': 'Communicantes',
'CommunioP': 'Antyfona na Komunię (Okres Wielkanocny)',
'Communio': 'Antyfona na Komunię',
'Evangelium': 'Ewangelia',
'GradualeP': 'Alleluja Wielkanocne',
'Graduale': 'Graduał',
'Introitus': 'Introit',
'Lectio': 'Lekcja',
'OffertoriumP': 'Antyfona na Ofiarowanie (Okres Wielkanocny)',
'Offertorium': 'Antyfona na Ofiarowanie',
'Oratio': 'Kolekta',
'Postcommunio': 'Pokomunia',
'Secreta': 'Sekreta',
'Sequentia': 'Sekwencja',
'Super populum': 'Modlitwa nad ludem',
'Prefatio': 'Prefacja',
'Tractus': 'Traktus'}

TRANSLATION_MULTI = {
'GradualeL1': '1 Graduał',
'GradualeL2': '2 Graduał',
'GradualeL3': '3 Graduał',
'GradualeL4': '4 Graduał',
'GradualeL5': '5 Graduał',
'Graduale': '6 Graduał',
'LectioL1': '1 Lekcja',
'LectioL2': '2 Lekcja',
'LectioL3': '3 Lekcja',
'LectioL4': '4 Lekcja',
'LectioL5': '5 Lekcja',
'Lectio': '6 Lekcja',
'OratioL1': '2 Kolekta',
'OratioL2': '3 Kolekta',
'OratioL3': '4 Kolekta',
'OratioL4': '5 Kolekta',
'OratioL5': '6 Kolekta',
'Oratio': '1 Kolekta'}

PATERNOSTER = "Ojcze nasz, któryś jest w niebie: Święć się Imię Twoje, Przyjdź królestwo Twoje, Bądź wola Twoja jako w niebie tak i na ziemi.\nChleba naszego powszedniego daj nam dzisiaj I odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom. I nie wódź nas na pokuszenie. Ale nas zbaw ode złego. Amen."

REF_REGEX = re.compile('^@(.*):(.*)')
SECTION_REGEX = re.compile(r'^### *(.*)')

TRANSFORMATIONS = (
    (re.compile(r'\+\+'), '☩'),
    (re.compile(r'\+'), '☩'),
    (re.compile(r'^#'), '##'),
    (re.compile(r'^!x!'), '!'),
    (re.compile(r'^!! *(.*)'), '### \\1'),
    (re.compile(r'^\[([^\]]*)\]'), '### \\1'),
    (re.compile(r'^! *(.*)'), '*\\1*'),
    (re.compile(r'^v\. *'), ''),
    (re.compile(r'^_'), ''),
    (re.compile(r'\(\('), '('),
    (re.compile(r'\)\)'), ')'),
    (re.compile(r'\['), '('),
    (re.compile(r'\]'), ')'),
    (re.compile(r'^.*`.*$'), ''),
    (re.compile(r'^[&$]Gloria.*'), 'Chwała Ojcu.'),
    (re.compile(r'^\$Per Dominum.*'), 'Przez Pana.'),
    (re.compile(r'^\$Per eu[mn]dem.*'), 'Przez tegoż Pana.'),
    (re.compile(r'^\$Qui tecum.*'), 'Który z Tobą.'),
    (re.compile(r'^\$Qui vivis.*'), 'Który żyjesz.'),
    (re.compile(r'^\$Deo [Gg]ratias.*'), 'Bogu dzięki.'),
    (re.compile(r'^[&$]Dominus *[Vv]obiscum.*'), 'V. Pan z wami.\nR. I z duchem twoim.'),
    (re.compile(r'^\*Modlitwa nad ludem\*.*'), ''),
    (re.compile(r'^\$Pater noster.*'), PATERNOSTER),
    (re.compile(r'\(rubrica 1955 aut rubrica 1960 dicitur\)'), ''),
    (re.compile(r'\(deinde dicuntur semper\)'), ''),
)

PROPERS_INPUT = (
('Okres Męki', ),
('Tempora/Quad6-5r.txt', 'Quad5', None), # Triduum
)

PROPERS_INPUT1 = (
('Stałe Części Mszy Świętej', ),
('Ordo/Asperges.txt', 'Communis', None),
('Ordo/Incipit.txt', 'Communis', None),
('Ordo/Verbo.txt', 'Communis', None),
('Ordo/Offertorium.txt', 'Communis', None),
('Ordo/Canon.txt', 'Communis', None),
('Ordo/Communio.txt', 'Communis', None),
('Ordo/Conclusio.txt', 'Communis', None),

('Adwent', ),
('Tempora/Adv1-0.txt', 'Trinitate', None),
('Tempora/Adv2-0.txt', 'Trinitate', None),
('Tempora/Adv3-0.txt', 'Trinitate', None),
('Tempora/Adv3-3.txt', 'Communis', None),
('Tempora/Adv3-5.txt', 'Communis', None),
('Tempora/Adv3-6.txt', 'Communis', None),
('Tempora/Adv4-0.txt', 'Trinitate', None),
('Sancti/12-24.txt', 'Trinitate', None),

('Okres Bożego Narodzenia', ),
('Sancti/12-25m1.txt', 'Nat', 'C-Nat1962'),
('Sancti/12-25m2.txt', 'Nat', 'C-Nat1962'),
('Sancti/12-25m3.txt', 'Nat', 'C-Nat1962'),
('Tempora/Nat1-0.txt', 'Nat', 'C-Nat1962'),
('Sancti/12-26.txt', 'Nat', 'C-Nat1962'),
('Sancti/12-27.txt', 'Nat', 'C-Nat1962'),
('Sancti/12-28.txt', 'Nat', 'C-Nat1962'),
('Sancti/01-01.txt', 'Nat', 'C-Nat1962'),
('Sancti/01-03n.txt', 'Nat', None),
('Sancti/01-06.txt', 'Epi', 'C-Epi1962'),
('Tempora/Epi1-0.txt', 'Epi', None),
('Sancti/01-13.txt', 'Epi', None),

('Okres po Objawieniu', ),
('Tempora/Epi2-0.txt', 'Trinitate', None),
('Tempora/Epi3-0.txt', 'Trinitate', None),
('Tempora/Epi4-0.txt', 'Trinitate', None),
('Tempora/Epi5-0.txt', 'Trinitate', None),
('Tempora/Epi6-0.txt', 'Trinitate', None),

('Przedpoście', ),
('Tempora/Quadp1-0.txt', 'Trinitate', None),
('Tempora/Quadp2-0.txt', 'Trinitate', None),
('Tempora/Quadp3-0.txt', 'Trinitate', None),

('Wielki Post', ),
('Tempora/Quadp3-3.txt', 'Quad', None),
('Tempora/Quad1-0.txt', 'Quad', None),
('Tempora/Quad1-3.txt', 'Quad', None),
('Tempora/Quad1-5.txt', 'Quad', None),
('Tempora/Quad1-6.txt', 'Quad', None),
('Tempora/Quad2-0.txt', 'Quad', None),
('Tempora/Quad3-0.txt', 'Quad', None),
('Tempora/Quad4-0.txt', 'Quad', None),

('Okres Męki Pańskiej', ),
('Tempora/Quad5-0.txt', 'Quad5', None),
('Tempora/Quad6-0r.txt', 'Quad5', None),
('Tempora/Quad6-1.txt', 'Quad5', None),
('Tempora/Quad6-2.txt', 'Quad5', None),
('Tempora/Quad6-3.txt', 'Quad5', None),
('Tempora/Quad6-4r.txt', 'Quad5', None),  # Triduum
('Tempora/Quad6-5r.txt', 'Communis', None), # Triduum

('Okres Wielkanocny', ),
('Tempora/Quad6-6r.txt', 'Communis', None), # Triduum
('Tempora/Pasc0-0.txt', 'Pasch', 'C-Pasc1962'),
('Tempora/Pasc0-1.txt', 'Pasch', 'C-Pasc1962'),
('Tempora/Pasc0-2.txt', 'Pasch', 'C-Pasc1962'),
('Tempora/Pasc0-3.txt', 'Pasch', 'C-Pasc1962'),
('Tempora/Pasc0-4.txt', 'Pasch', 'C-Pasc1962'),
('Tempora/Pasc0-5.txt', 'Pasch', 'C-Pasc1962'),
('Tempora/Pasc0-6.txt', 'Pasch', 'C-Pasc1962'),
('Tempora/Pasc1-0.txt', 'Pasch', None),
('Tempora/Pasc2-0.txt', 'Pasch', None),
('Tempora/Pasc3-0r.txt', 'Pasch', None),
('Tempora/Pasc4-0.txt', 'Pasch', None),
('Tempora/Pasc5-0.txt', 'Pasch', None),
('Tempora/Pasc5-3.txt', 'Pasch', None),
('Tempora/Pasc5-4.txt', 'Asc', 'C-Asc1962'),
('Tempora/Pasc6-0.txt', 'Asc', None),
('Tempora/Pasc6-6.txt', 'Spiritu', 'C-Pent1962'),
('Tempora/Pasc7-0.txt', 'Spiritu', 'C-Pent1962'),
('Tempora/Pasc7-1.txt', 'Spiritu', 'C-Pent1962'),
('Tempora/Pasc7-2.txt', 'Spiritu', 'C-Pent1962'),
('Tempora/Pasc7-3.txt', 'Spiritu', 'C-Pent1962'),
('Tempora/Pasc7-4.txt', 'Spiritu', 'C-Pent1962'),
('Tempora/Pasc7-5.txt', 'Spiritu', 'C-Pent1962'),
('Tempora/Pasc7-6.txt', 'Spiritu', 'C-Pent1962'),

('Okres po Zesłaniu Ducha Świetego', ),
('Tempora/Pent01-0r.txt', 'Trinitate', None),
('Tempora/Pent01-4.txt', 'Nat', None),
('Tempora/Pent02-0r.txt', 'Trinitate', None),
('Tempora/Pent02-5.txt', 'Cord', None),
('Tempora/Pent03-0r.txt', 'Trinitate', None),
('Tempora/Pent04-0.txt', 'Trinitate', None),
('Tempora/Pent05-0.txt', 'Trinitate', None),
('Tempora/Pent06-0.txt', 'Trinitate', None),
('Tempora/Pent07-0.txt', 'Trinitate', None),
('Tempora/Pent08-0.txt', 'Trinitate', None),
('Tempora/Pent09-0.txt', 'Trinitate', None),
('Tempora/Pent10-0.txt', 'Trinitate', None),
('Tempora/Pent11-0.txt', 'Trinitate', None),
('Tempora/Pent12-0.txt', 'Trinitate', None),
('Tempora/Pent13-0.txt', 'Trinitate', None),
('Tempora/Pent14-0.txt', 'Trinitate', None),
('Tempora/Pent15-0.txt', 'Trinitate', None),
('Tempora/Pent16-0.txt', 'Trinitate', None),
('Tempora/093-3.txt', 'Communis', None),
('Tempora/093-5.txt', 'Communis', None),
('Tempora/093-6.txt', 'Communis', None),
('Tempora/Pent17-0.txt', 'Trinitate', None),
('Tempora/Pent18-0.txt', 'Trinitate', None),
('Tempora/Pent19-0.txt', 'Trinitate', None),
('Tempora/Pent20-0.txt', 'Trinitate', None),
('Tempora/Pent21-0.txt', 'Trinitate', None),
('Tempora/Pent22-0.txt', 'Trinitate', None),
('Sancti/10-DUr.txt', 'Regis', None),
('Tempora/Pent23-0.txt', 'Trinitate', None),
('Tempora/Pent24-0.txt', 'Trinitate', None),

('Msze Własne o Świętych', ),
('Sancti/12-08.txt', 'Maria', None),
('Sancti/12-21.txt', 'Apostolis', None),
('Sancti/02-02.txt', 'Communis', None),
('Sancti/02-22.txt', 'Apostolis', None),
('Sancti/02-24.txt', 'Apostolis', None),
('Sancti/03-19.txt', 'Joseph', None),
('Sancti/03-25.txt', 'Maria', None),
('Sancti/04-23pl.txt', 'Communis', None),
('Sancti/04-25.txt', 'Apostolis', None),
('Sancti/05-01r.txt', 'Joseph', None),
('Sancti/05-03pl.txt', 'Maria', None),
('Sancti/05-08pl.txt', 'Communis', None),
('Sancti/05-11r.txt', 'Apostolis', None),
('Sancti/05-24pl.txt', 'Maria', None),
('Sancti/05-31.txt', 'Maria', None),
('Sancti/06-23.txt', 'Communis', None),
('Sancti/06-24.txt', 'Communis', None),
('Sancti/06-28r.txt', 'Communis', None),
('Sancti/06-29.txt', 'Apostolis', None),
('Sancti/07-01.txt', 'Quad5', None),
('Sancti/07-02.txt', 'Maria', None),
('Sancti/07-25.txt', 'Apostolis', None),
('Sancti/07-26.txt', 'Communis', None),
('Sancti/08-06.txt', 'Communis', None),
('Sancti/08-10.txt', 'Communis', None),
('Sancti/08-14.txt', 'Communis', None),
('Sancti/08-15r.txt', 'Maria', None),
('Sancti/08-16.txt', 'Communis', None),
('Sancti/08-22r.txt', 'Maria', None),
('Sancti/08-24.txt', 'Apostolis', None),
('Sancti/08-26pl.txt', 'Maria', None),
('Sancti/09-08.txt', 'Maria', None),
('Sancti/09-14.txt', 'Quad5', None),
('Sancti/09-15.txt', 'Maria', None),
('Sancti/09-21.txt', 'Apostolis', None),
('Sancti/09-29.txt', 'Communis', None),
('Sancti/10-07r.txt', 'Maria', None),
('Sancti/10-11.txt', 'Maria', None),
('Sancti/10-18.txt', 'Apostolis', None),
('Sancti/10-28.txt', 'Apostolis', None),
('Sancti/11-01.txt', 'Communis', None),
('Sancti/11-02m1.txt', 'Defunctorum', None),
('Sancti/11-02m2.txt', 'Defunctorum', None),
('Sancti/11-02m3.txt', 'Defunctorum', None),
('Sancti/11-09.txt', 'Communis', None),
('Sancti/11-13pl.txt', 'Communis', None),
('Sancti/11-30.txt', 'Apostolis', None),
)