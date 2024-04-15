from word import Word
from vocabulary import Vocabulary

nimi_pu_list = [
    'a', 'akesi', 'ala', 'alasa', 'ale', 'anpa', 'ante', 'anu', 'awen',
    'e', 'en', 'esun',
    'ijo', 'ike', 'ilo', 'insa',
    'jaki', 'jan', 'jelo', 'jo',
    'kala', 'kalama', 'kama', 'kasi', 'ken', 'kepeken',
    'kili', 'kiwen', 'ko', 'kon', 'kule', 'kulupu', 'kute',
    'la', 'lape', 'laso', 'lawa', 'len', 'lete', 'li', 'lili', 'linja', 'lipu',
    'loje', 'lon', 'luka', 'lukin', 'lupa', 'ma', 'mama', 'mani', 'meli',
    'mi', 'mije', 'moku', 'moli', 'monsi', 'mu', 'mun', 'musi', 'mute',
    'nanpa', 'nasa', 'nasin', 'nena', 'ni', 'nimi', 'noka',
    'o', 'olin', 'ona', 'open', 'pakala', 'pali', 'palisa', 'pan', 'pana',
    'pi', 'pilin', 'pimeja', 'pini', 'pipi', 'poka', 'poki', 'pona', 'pu',
    'sama', 'seli', 'selo', 'seme', 'sewi',
    'sijelo', 'sike', 'sin', 'sina', 'sinpin', 'sitelen', 'sona', 'soweli',
    'suli', 'suno', 'supa', 'suwi',
    'tan', 'taso', 'tawa', 'telo', 'tenpo', 'toki', 'tomo', 'tu',
    'unpa', 'uta', 'utala', 'walo', 'wan', 'waso', 'wawa', 'weka', 'wile'
    ]


d = 1000

toki_ni_words = [Word( 1041/d, 'wan'),    # wan
                 Word( 5230/d, 'meni'),   # mute
                 Word(21154/d, 'pi'),     # li
                 Word(16893/d, ''),       # e
                 Word(11728/d, 'ai'),     # mi
                 Word( 8202/d, 'ju'),     # sina
                 Word( 1547/d, 'pik'),    # suli
                 Word( 2523/d, 'smal'),   # lili
                 Word( 5046/d, 'kut'),    # pona
                 Word( 2133/d, 'pat'),    # ike
                 Word(  230/d, 'let'),    # loje
                 Word(  140/d, 'jelo'),   # jelo
                 Word(  130/d, 'klin'),   # peta ('green')
                 Word(  130/d, 'plu'),    # laso
                 Word(  604/d, 'plak'),   # pimeja
                 Word(  310/d, 'wait'),   # walo
                 Word(  334/d, 'kala'),   # kule
                 Word(  904/d, 'mani'),   # mani
                 Word(  637/d, 'plant'),  # kasi
                 Word(  983/d, 'animal'), # soweli
                 Word(  500/d, 'laip'),   # konwe ('life')
                 Word(10374/d, 'pok')     # jan
]



#vocab = Vocabulary(words=nimi_pu_list)
#print(vocab)
#vocab = Vocabulary(count=120)
vocab = Vocabulary(words=toki_ni_words)
print(vocab)
r = 0
while True:
    if r % 1000 == 0:
        print('\n')
        print(f'r = {r}, cost = {vocab.cost():.3f}')
        print(vocab)
    vocab.alter_if_better()
    r += 1