import random
from itertools import combinations

from constants import *
from utils import *

from syllable import Syllable
from word import Word


# some word shapes that are useful to keep as constants
SHAPES = [
    # one-syllable words
    Word('o').shape(),
    Word('po').shape(),
    Word('on').shape(),
    Word('pon').shape(),
    # two-syllable words
    Word('opo').shape(),
    Word('opon').shape(),
    Word('popo').shape(),
    Word('popon').shape(),
    Word('onpo').shape(),
    Word('onpon').shape(),
    Word('ponpo').shape(),
    Word('ponpon').shape(),
    # three-syllable words
    # (this is the most common, but there are many others)
    Word('popopo').shape(),
    ]

class Vocabulary:
    """A set of vocabulary terms. Toki Pona's 120 nimi pu is an example."""

    def __init__(self, words:list=None, count:int=120):
        """Create a vocabulary from a list of words. Else, random words."""
        # if words are given, parse them
        if words:
            self.words = [Word(w) for w in words]
        # else, start with a list of random, unique words
        else:
            self.randomize(count = count)
    
    def randomize(self, count:int=120):
        """Randomize the vocabulary."""
        syllable_length = 1
        self.words = []
        failed_attempts = 0
        while len(self.words) < count:
            new_word = Word(syllable_count=syllable_length)
            if new_word not in self.words:
                self.words.append(new_word)
                failed_attempts = 0
            else:
                failed_attempts += 1
                if failed_attempts > 20:
                    syllable_length += 1
                    failed_attempts = 0

    def cost(self):
        """The cost ('badness') of this vocabulary."""
        cost = 0
        # cost of each word alone
        for w1 in self.words:
            cost += w1.inherent_cost()
        # cost of pairs of words
        for w1, w2 in combinations(self.words, 2):
            cost += w1.similarity_cost(w2)
        return cost
    
    def alter_if_better(self):
        """Randomly alter this Vocabulary, if it reduces the cost()."""
        old_cost = self.cost()
        # choose one word, and change it randomly in place
        word_index = random.randrange(0, len(self.words))
        word = self.words[word_index]
        new_word = word.random_variant()
        # if the new word matches an existing word, don't accept the change
        if new_word in self.words:
            return
        # make the change.
        # if the cost gets worse (higher), revert the change.
        self.words[word_index] = new_word
        new_cost = self.cost()
        if new_cost > old_cost:
            self.words[word_index] = word

    def bar_graph(self, function, categories):
        """A string bar graph: how many function(word) are in each category?"""
        # count up each category
        counts = [0] * len(categories)
        for w in self.words:
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
        uncounted = len(self.words) - counted
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
            start_with = [w for w in self.words if w.first_sound() == start]
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
        lengths = [len(w.syllables) for w in self.words]
        max_len = max(lengths)
        s += self.bar_graph(lambda w: len(w.syllables),
                            range(1, max_len+1))
        avg_len = sum(lengths) / len(self.words)
        s += f'average syllables = {avg_len:.1f}\n'
        s += '\n'

        # length in letters
        s += 'LETTERS\n'
        lengths = [len(str(w)) for w in self.words]
        max_len = max(lengths)
        s += self.bar_graph(lambda w: len(str(w)),
                            range(1, max_len+1))
        avg_len = sum(lengths) / len(self.words)
        s += f'average letters = {avg_len:.1f}\n'
        s += '\n'

        s = s.strip()
        return s