from functools import lru_cache

from constants import CACHINESS
from utils import edit_distance
from wordform import Wordform

class Word():
    def __init__(self, source:str=''):
        self.source = source

    @lru_cache(maxsize=CACHINESS)
    def source_cost(self, wordform:Wordform):
        """The cost of the dissimilarity of this word to its source wordforms.

        With just one soure wordform, this is simply the edit distance.
        Consider the source English word 'currency' represented as 'kalensi'.
        Consider the two candidate Wordforms:
          'kalensi' (which is a perfect match)
          'sitelen' (which is arbitrary)
        For an English speaker, 'kalensi' takes almost no effort to learn,
        while 'sitelen' takes full effort (all 7 letters must be memorized).
        """
        return edit_distance(self.source,
                             wordform.spelling())
    
    def __repr__(self):
        return f"Word('{self.source}')"