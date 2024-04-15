from wordform import Wordform

class Word():
    def __init__(self, importance:int=1):
        self.importance = importance

    def source_cost(self, wordform:Wordform):
        """The cost of the dissimilarity of this word to its source wordforms.

        Currently, Words have no source wordforms, so this is always zero."""
        return 0
    
    def __gt__(self, other):
        return self.importance > other.importance
    
    def __repr__(self):
        return f"Word({self.importance:.3f})"