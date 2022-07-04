import poetry_reader as poetry_reader
import os.path
import unittest
import sys
sys.path.append(".")


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
