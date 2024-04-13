from constants import *
from utils import *

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

"""
dissimilarities = []
for w1, w2 in combinations(nimi_pu_list, 2):
    dissimilarity = string_dissimilarity(w1, w2)
    if dissimilarity < 1.00:
        dissimilarities.append((w1, w2, dissimilarity))
dissimilarities.sort(key=lambda x: x[2])
for w1, w2, d in dissimilarities:
    print(f'{w1} - {w2} = {d:.3f} = {(1/d/d - 1)/5}')
    """
        

#vocab = Vocabulary(words=nimi_pu_list)
#print(vocab)
vocab = Vocabulary(count=120)
r = 0
while True:
    if r % 100 == 0:
        print('\n')
        print(f'r = {r}, cost = {vocab.cost():.3f}')
        print(vocab)
    vocab.alter_if_better()
    r += 1