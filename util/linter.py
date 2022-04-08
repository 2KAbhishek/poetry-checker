from io import StringIO
import os.path
from typing import Any, Dict
from copy import deepcopy
import unittest
import linter_generic
import poetry_functions
import poetry_reader

PYTA_CONFIG = 'pyta.json'
FILENAME_FUNCTIONS = os.path.dirname(__file__) +\
    '/../src/poetry_functions.py'
FILENAME_READER = os.path.dirname(__file__) +\
    '/../src/poetry_reader.py'
TARGET_LEN = 79
SEP = '='


SAMPLE_POETRY_FORM_FILE = '''Limerick
8 A
8 A
5 B
5 B
8 A

Haiku
5 *
7 *
5 *
'''

SAMPLE_DICTIONARY_FILE = ''';;; Comment line
;;; Another comment line
ABSINTHE  AE1 B S IH0 N TH
HEART  HH AA1 R T
FONDER  F AA1 N D ER0
'''


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    # Functions from poetry_functions.py

    # Functions related to syllable counts

    def test_get_syllable_count(self) -> None:
        """Function get_syllable_count."""

        poem_line = 'Then! the #poem ends.'
        word_to_phonemes = {'THEN': ('DH', 'EH1', 'N'),
                            'ENDS': ('EH1', 'N', 'D', 'Z'),
                            'THE': ('DH', 'AH0'),
                            'POEM': ('P', 'OW1', 'AH0', 'M')}
        word_to_phonemes_copy = deepcopy(word_to_phonemes)

        self._check(poetry_functions.get_syllable_count,
                    [poem_line, word_to_phonemes], int)
        self._check_no_mutation(poetry_functions.get_syllable_count,
                                word_to_phonemes, word_to_phonemes_copy)

    def test_check_syllable_counts(self) -> None:
        """Function check_syllable_counts."""

        poem_lines = ['The first line leads off,',
                      'With a gap before the next.', 'Then the poem ends.']
        description = ((5, 5, 4), ('*', '*', '*'))
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
        poem_lines_copy = deepcopy(poem_lines)
        word_to_phonemes_copy = deepcopy(word_to_phonemes)
        types = (str, str)

        self._test_returns_collection_of(
            poetry_functions.check_syllable_counts,
            [poem_lines, description, word_to_phonemes], list, types)
        self._check_no_mutation(poetry_functions.check_syllable_counts,
                                poem_lines, poem_lines_copy)
        self._check_no_mutation(poetry_functions.check_syllable_counts,
                                word_to_phonemes, word_to_phonemes_copy)

    # Functions related to rhyming

    def test_get_last_syllable(self) -> None:
        """Function get_last_syllable."""

        phoneme = ('AE1', 'B', 'S', 'IH0', 'N', 'TH')
        types = (str, str, str)

        self._test_returns_collection_of(
            poetry_functions.get_last_syllable, [phoneme], tuple, types)

    def test_words_rhyme(self) -> None:
        """Function words_rhyme."""

        word_to_phonemes = {'THINE': ('DH', 'AY1', 'N'),
                            'DEVINE': ('D', 'AH0', 'V', 'AY1', 'N'),
                            'HEARD': ('HH', 'ER1', 'D')}
        word_to_phonemes_copy = deepcopy(word_to_phonemes)

        self._check(poetry_functions.words_rhyme,
                    ['thine', 'devine', word_to_phonemes], bool)
        self._check_no_mutation(poetry_functions.words_rhyme,
                                word_to_phonemes, word_to_phonemes_copy)

    def test_all_lines_rhyme(self) -> None:
        """Function all_lines_rhyme."""

        poem_lines = ['The mouse', 'in my house', 'electric.']
        lines_to_check = [0, 1]
        word_to_phonemes = {'THE': ('DH', 'AH0'),
                            'MOUSE': ('M', 'AW1', 'S'),
                            'IN': ('IH0', 'N'),
                            'MY': ('M', 'AY1'),
                            'HOUSE': ('HH', 'AW1', 'S'),
                            'ELECTRIC': ('IH0', 'L', 'EH1', 'K',
                                         'T', 'R', 'IH0', 'K')}
        poem_lines_copy = deepcopy(poem_lines)
        lines_to_check_copy = deepcopy(lines_to_check)
        word_to_phonemes_copy = deepcopy(word_to_phonemes)

        self._check(poetry_functions.all_lines_rhyme,
                    [poem_lines, lines_to_check, word_to_phonemes], bool)
        self._check_no_mutation(poetry_functions.all_lines_rhyme,
                                poem_lines, poem_lines_copy)
        self._check_no_mutation(poetry_functions.all_lines_rhyme,
                                lines_to_check, lines_to_check_copy)
        self._check_no_mutation(poetry_functions.all_lines_rhyme,
                                word_to_phonemes, word_to_phonemes_copy)

    def test_get_symbol_to_lines(self) -> None:
        """Function get_symbol_to_lines."""

        rhyme_scheme = ('A', 'A', 'B', 'B', 'A')

        self._test_returns_dict_of_str_to_list_of_int(
            poetry_functions.get_symbol_to_lines, [rhyme_scheme])

    def test_check_rhyme_scheme(self) -> None:
        """Function check_rhyme_scheme."""

        poem_lines = ['The first line leads off,',
                      'With a gap before the next.', 'Then the poem ends.']
        description = ((5, 5, 4), ('A', 'B', 'A'))
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
        poem_lines_copy = deepcopy(poem_lines)
        word_to_phonemes_copy = deepcopy(word_to_phonemes)
        types = (str, str)

        self._test_returns_list_of_list_of_str(
            poetry_functions.check_rhyme_scheme,
            [poem_lines, description, word_to_phonemes])
        self._check_no_mutation(poetry_functions.check_rhyme_scheme,
                                poem_lines, poem_lines_copy)
        self._check_no_mutation(poetry_functions.check_rhyme_scheme,
                                word_to_phonemes, word_to_phonemes_copy)

    # Functions from poetry_reader.py

    def test_read_pronunciation(self) -> None:
        """A simple check for read_pronunciation."""

        self._test_returns_dict_of_str_to_tuple_of_str(
            poetry_reader.read_pronunciation,
            [StringIO(SAMPLE_DICTIONARY_FILE)])

    def test_read_poetry_form_descriptions(self) -> None:
        """A simple check for read_poetry_form_descriptions."""

        self._test_returns_poetry_forms_dict(
            poetry_reader.read_poetry_form_descriptions,
            [StringIO(SAMPLE_POETRY_FORM_FILE)])

    # Check helper functions

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print('\nChecking {}...'.format(func.__name__))
        result = linter_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print('  check complete')

    def _check_no_mutation(self, func: callable, actual, expected) -> None:
        """Check that func does not mutate that argument actual so that
        it still matches expected.
        """
        self.assertTrue(expected == actual,
                        '{0} should not mutate its arguments'.format(
                            func.__name__))

    def _test_returns_collection_of(self, func, args, coll_type, types):
        """Check that func when called with args returns a coll_type of
        elements of typef from types.

        """

        print('\nChecking {}...'.format(func.__name__))

        coll_type_name = coll_type.__name__

        result = linter_generic.check(func, args, coll_type)
        self.assertTrue(result[0], result[1])

        msg = '{} should return a {} of length {}'
        self.assertEqual(len(result[1]), len(types),
                         msg.format(func.__name__, coll_type_name,
                         len(types)))

        msg = ('Element at index {} in the {} returned '
               'should be of type {}. Got {}.')
        for i, typ in enumerate(types):
            self.assertTrue(isinstance(result[1][i], typ),
                            msg.format(i, coll_type_name, typ, result[1][i]))

        print('  check complete')

    def _test_returns_dict_of_str_to_list_of_int(self, func, args):
        """Check that func when called with args returns a dict that maps
        objects of type str to objects of type list of int.
        """

        print('\nChecking {}...'.format(func.__name__))

        result = linter_generic.check(func, args, dict)
        self.assertTrue(result[0], result[1])

        msg = '{} should return a Dict[str, List[int]] ' + \
              'but instead returned {}'
        for key, value in result[1].items():
            self.assertTrue(isinstance(key, str) and isinstance(value, list),
                            msg.format(func.__name__, result[1]))
            for item in value:
                self.assertTrue(isinstance(item, int),
                                msg.format(func.__name__, result[1]))

        print('  check complete')

    def _test_returns_dict_of_str_to_tuple_of_str(self, func, args):
        """Check that func when called with args returns a dict that maps
        objects of type str to objects of type tuple of str.
        """

        print('\nChecking {}...'.format(func.__name__))

        result = linter_generic.check(func, args, dict)
        self.assertTrue(result[0], result[1])

        msg = '{} should return a Dict[str, Tuple[str]] ' + \
              'but instead returned {}'
        for key, value in result[1].items():
            self.assertTrue(isinstance(key, str) and isinstance(value, tuple),
                            msg.format(func.__name__, result[1]))
            for item in value:
                self.assertTrue(isinstance(item, str),
                                msg.format(func.__name__, result[1]))

        print('  check complete')

    def _test_returns_list_of_list_of_str(self, func, args):
        """Check that func when called with args returns a list of
        items that are lists of str.
        """

        print('\nChecking {}...'.format(func.__name__))

        result = linter_generic.check(func, args, list)
        self.assertTrue(result[0], result[1])

        msg = '{} should return a List[List[str]] ' + \
              'but instead returned {}'
        for outer_item in result[1]:
            self.assertTrue(isinstance(outer_item, list),
                            msg.format(func.__name__, result[1]))
            for inner_item in outer_item:
                self.assertTrue(isinstance(inner_item, str),
                                msg.format(func.__name__, result[1]))

        print('  check complete')

    def _test_returns_poetry_forms_dict(self, func, args):
        """Check that func when called with args returns a dict that maps
        objects of type str to a two-tuple where the first item is a tuple
        of int and the second item is a tuple of str.
        """

        print('\nChecking {}...'.format(func.__name__))

        result = linter_generic.check(func, args, dict)
        self.assertTrue(result[0], result[1])

        msg = '{} should return a Dict[str, Tuple[Tuple[int], Tuple[str]]]' + \
              ' with parallel inner Tuples but instead returned {}'
        for key, value in result[1].items():
            self.assertTrue(isinstance(key, str) and isinstance(value, tuple),
                            msg.format(func.__name__, result[1]))

            self.assertEqual(len(value), 2,
                             msg.format(func.__name__, result[1]))

            types = (int, str)
            for i in range(len(types)):
                self.assertTrue(isinstance(value[i], tuple),
                                msg.format(func.__name__, result[1]))
                for item in value[i]:
                    self.assertTrue(isinstance(item, types[i]),
                                    msg.format(func.__name__, result[1]))

            self.assertEqual(len(value[0]), len(value[1]),
                             msg.format(func.__name__, result[1]))

        print('  check complete')


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style '.center(TARGET_LEN, SEP))
linter_generic.run_pyta(FILENAME_FUNCTIONS, PYTA_CONFIG)
linter_generic.run_pyta(FILENAME_READER, PYTA_CONFIG)
print(' End checking coding style '.center(TARGET_LEN, SEP))

print('\n' + ' Start: checking type contracts '.center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
