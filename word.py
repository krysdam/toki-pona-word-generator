import random

from utils import *

from syllable import Syllable

class Word:
    def __init__(self, word:str=None, syllable_count:int=2):
        """Create a word from the given string. Else, a random word.
        
        Warning: if the provided word is not a possible legal word,
        the resulting Word will not be legal."""
        if word is not None:
            self.parse_string(word)
        else:
            self.randomize(syllable_count = syllable_count)

    def parse_string(self, word:str):
        """Parse a word from the given string.
        
        If the given string is not a valid word,
        parse as many legal syllables as possible from the end of the word,
        and put the rest as an illegal syllable at the beginning.
        """
        # in a toki pona word,
        # the longest suffix that is a legal syllable
        # is always an actual syllable of the word.
        # so, check if the last 3 letters is a syllable,
        # else 2 letters, else 1 letter.
        # if none of these is a syllable, the word is not legal.
        syllables = []
        while word:
            for length in [3, 2, 1, -1]:
                syl = Syllable(word[-length:])
                if syl.is_legal():
                    syllables.insert(0, syl)
                    word = word[:-length]
                    break
                # if we reach the -1 case, the word is not legal.
                # record what we have so far, and return.
                if length == -1:
                    syllables.insert(0, Syllable(word))
                    self.syllables = syllables
                    return
        self.syllables = syllables

    def is_legal(self):
        """Is the word legal?"""
        # must contain at least one syllable
        if not self.syllables:
            return False
        # each syllable must be legal
        for syllable in self.syllables:
            if not syllable.is_legal():
                return False
        # cannot have nn or nm
        for syl1, syl2 in zip(self.syllables, self.syllables[1:]):
            if syl1.coda == 'n' and syl2.onset in ['n', 'm']:
                return False
        # cannot have empty onset after first syllable
        for syllable in self.syllables[1:]:
            if syllable.onset == '':
                return False
        return True

    def randomize(self, syllable_count:int=2):
        """Set the word to a random legal two-syllable word."""
        self.syllables = [Syllable() for _ in range(syllable_count)]
        # if the word is illegal, try again
        if not self.is_legal():
            self.randomize(syllable_count = syllable_count)

    def copy(self):
        """A copy of the word."""
        w = Word()
        w.syllables = [s.copy() for s in self.syllables]
        return w
    
    def shape(self):
        """The "shape" of the syllable.
        
        Onsets become P, vowels become O, final n becomes N.
        Examples: a is O, ma is PO, en is ON, kin is PON.
        kala is POPO, akesi is OPOPO, and sitelen is POPOPON.
        """
        return ''.join([s.shape() for s in self.syllables])

    def first_sound(self):
        """The first sound (onset or vowel) of the word."""
        return self.syllables[0].first_sound()

    def random_variant(self):
        """A variant of this word, altered randomly.
        
        Guaranteed to be legal and different from the original."""
        new_word = self.copy()
        # usually alter a random syllable,
        # sometimes add or remove one, sometimes replace the whole word.
        action = random.choices(['alter', 'add', 'remove', 'replace'],
                                [100, 10, 10, 1],
                                k=1)[0]
        if action == 'add':
            new_word.syllables.append(Syllable())
        elif action == 'remove':
            if len(new_word.syllables) > 1:
                new_word.syllables.pop()
        elif action == 'replace':
            new_word = Word()
        elif action == 'alter':
            index = random.randrange(0, len(new_word.syllables))
            syllable = new_word.syllables[index]
            new_word.syllables[index] = syllable.random_variant()
        # if the new word is illegal, try again
        if not new_word.is_legal():
            return self.random_variant()
        # if the new word is the same as the old word, try again
        if str(new_word) == str(self):
            return self.random_variant()
        return new_word
    
    def inherent_cost(self):
        """The cost of this word's word-form. Higher is worse.
        
        Difficult words are bad. This is counted in two ways.
        Length: each letter of length of a word counts for 1 cost.
        Starting with a vowel: starting with a vowel costs 0.5.
            In other words, an initial glottal stop counts as 0.5 letters.
        """
        cost = 0
        cost += len(str(self))
        if self.syllables[0].onset == '':
            cost += 0.5
        return cost
    
    def similarity_cost(self, other):
        """The similarity of two words, as a number. Higher is more similar.

        Similar words are bad. This is counted in a few ways.
        Prefixes: If one word is a prefix of another, that's very bad.
            Add (2 + length of the prefix) to the cost.
        Edit distance: if adjusted edit distance < 0.5, add 1/that to cost.
        Word shape: if shape is the same, add 0.1 to cost.
        First sound: if first sound is the same, add 0.1 to cost.
        """
        cost = 0
        s1, s2 = str(self), str(other)
        # if one is a prefix, add 2 + length of the prefix
        if s1.startswith(s2) or s2.startswith(s1):
            cost += 2 + min(len(s1), len(s2))
        # if the words are similar, add 1/dissimilarity
        dissimilarity = edit_distance_adjusted(s1, s2)
        if dissimilarity < 0.5:
            cost += 1 / (dissimilarity)
        # if the shapes are the same, add 0.1
        if self.shape() == other.shape():
            cost += 0.1
        # if the first sound is the same, add 0.1
        if self.first_sound() == other.first_sound():
            cost += 0.1
        return cost

    def __gt__(self, other):
        """Compare two words by their string representations."""
        return str(self) > str(other)
    
    def __eq__(self, other):
        """Compare two words by their string representations."""
        return str(self) == str(other)

    def __repr__(self):
        """The string representation of the word."""
        return ''.join([str(s) for s in self.syllables])