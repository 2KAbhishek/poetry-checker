"""CSC108H1: Assignment 3: Poetry Form Checker

Instructions (READ THIS FIRST!)
===============================

Make sure that the code files:
    poetry_constants.py, poetry_functions, poetry_reader.py,
    test_get_last_syllable.py,
    a3_checker.py, a3_pyta.json and checker_generic.py,
the folder dataset that includes files:
    pronunication_dictionary.txt, pronunication_dictionary_small.txt,
    poetry_forms.txt and poetry_forms_small.txt, and
the folder sample_poems that includes files:
    haiku1.txt, haiku2.txt, etc.
are in the same folder as this file (poetry_program.py).

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

import os.path
import poetry_functions
import poetry_reader

from poetry_constants import (POEM, PRONUNCIATION_DICT,
                              POETRY_FORM_DESCRIPTION, POETRY_FORMS_DICT)

DICTIONARY_FILENAME = os.path.dirname(__file__) +\
     '/../data/pronunciation_dictionary.txt'
POETRY_FORMS_FILENAME = os.path.dirname(__file__) +\
     '/../data/poetry_forms.txt'
SAMPLE_POEMS_FOLDER = os.path.dirname(__file__) +\
     '/../data/sample_poems'


def get_poem_filename(msg: str) -> str:
    """Prompt the user, using msg, to type the name of a poem file. This file
    should exist in the SAMPLE_POEMS_FOLDER in the same folder as the starter
    code. If the file does not exist, keep prompting until the user gives a
    valid poem filename. Return the path to the poem file.
    """

    filename = input(msg)
    poem_filename = SAMPLE_POEMS_FOLDER + '/' + filename
    while not os.path.exists(poem_filename):
        print("That file does not exist.")
        filename = input(msg)
        poem_filename = SAMPLE_POEMS_FOLDER + '/' + filename
    return poem_filename


def trim_lines(list_of_lines: List[str]) -> POEM:
    """Return a list that is the same as list_of_lines, except that empty
    strings in list_of_lines and whitespace-only strings are not included.
    In addition, leading and trailing space from each line in list_of_lines
    is not included.

    >>> my_list = ['    ', 'A', '', ' BCD  ', '  ', '\t']
    >>> trim_lines(my_list)
    ['A', 'BCD']
    """

    newlines = []
    for line in list_of_lines:
        line = line.strip()
        if line:
            newlines.append(line)
    return newlines


def get_poem_lines(poem: str) -> POEM:
    r"""Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line.

    >>> get_poem_lines('Line 1: has text.\n\n\n  Line 4: Lines 2,3 empty. \n' +
    ...                '    Line 5: The End.    \n')
    ['Line 1: has text.', 'Line 4: Lines 2,3 empty.', 'Line 5: The End.']
    """

    list_of_lines = poem.split('\n')
    trimmed_lines = trim_lines(list_of_lines)

    return trimmed_lines


def make_menu(poetry_forms: POETRY_FORMS_DICT) -> Tuple[str, Dict[str, str]]:
    r"""Return a numbered menu of the poetry form names that are keys in
    poetry_forms.

    >>> d = {'Haiku': ((5, 7, 5), ('*', '*', '*')),
    ...         'Unknown': ((1, 2, 3), ('A', 'B', 'C'))}
    >>> menu = make_menu(d)
    >>> menu == ('1: Haiku\n2: Unknown\n', {'1': 'Haiku', '2': 'Unknown'})
    True
    """

    menu = ''
    menu_dict = {}

    # Sort the names so that they appear in alphabetical order in the menu.
    form_names = list(poetry_forms.keys())
    form_names.sort()

    i = 1
    for form_name in form_names:
        menu += '{}: {}\n'.format(i, form_name)
        menu_dict[str(i)] = form_name
        i = i + 1

    return menu, menu_dict


def check_poem(poem_lines: POEM,
               description: POETRY_FORM_DESCRIPTION,
               word_to_phonemes: PRONUNCIATION_DICT,
               form_name: str) -> None:
    """Check whether the poem in poem_lines has the right number of lines to
    match for form given in description, and print a message if it doesn't.
    If it does, then check whether the lines in the poem have the right number
    of syllables and report the lines that don't; also check whether the
    lines of the poem have the correct rhyming scheme and report the lines
    that should rhyme but don't.
    """

    if len(poem_lines) != len(description[0]):
        print("\n== The poem doesn't have the right number of lines. == \n")
    else:
        problem_lines = poetry_functions.check_syllable_counts(
            poem_lines, description, word_to_phonemes)

        if len(problem_lines) == 0:
            print('\nThe poem has the right number of syllables '
                  'on each line.\n')
        else:
            print('\n== The poem is not a {}.=='.format(form_name))
            print('These line(s) don\'t have the right number of syllables:')
            print('\n'.join(problem_lines) + '\n')

        problem_rhymes = poetry_functions.check_rhyme_scheme(
            poem_lines, description, word_to_phonemes)

        if len(problem_rhymes) == 0:
            print('The poem follows the rhyme scheme.\n')
        else:
            print('\n== The poem is not a {}. These lines should rhyme'
                  " but don't: ==".format(form_name))
            for lines in problem_rhymes:
                print('\n'.join(lines) + '\n')


def main() -> None:
    """Main program for the Poetry Form Checker.
    """

    word_to_phonemes = poetry_reader.read_pronunciation(
        open(DICTIONARY_FILENAME))
    name_to_description = poetry_reader.read_poetry_form_descriptions(
        open(POETRY_FORMS_FILENAME))

    menu, menu_dict = make_menu(name_to_description)
    print('=================================================')
    print('Here is a list of known poetry forms:\n' + menu)
    prompt = 'Enter number for poetry form to check (0 to quit):\n'
    form_num = input(prompt)

    while form_num not in ('', '0'):
        if form_num in menu_dict:
            form_name = menu_dict[form_num]
            description = name_to_description[form_name]

            msg = 'Enter name of poem file in folder ' + SAMPLE_POEMS_FOLDER \
                  + ': '
            poem_filename = get_poem_filename(msg)
            poem_file = open(poem_filename)
            poem = poem_file.read()
            poem_file.close()
            poem_lines = get_poem_lines(poem)

            check_poem(poem_lines, description, word_to_phonemes, form_name)

            print('=================================================')
            print('Here is a list of known poetry forms:\n' + menu)
            form_num = input(prompt)
        else:
            form_num = input('Invalid number. ' + prompt)


if __name__ == '__main__':
    main()
