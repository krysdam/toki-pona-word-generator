import random
from itertools import combinations

from constants import ONSETS, VOWELS

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
            words = []
            # give words random importances,
            # approximately a normal distribution with a mean of 1.
            for _ in range(count):
                importance = sum([random.random()*.5 for _ in range(4)])
                words.append(Word(importance=importance))
        # sort words, most important first.
        words = sorted(words, reverse=True)
        self.wordforms = {w: None for w in words}
        self.set_favorites()

    def set_favorites(self):
        """Set Wordforms so as to minimize inherent and source costs only."""
        print("INITIALIZING...")
        for w in sorted(self.wordforms, reverse=True):
            # best wordforms first.
            solo_cost = lambda wf: wf.inherent_cost() + w.source_cost(wf)
            best_wordforms = sorted(WORDFORMS, key=solo_cost)
            # take the first wordfrom that isn't already in the vocabulary.
            for wf in best_wordforms:
                if wf in self.wordforms.values():
                    print(f'{w!s} wants {wf!s}, but it is already taken.')
                    pass
                else:
                    print(f'{w!s} -> {wf!s}')
                    self.wordforms[w] = wf
                    break

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
            cost += (wf1.similarity_cost(wf2) *
                     max(w1.importance, w2.importance))
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

    def bar_graph(self, title, function):
        """A string bar graph: how many function(word) are in each category?
        
        This is a horizontal stacked bar graph.
        Each bar is composed of repeated copies of the bar's label.
        For example, a bar graph showing the lengths of words
        might look like this:
        LENGTHS  1 222 3333333 44444444444444444444444444444 55 66666 7

        If any label is longer than one character,
        bars are one copy of the lable, followed by one equal sign per word.
        For example, a bar graph showing the shapes of words
        might look like this:
        SHAPE    O== PO===== ON== POPO============= ONPO ====== PONPO===
        """
        # collect values
        values = []
        for w in self.wordforms:
            wf = self.wordforms[w]
            values.append(function(wf))
        values.sort()
        labels = [str(v) for v in values]
        long_labels = any(len(l) > 1 for l in labels)
        
        # make string
        s = f'{title:16s}'
        for i in range(len(labels)):
            prev = labels[i-1]
            label = labels[i]
            new_bar = (i == 0) or (label != prev)
            if long_labels:
                if new_bar:
                    s += '  ' + label
                s += '='
            else:
                if new_bar:
                    s += '  '
                s += label
            
        s += '\n'
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

        # bar graphs to show distribution of wordforms:
        # first sound, shape, length in syllables, length in letters.
        s += self.bar_graph('FIRST SOUND',
                            lambda wf: wf.first_sound())
        s += self.bar_graph('SHAPE',
                            lambda wf: wf.shape())                            
        s += self.bar_graph('SYLLABLES',
                            lambda wf: len(wf.syllables))
        s += self.bar_graph('LETTERS',
                            lambda wf: len(wf.spelling()))
        s += '\n'

        """
        # importance
        s += 'IMPORTANCE\n'
        for imp in range(21):
            s += f'{imp/10:.1f}\t'
            has_imp = [w for w in self.wordforms
                       if int(w.importance*10) == imp]
            for w in has_imp:
                s += f' {w!s}->{self.wordforms[w]!s}'
            s += '\n'
        """

        # importance
        s += 'IMPORTANCE\n'
        for w in sorted(self.wordforms, reverse=True):
            s += f'{w!s} -> {self.wordforms[w]!s}\n'

        s = s.strip()
        return s