from constants import ONSETS, VOWELS, CODAS, ILLEGAL_SUBSTRINGS

class Syllable:
    def __init__(self, syllable:str):
        """Create a syllable from the given string."""
        self.onset, self.vowel, self.coda = Syllable.parse(syllable)

    def parse(syllable:str):
        """Try to parse the given syllable. Return (onset, vowel, coda).
        
        If the given string is not a legal syllable, raise a ValueError.
        """
        onset = vowel = coda = ''
        try:
            # strip off the onset, if any.
            if syllable[0] in ONSETS:
                onset = syllable[0]
                syllable = syllable[1:]
            # strip off the coda, if any.
            if syllable[-1] in CODAS:
                coda = syllable[-1]
                syllable = syllable[:-1]
        except IndexError:
            raise ValueError(f"Invalid syllable: {syllable}")
        # rest should be a vowel.
        if syllable in VOWELS:
            vowel = syllable
        else:
            raise ValueError(f"Invalid syllable: {syllable}")
        return (onset, vowel, coda)
    
    def first_sound(self):
        """The first sound (onset or vowel) of the syllable."""
        return self.onset or self.vowel

    def shape(self):
        """The "shape" of the syllable: O, PO, ON, or PON.
        
        Onsets become P, vowels become O, final n becomes N.
        Examples: a is O, ma is PO, en is ON, kin is PON.
        """
        shape = (('P' if self.onset else '') +
                 ('O' if self.vowel else '') +
                 ('N' if self.coda else ''))
        return shape
    
    def spelling(self):
        """The actual letters of the syllable, spelled in order."""
        return self.onset + self.vowel + self.coda

    def __repr__(self):
        """An unambiguous string representation of the syllable."""
        return ((self.onset or '_') +
                self.vowel +
                (self.coda or '_'))

    def __str__(self):
        """A simple string representation of the syllable.
        
        Currently, this is the same as the spelling(), but I want the option
        of changing it to something fancier without screwing up everything
        that relies on spelling."""
        return self.onset + self.vowel + self.coda
    
# generate all legal syllables.
SYLLABLES = []
for o in ONSETS:
    for v in VOWELS:
        for c in CODAS:
            syl = o + v + c
            for ill in ILLEGAL_SUBSTRINGS:
                if ill in syl:
                    break
            else:
                SYLLABLES.append(Syllable(syl))