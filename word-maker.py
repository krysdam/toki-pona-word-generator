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


toki_ni_freq = [328, 2242, 11430, 12551, 4012, 703, 1594, 6479, 1703, 77, 57, 54, 54, 255, 96, 109, 168, 283, 352, 400, 3736]
toki_ni_words = [Word('wan'), Word('meni'), Word('pi'), Word('aj'), Word('ju'), Word('pik'), Word('smal'), Word('kut'), Word('pat'), Word('let'), Word('jelo'), Word('klin'), Word('plu'), Word('plak'), Word('wajt'), Word('kala'), Word('mani'), Word('plant'), Word('animal'), Word('lajp'), Word('pok')]

nimi_pu_freq = [12551, 11430, 8785, 6617, 6479, 5753, 5231, 4715, 4430, 4012, 3907, 3736, 3480, 2976, 2949, 2757, 2741, 2434, 2242, 2140, 2063, 2041, 2001, 1971, 1790, 1703, 1594, 1476, 1472, 1389, 1361, 1306, 1104, 975, 930, 912, 835, 828, 826, 820, 805, 734, 733, 729, 722, 703, 684, 665, 660, 646, 635, 566, 549, 528, 514, 501, 492, 482, 477, 448, 419, 416, 366, 356, 355, 352, 352, 341, 329, 328, 306, 296, 286, 283, 281, 270, 268, 260, 255, 252, 249, 223, 215, 214, 211, 209, 192, 188, 185, 185, 183, 178, 172, 168, 158, 145, 142, 129, 119, 110, 109, 101, 100, 96, 94, 94, 88, 84, 78, 77, 75, 71, 66, 65, 64, 58, 57, 54, 53, 32]
nimi_pu_words = [Word('aj'), Word('pi'), Word(''), Word('tak'), Word('kut'), Word('tis'), Word('a'), Word(''), Word('nat'), Word('ju'), Word('at'), Word('pok'), Word('tu'), Word('ap'), Word('no'), Word('tajm'), Word('tej'), Word('want'), Word('meni'), Word('pat'), Word('o'), Word('kama'), Word('ken'), Word('pil'), Word('nejm'), Word('pat'), Word('smal'), Word('pikas'), Word('aws'), Word('wak'), Word('lant'), Word('imas'), Word('jus'), Word('pan'), Word('ap'), Word('put'), Word('luk'), Word('lajk'), Word('wata'), Word('slip'), Word('wat'), Word('tul'), Word('al'), Word('ent'), Word('diprent'), Word('pik'), Word('tin'), Word('ol'), Word('stlejns'), Word('kulupu'), Word('san'), Word('kip'), Word('sawnt'), Word('puk'), Word('tu'), Word('wej'), Word('nu'), Word('plejk'), Word('en'), Word('pawa'), Word('lap'), Word('et'), Word('stej'), Word('aj'), Word('at'), Word('ejl'), Word('animal'), Word('lip'), Word('mu'), Word('wan'), Word('kolt'), Word('sakl'), Word('nanpal'), Word('plant'), Word('taj'), Word('il'), Word('swit'), Word('pajt'), Word('plak'), Word('palent'), Word('pati'), Word('klejn'), Word('ant'), Word('mawt'), Word('open'), Word('semisalit'), Word('jaki'), Word('pis'), Word('pu'), Word('insajt'), Word('tlejt'), Word('plut'), Word('sajt'), Word('mani'), Word('klot'), Word('lajn'), Word('waman'), Word('alt'), Word('kantejna'), Word('sapas'), Word('kala'), Word('man'), Word('pat'), Word('wajt'), Word('pak'), Word('stik'), Word('anta'), Word('pat'), Word('leptajl'), Word('let'), Word('mun'), Word('il'), Word('seks'), Word('pejs'), Word('skin'), Word('piajnt'), Word('jelo'), Word('plu'), Word('ant'), Word('ol')]


#vocab = Vocabulary(words=nimi_pu_list)
#print(vocab)
#vocab = Vocabulary(count=120)
#vocab = Vocabulary(words=toki_ni_words, importances=toki_ni_imp)
vocab = Vocabulary(words=nimi_pu_words, importances=nimi_pu_freq)
r = 0
while True:
    if r % 1000 == 0:
        print('\n')
        print(f'r = {r}, cost = {vocab.cost():.3f}')
        #vocab.print_costs()
        print(vocab)
    vocab.alter_if_better()
    r += 1