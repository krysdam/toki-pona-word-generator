import random
from itertools import combinations

from constants import *
from utils import *

from word import Word
from wordform import Wordform, WORDFORMS


# some word shapes that are useful to keep as constants
SHAPES = [
    # one-syllable words
    Wordform('o').shape(),
    Wordform('po').shape(),
    Wordform('on').shape(),
    Wordform('pon').shape(),
    # two-syllable words
    Wordform('opo').shape(),
    Wordform('opon').shape(),
    Wordform('popo').shape(),
    Wordform('popon').shape(),
    Wordform('onpo').shape(),
    Wordform('onpon').shape(),
    Wordform('ponpo').shape(),
    Wordform('ponpon').shape(),
    # three-syllable words
    # (this is the most common, but there are many others)
    Wordform('popopo').shape(),
    ]

class Vocabulary:
    """A mapping from Words to Wordforms."""

    def __init__(self, words:list=None, count:int=120):
        """Create a vocabulary with given Words and unique Wordforms."""
        if words is None:
            words = [Word(importance=1) for _ in range(count)]
        # assigne wordforms.
        wordforms = WORDFORMS[:len(words)]
        #wordforms = random.sample(WORDFORMS, len(words))
        self.wordforms = dict(zip(words, wordforms))

    def cost(self):
        """The cost ('badness') of this vocabulary."""
        cost = 0
        # cost of each word alone
        for w in self.wordforms:
            wf = self.wordforms[w]
            cost += wf.inherent_cost() * w.importance
            cost += w.source_cost(wf) * w.importance
        # cost of pairs of words
        for (w1, wf1), (w2, wf2) in combinations(self.wordforms.items(), 2):
            cost += wf1.similarity_cost(wf2) * w1.importance * w2.importance
        return cost
    
    def alter_if_better(self):
        """Randomly alter this Vocabulary, if it reduces the cost()."""
        old_cost = self.cost()
        # choose one word, and change it randomly in place
        word, old_wf = random.choice(list(self.wordforms.items()))
        new_wf = random.choice(WORDFORMS)
        # if the new wordform matches an existing wordform,
        # don't accept the change
        if new_wf in self.wordforms.values():
            return
        # make the change.
        self.wordforms[word] = new_wf
        # if the cost gets worse (higher), revert the change.
        new_cost = self.cost()
        if new_cost > old_cost:
            self.wordforms[word] = old_wf

    def bar_graph(self, function, categories):
        """A string bar graph: how many function(word) are in each category?"""
        # count up each category
        counts = [0] * len(categories)
        for w in self.wordforms.values():
            for i, c in enumerate(categories):
                if function(w) == c:
                    counts[i] += 1
        # draw a bar for each category
        s = ''
        for i, c in enumerate(categories):
            s += str(c) + '\t'
            s += 'X' * counts[i]
            s += '\n'
        # report the number of words in no category
        counted = sum(counts)
        uncounted = len(self.wordforms) - counted
        if uncounted:
            s += f'(... and {uncounted} others)\n'
        return s

    def __str__(self):
        s = ''
        # starting sound
        for start in VOWELS + ONSETS:
            if start == '':
                continue
            s += f'{start}\t'
            start_with = [w for w in self.wordforms.values()
                          if w.first_sound() == start]
            start_with.sort()
            s += ' '.join(str(w) for w in start_with)
            s += '\n'
        s += '\n'

         # shapes
        s += 'FIRST SOUND\n'
        s += self.bar_graph(lambda w: w.first_sound(),
                            [start for start in VOWELS + ONSETS
                             if start != ''])
        s += '\n'

        # shapes
        s += 'SHAPES\n'
        s += self.bar_graph(lambda w: w.shape(),
                            SHAPES)
        s += '\n'
                            
        # length in syllables
        s += 'SYLLABLES\n'
        lengths = [len(w.syllables) for w in self.wordforms.values()]
        max_len = max(lengths)
        s += self.bar_graph(lambda w: len(w.syllables),
                            range(1, max_len+1))
        avg_len = sum(lengths) / len(self.wordforms)
        s += f'average syllables = {avg_len:.1f}\n'
        s += '\n'

        # length in letters
        s += 'LETTERS\n'
        lengths = [len(str(w)) for w in self.wordforms.values()]
        max_len = max(lengths)
        s += self.bar_graph(lambda w: len(str(w)),
                            range(1, max_len+1))
        avg_len = sum(lengths) / len(self.wordforms)
        s += f'average letters = {avg_len:.1f}\n'
        s += '\n'

        s = s.strip()
        return s