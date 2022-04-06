"""CSC108H1: Assignment 3: Poetry Form Checker

Instructions (READ THIS FIRST!)
===============================

Make sure that the code files:
    poetry_constants.py, poetry_functions.py, poetry_program.py,
    poetry_reader.py,
    a3_checker.py, a3_pyta.json and checker_generic.py,
the folder dataset that includes files:
    pronunication_dictionary.txt, pronunication_dictionary_small.txt,
    poetry_forms.txt and poetry_forms_small.txt, and
the folder sample_poems that includes files:
    haiku1.txt, haiku2.txt, etc.
are in the same folder as this file (test_get_last_syllable.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the course CSC108 at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108 Teaching Team.
"""

import unittest
import poetry_functions


class TestGetLastSyllable(unittest.TestCase):

    def test_get_last_syllable_empty(self):
        """Test get_last_syllable on an empty tuple."""

        actual = poetry_functions.get_last_syllable(())
        expected = ()
        self.assertEqual(actual, expected, 'empty tuple')

    # Place your unit test definitions after this line.

    def test_get_last_syllable(self):
        """Test get_last_syllable on a tuple with one syllable."""

        actual = poetry_functions.get_last_syllable(
            ('AE1', 'B', 'S', 'IH0', 'N', 'TH'))
        expected = ('IH0', 'N', 'TH')
        self.assertEqual(actual, expected, 'get syllables')

    def test_get_syllable_count(self):
        """Test get_syllable_count on a poem line."""
        word_to_phonemes = {'THEN': ('DH', 'EH1', 'N'),
                            'ENDS': ('EH1', 'N', 'D', 'Z'),
                            'THE': ('DH', 'AH0'),
                            'POEM': ('P', 'OW1', 'AH0', 'M')}
        line = 'Then! the #poem ends.'

        actual = poetry_functions.get_syllable_count(line, word_to_phonemes)
        expected = 5
        self.assertEqual(actual, expected, 'get syllable count')


# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
