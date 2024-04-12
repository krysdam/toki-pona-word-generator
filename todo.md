- define word-similarity on words:
  = 4x prefix + 1/dissimilarity + 0.05*word_shape + 0.05*first_sound
  then use this for generating words.
  But the shape and first sound weights seem too low in this context.
- idea: instead of words pushing just off each other, they should push off other source words
- dissimilarity function is not quite what I want.
  cost of (mama, wawa) should be low, but not zero.
  two methods of finding what I really mean here:
    - think through cost of pairs of words, and compare their dissimilarities
    - reason my way to a function from first principles
      (possibly not involving edit distance at all)
- known local minimum trap: single vowel words take out that whole vowel
- make good terminal interface
- care about word frequency (multiply costs due to a word by its importance)