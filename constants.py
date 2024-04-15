# number of instances to cache in Word and Wordform methods.
# (for methods that take two instance, this is squared.)
# (recommend about as many as the size of the vocab,
#  although significantly fewer seems to somehow work too.)
CACHINESS = 128

# toki pona's phonology
ONSETS = ['', 'p', 't', 'k', 's', 'm', 'n', 'l', 'w', 'j']
VOWELS = ['i', 'e', 'a', 'o', 'u']
CODAS = ['', 'n']
# warning: initializing Syllable and Word with strings
# depends on certain features of toki pona's actual phonology:
# each sound must be just one letter, and n is the only coda.
# everything else works with any settings of ONSETS, VOWELS, and CODAS.

# wuwojiti are illegal substrings in any position
ILLEGAL_SUBSTRINGS = ['wu', 'wo', 'ji', 'ti']


# Double toki pona phonology
"""
ONSETS = ['', 'p', 'b', 't', 'd', 'k', 'g',
          'c', 'f', 's', 'z', 'x', 'h', 'm', 'n', 'l', 'r', 'w', 'j']
VOWELS = ['i', 'e', 'a', 'o', 'u']
CODAS = ['', 'n', 'l', 'r']
"""


# Approximate English phonology
"""
ONSETS = ([''] + list('pbtdkg') + list('fvszh') +
          list('mn') + list('lr') + list('wj') +
          ['qu', 'c', 'ch', 'ph', 'th', 'sh', 'wh'] +
          ['pl', 'bl', 'kl', 'gl', 'fl', 'sl', 'cl'] +
          ['pr', 'br', 'tr', 'dr', 'kr', 'gr', 'fr', 'cr', 'wr'] +
          ['tw', 'dw', 'kw', 'sw'] +
          ['sp', 'st', 'sk', 'sm', 'sn', 'sl', 'sw', 'sc', 'squ'] +
          ['spr', 'str', 'skr', 'scr'] + ['spl'])

VOWELS = (list('aeiou') + list('y') +
          ['ai', 'ea', 'ee', 'oa', 'oo', 'ou'])

CODAS = ([''] + list('pbtdkg') + list('fvszh') +
          list('mn') + list('lr') +
          ['c', 'ch', 'ph', 'th', 'sh'] +
          ['lp', 'lb', 'lt', 'ld', 'lk', 'lg', 'lf', 'ls', 'lz', 'lm', 'ln'] +
          ['lsh', 'lth', 'lch', 'lph'] +
          ['rp', 'rb', 'rt', 'rd', 'rk', 'rg', 'rf', 'rs', 'rz', 'rm', 'rn'] +
          ['rsh', 'rth', 'rch', 'rph'] +
          ['mp', 'mb', 'ms', 'mz'] +
          ['nt', 'nd', 'nk', 'ng', 'ns', 'nz'] + ['nth', 'nch'] +
          ['sp', 'st', 'sk'] +
          ['x'])

ILLEGAL_SUBSTRINGS = []
"""