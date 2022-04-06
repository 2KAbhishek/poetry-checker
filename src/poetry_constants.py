"""CSC108H1: Assignment 3: Poetry Form Checker

Instructions (READ THIS FIRST!)
===============================

Make sure that the code files:
    poetry_functions.py, poetry_program.py, poetry_reader.py,
    test_get_last_syllable.py,
    a3_checker.py, a3_pyta.json and checker_generic.py,
the folder dataset that includes files:
    pronunication_dictionary.txt, pronunication_dictionary_small.txt,
    poetry_forms.txt and poetry_forms_small.txt, and
the folder sample_poems that includes files:
    haiku1.txt, haiku2.txt, etc.
are in the same folder as this file (poetry_constants.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the course CSC108 at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108 Teaching Team.
"""

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
