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


toki_ni_imp = [328, 2242, 11430, 12551, 4012, 703, 1594, 6479, 1703, 77, 57, 54, 54, 255, 96, 109, 168, 283, 352, 400, 3736]
toki_ni_words = [Word('wan'), Word('meni'), Word('pi'), Word('aj'), Word('ju'), Word('pik'), Word('smal'), Word('kut'), Word('pat'), Word('let'), Word('jelo'), Word('klin'), Word('plu'), Word('plak'), Word('wajt'), Word('kala'), Word('mani'), Word('plant'), Word('animal'), Word('lajp'), Word('pok')]



#vocab = Vocabulary(words=nimi_pu_list)
#print(vocab)
#vocab = Vocabulary(count=120)
vocab = Vocabulary(words=toki_ni_words, importances=toki_ni_imp)
#vocab = Vocabulary(words=nimi_pu_words)
r = 0
while True:
    if r % 1000 == 0:
        print('\n')
        print(f'r = {r}, cost = {vocab.cost():.3f}')
        #vocab.print_costs()
        print(vocab)
    vocab.alter_if_better()
    r += 1