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

    def costs(self):
        """The 'badness' of this vocabulary, categorized by cost type.

        Longer words are bad.
            For each word, its length is added to the cost.
        Starting with a vowel is slightly bad.
            For each word, if it starts with a vowel,
            0.5 is added to the cost.
            (In other words, initial glottal stop is 0.5 of a consonant.)
        Words that are prefixes of other words are very bad.
            For each pair of words, if one is a prefix of the other,
            4x the length of the prefix is added to the cost.

        Similar words are bad. This is counted in a few ways.
        Edit distance:
            For each pair of words, if their dissimilarity < 1.00,
            (1/dissimilarity) - 1 is added to the cost.
        Word shape:
            For each pair of words, if their shape is the same,
            0.05 is added to the cost.
        First sound:
            For each pair of words, if their first sound is the same,
            0.05 is added to the cost.
        """
        length_cost = 0
        vowel_cost = 0
        prefix_cost = 0
        similarity_cost = 0
        shape_cost = 0
        first_sound_cost = 0

        for w1 in self.words:
            # add the length of each word
            length_cost += len(str(w1))
            # if the word starts with a vowel, add 0.5
            if w1.syllables[0].onset == '':
                vowel_cost += 0.5
        # for each unique pair of words...
        for w1, w2 in combinations(self.words, 2):
            s1, s2 = str(w1), str(w2)
            # if one is a prefix, add 4x the length of the prefix
            if s1.startswith(s2) or s2.startswith(s1):
                prefix_cost += 4 * min(len(s1), len(s2))
            # if the words are similar, add 1/dissimilarity
            dissimilarity = string_dissimilarity(s1, s2)
            if dissimilarity < 0.5:
                similarity_cost += 1 / (dissimilarity)
            # if the shapes are the same, add 0.05
            if w1.shape() == w2.shape():
                shape_cost += 0.05
            # if the first sound is the same, add 0.05
            if w1.first_sound() == w2.first_sound():
                first_sound_cost += 0.05

        costs = (length_cost, vowel_cost, prefix_cost,
                 similarity_cost, shape_cost, first_sound_cost)
        return costs

    def cost(self):
        """The total 'badness' of this vocabulary."""
        cost = sum(self.costs())
        return cost
    
    def print_costs(self):
        """Print the costs of this vocabulary."""
        (length_cost, vowel_cost, prefix_cost,
         similarity_cost, shape_cost, first_sound_cost) = self.costs()
        print(f'length cost =      {length_cost:8.3f}')
        print(f'vowel cost =       {vowel_cost:8.3f}')
        print(f'prefix cost =      {prefix_cost:8.3f}')
        print(f'similarity cost =  {similarity_cost:8.3f}')
        print(f'shape cost =       {shape_cost:8.3f}')
        print(f'first sound cost = {first_sound_cost:8.3f}')
        print(f'total cost =       {self.cost():8.3f}')
        print()
    
    def alter_if_better(self):
        """Randomly alter this Vocabulary, if it reduces the cost().
        
        Also accept 1/1000 of changes that increase the cost,
        to allow more exploration of the cost space.
        """
        old_cost = self.cost()
        # choose one word, and change it randomly in place
        word_index = random.randrange(0, len(self.words))
        word = self.words[word_index]
        new_word = word.random_variant()
        # if the new word matches an existing word, don't accept the change
        if new_word in self.words:
            return
        self.words[word_index] = new_word
        new_cost = self.cost()
        # if the cost is worse, revert the change with probability 0.999
        # (we want to keep some bad changes, as an annealing thing)
        if new_cost > old_cost:
            #if random.random() < 0.999:
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