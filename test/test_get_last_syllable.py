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
import os.path
import unittest

import src.poetry_functions as poetry_functions
import src.poetry_reader as poetry_reader


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


class TestGetSyllableCount(unittest.TestCase):
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


class TestWordsRhyme(unittest.TestCase):
    word_to_phonemes = {'THINE': ('DH', 'AY1', 'N'),
                        'DEVINE': ('D', 'AH0', 'V', 'AY1', 'N'),
                        'HEARD': ('HH', 'ER1', 'D')}

    def test_words_rhyme(self):
        """Test words_rhyme on a poem line, positive case."""
        rhymes = poetry_functions.words_rhyme(
            'thine', 'devine', self.word_to_phonemes)
        self.assertTrue(rhymes, 'words rhyme')

    def test_words_dont_rhyme(self):
        """Test words_rhyme on a poem line, negative case."""
        rhymes = poetry_functions.words_rhyme(
            'thine', 'heard', self.word_to_phonemes)
        self.assertFalse(rhymes, 'words do not rhyme')


class TestCheckSyllableCounts(unittest.TestCase):
    word_to_phonemes = {'NEXT': ('N', 'EH1', 'K', 'S', 'T'),
                        'GAP': ('G', 'AE1', 'P'),
                        'BEFORE': ('B', 'IH0', 'F', 'AO1', 'R'),
                        'LEADS': ('L', 'IY1', 'D', 'Z'),
                        'WITH': ('W', 'IH1', 'DH'),
                        'LINE': ('L', 'AY1', 'N'),
                        'THEN': ('DH', 'EH1', 'N'),
                        'THE': ('DH', 'AH0'),
                        'A': ('AH0'),
                        'FIRST': ('F', 'ER1', 'S', 'T'),
                        'ENDS': ('EH1', 'N', 'D', 'Z'),
                        'POEM': ('P', 'OW1', 'AH0', 'M'),
                        'OFF': ('AO1', 'F')}

    def test_check_syllable_counts(self):
        """Test check_syllable_counts on poem lines."""
        poem_lines = ['The first line leads off,',
                      'With a gap before the next.', 'Then the poem ends.']
        description = ((5, 5, 4), ('*', '*', '*'))

        actual = poetry_functions.check_syllable_counts(
            poem_lines, description, self.word_to_phonemes)
        expected = ['With a gap before the next.', 'Then the poem ends.']
        self.assertEqual(actual, expected, 'check syllable counts')

    def test_check_syllable_counts_empty(self):
        """Test check_syllable_counts on poem lines, empty scenario."""
        poem_lines = ['The first line leads off,']
        description = ((0,), ('*'))

        actual = poetry_functions.check_syllable_counts(
            poem_lines, description, self.word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected, 'check syllable counts')


class TestAllLinesRhyme(unittest.TestCase):
    word_to_phonemes = {'THE': ('DH', 'AH0'),
                        'MOUSE': ('M', 'AW1', 'S'),
                        'IN': ('IH0', 'N'),
                        'MY': ('M', 'AY1'),
                        'HOUSE': ('HH', 'AW1', 'S'),
                        'ELECTRIC': ('IH0', 'L', 'EH1', 'K',
                                     'T', 'R', 'IH0', 'K')}
    poem_lines = ['The mouse', 'in my house', 'electric.']

    def test_all_lines_rhyme(self):
        """Test all_lines_rhyme on poem lines."""
        lines_to_check = [0, 1]
        rhymes = poetry_functions.all_lines_rhyme(
            self.poem_lines, lines_to_check, self.word_to_phonemes)
        self.assertTrue(rhymes, 'all lines rhyme')

    def test_all_lines_dont_rhyme(self):
        """Test all_lines_rhyme on poem lines, negative case."""
        lines_to_check = [0, 1, 2]
        rhymes = poetry_functions.all_lines_rhyme(
            self.poem_lines, lines_to_check, self.word_to_phonemes)
        self.assertFalse(rhymes, 'all lines do not rhyme')


class TestGetSymbolToLines(unittest.TestCase):
    def test_get_sympol_to_lines(self):
        """Test to generate symbols for lines"""
        actual = poetry_functions.get_symbol_to_lines(
            ('A', 'A', 'B', 'B', 'A'))
        expected = {'A': [0, 1, 4], 'B': [2, 3]}
        self.assertEqual(actual, expected, 'get symbol to lines')

    def test_get_sympol_to_lines_asterisk(self):
        """Test to generate symbols for lines, asterisks case"""
        actual = poetry_functions.get_symbol_to_lines(
            ('*', '*', '*', '*', '*'))
        expected = {'*': [0, 1, 2, 3, 4]}
        self.assertEqual(actual, expected, 'get symbol to lines')


class TestCheckRhymeScheme(unittest.TestCase):
    word_to_phonemes = {'NEXT': ('N', 'EH1', 'K', 'S', 'T'),
                        'GAP': ('G', 'AE1', 'P'),
                        'BEFORE': ('B', 'IH0', 'F', 'AO1', 'R'),
                        'LEADS': ('L', 'IY1', 'D', 'Z'),
                        'WITH': ('W', 'IH1', 'DH'),
                        'LINE': ('L', 'AY1', 'N'),
                        'THEN': ('DH', 'EH1', 'N'),
                        'THE': ('DH', 'AH0'),
                        'A': ('AH0'),
                        'FIRST': ('F', 'ER1', 'S', 'T'),
                        'ENDS': ('EH1', 'N', 'D', 'Z'),
                        'POEM': ('P', 'OW1', 'AH0', 'M'),
                        'OFF': ('AO1', 'F')}

    def test_check_rhyme_scheme(self):
        """Test check_rhyme_scheme on poem lines."""
        poem_lines = ['The first line leads off,',
                      'With a gap before the next.', 'Then the poem ends.']
        description = ((5, 7, 5), ('A', 'B', 'A'))

        actual = poetry_functions.check_rhyme_scheme(poem_lines, description,
                                                     self.word_to_phonemes)
        actual.sort()
        expected = [['The first line leads off,', 'Then the poem ends.']]
        self.assertEqual(actual, expected, 'check rhyme scheme')


class TestReadPronunciation(unittest.TestCase):
    def test_read_pronunciation(self):
        """Test phonemes on a pronunciation dictionary."""
        import os
        small_pd = open(os.path.dirname(__file__) +
                        '/../data/pronunciation_dictionary_small.txt')
        actual = poetry_reader.read_pronunciation(small_pd)

        expected = {'CAMPBELL': ('K', 'AE1', 'M', 'B', 'AH0', 'L'),
                    'GRIES': ('G', 'R', 'AY1', 'Z'),
                    'SMITH': ('S', 'M', 'IH1', 'TH')}
        self.assertEqual(actual, expected, 'read pronunciation')


class TestReadPoetryFormDetails(unittest.TestCase):
    def test_read_poetry_form_details(self):
        """Test whether the poetry form details are read correctly."""
        import os
        small_pf = open(os.path.dirname(__file__) +
                        '/../data/poetry_forms_small.txt')
        actual = poetry_reader.read_poetry_form_descriptions(small_pf)
        expected = {
            'Haiku': ((5, 7, 5), ('*', '*', '*')),
            'Limerick': ((8, 8, 5, 5, 8), ('A', 'A', 'B', 'B', 'A'))}
        self.assertEqual(actual, expected, 'read poetry form details')


# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
