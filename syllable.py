import random

from constants import *

class Syllable:
    def __init__(self, syllable:str=None):
        """Create a syllable from the given string. Else, a random syllable.
        
        Warning: if the provided syllable is not a legal syllable,
        the resulting Syllable will not be legal.
        """
        if syllable is not None:
            self.parse_string(syllable)
        else:
            self.randomize()

    def parse_string(self, syllable:str):
        """Try to parse a syllable from the given string.
        
        If the given string is not a legal syllable,
        self.onset will be '' or the first letter,
        self.coda will be '' or a final n,
        and self.vowel will be the remaining middle.
        """
        self.onset = self.vowel = self.coda = ''
        if len(syllable) == 0:
            return
        if syllable[0] in ONSETS:
            self.onset = syllable[0]
            syllable = syllable[1:]
        if syllable.endswith('n'):
            self.coda = 'n'
            syllable = syllable[:-1]
        self.vowel = syllable

    def is_legal(self):
        """Is the syllable legal?"""
        if self.onset + self.vowel in ILLEGAL_SUBSTRINGS:
            return False
        return (self.onset in ONSETS and
                self.vowel in VOWELS and
                self.coda in CODAS)

    def randomize(self):
        """Set the syllable to a random legal syllable."""
        self.onset = random.choice(ONSETS)
        self.vowel = random.choice(VOWELS)
        self.coda = random.choice(CODAS)
        # if the syllable is illegal, try again
        if not self.is_legal():
            self.randomize()

    def copy(self):
        """A copy of the syllable."""
        s = Syllable()
        s.onset = self.onset
        s.vowel = self.vowel
        s.coda = self.coda
        return s
    
    def shape(self):
        """The "shape" of the syllable: O, PO, ON, or PON.
        
        Onsets become P, vowels become O, final n becomes N.
        Examples: a is O, ma is PO, en is ON, kin is PON.
        """
        shape = (('P' if self.onset else '') +
                 ('O' if self.vowel else '') +
                 ('N' if self.coda else ''))
        return shape
    
    def first_sound(self):
        """The first sound (onset or vowel) of the syllable."""
        return self.onset if self.onset else self.vowel

    def random_variant(self):
        """A slight variant of this syllable, altered randomly.
        
        Guaranteed to be legal and different from the original."""
        new_syllable = self.copy()
        action = random.choice(['onset', 'vowel', 'coda'])
        if action == 'onset':
            new_syllable.onset = random.choice(ONSETS)
        elif action == 'vowel':
            new_syllable.vowel = random.choice(VOWELS)
        elif action == 'coda':
            new_syllable.coda = random.choice(CODAS)
        # if the new syllable is illegal, try again
        if not new_syllable.is_legal():
            return self.random_variant()
        # if the new syllable is the same as the original, try again
        if str(new_syllable) == str(self):
            return self.random_variant()
        return new_syllable

    def __repr__(self):
        """The string representation of the syllable."""
        return self.onset + self.vowel + self.coda