from typing import Dict, List, Tuple

"""
A list of type definitions used in the Poetry Form Checker.
"""

POEM_LINE = str
"""
A poem line: a line from a poem that is not empty and for which the leading
and trailing space has been removed.
"""

POEM = List[POEM_LINE]
"""
A poem: a list of lines in a poem where empty lines and whitespace-only lines
are removed, and the leading and trailing space on each line is not included.
"""


PHONEMES = Tuple[str]
"""
The pronunciation for a single word or part of a word: a tuple of phonemes.

For example:
('G', 'UW1', 'F', 'IY0')
"""
PRONUNCIATION_DICT = Dict[str, PHONEMES]
"""
A pronunciation dictionary: Dict[str, Tuple[str]]
  - each key is a word
  - each value is the tuple of phonemes for that word's pronunciation

For example, here is a (small) pronunciation dictionary:
{'DANIEL': ('D', 'AE1', 'N', 'Y', 'AH0', 'L'),
 'IS': ('IH1', 'Z'),
 'GOOFY': ('G', 'UW1', 'F', 'IY0')}
"""

POETRY_FORM_DESCRIPTION = Tuple[Tuple[int], Tuple[str]]
"""
A poetry form description: a two-item tuple of (Tuple[int], Tuple[str])
  - first item is a tuple of the number of syllables required in each line
  - second item is a tuple describing the rhyme scheme rule for each line
  - the two items are parallel tuples

For example, a limerick has this poetry form description:
((8, 8, 5, 5, 8), ('A', 'A', 'B', 'B', 'A'))
"""

POETRY_FORMS_DICT = Dict[str, POETRY_FORM_DESCRIPTION]
"""
Poetry form description dictionary:
  - The keys are poetry form names
  - The values are decriptions of the poetry forms

Here is an example:
{'Haiku': ((5, 7, 5), ('*', '*', '*')),
 'Limerick': ((8, 8, 5, 5, 8), ('A', 'A', 'B', 'B', 'A'))}
"""
