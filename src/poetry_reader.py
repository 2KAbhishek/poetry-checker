"""CSC108H1: Assignment 3: Poetry Form Checker

Instructions (READ THIS FIRST!)
===============================

Make sure that the code files:
    poetry_constants.py, poetry_functions, poetry_program.py,
    test_get_last_syllable.py,
    a3_checker.py, a3_pyta.json and checker_generic.py,
the folder dataset that includes files:
    pronunication_dictionary.txt, pronunication_dictionary_small.txt,
    poetry_forms.txt and poetry_forms_small.txt, and
the folder sample_poems that includes files:
    haiku1.txt, haiku2.txt, etc.
are in the same folder as this file (poetry_reader.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the course CSC108 at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108 Teaching Team.
"""

from typing import TextIO, List, Tuple

from poetry_constants import (POETRY_FORMS_DICT, PRONUNCIATION_DICT)


# ===================== Add Your Helper Functions Here =====================
def get_poetry_form_names(poetry_forms_file: TextIO) -> List[str]:
    poetry_forms_file.seek(0)
    poetry_form_names = []
    for line in poetry_forms_file:
        line = line.strip()
        if line == '':
            continue
        if len(line.split()[0]) > 3:
            poetry_form_names.append(line)
    print(poetry_form_names)
    return poetry_form_names

def get_poetry_form_name_lines(poetry_forms_file: TextIO, poetry_form_name: str) -> List[int]:
    start, end, index = -1, -1, 0
    poetry_forms_file.seek(0)
    print(poetry_form_name)
    for line in poetry_forms_file:
        print("Line: " + line)
        print("index: " + str(index))
        print("start: " + str(start))
        print("end: " + str(end))
        print("len(line): " + str(len(line)))
        line = line.strip()
        if len(line) == 0 and start != -1:
            end = index - 1
        if line.strip() == poetry_form_name:
            start = index + 1
        if start != -1 and end != -1:
            break
        index += 1
    end = index - 1 if end == -1 else end
    print ([start, end])
    return [start, end]

def get_poetry_form_details(poetry_forms_file: TextIO, lines: List[int]) -> Tuple[Tuple[int], Tuple[str]]:
    syllable_counts = []
    rhyming_part = []
    i = 0
    poetry_forms_file.seek(0)

    for line in poetry_forms_file:
        if i >= lines[0] and i <= lines[1]:
            line = line.strip()
            if line == '':
                continue
            count, rhyme = line.split()
            syllable_counts.append(int(count))
            rhyming_part.append(rhyme)
        i += 1
    print(syllable_counts, rhyming_part)
    return tuple([tuple(syllable_counts), tuple(rhyming_part)])


# ===================== Required Functions =================================

def read_pronunciation(pronunciation_file: TextIO) -> PRONUNCIATION_DICT:
    """Return the pronunciation dictionary formed from reading
    pronunciation_file, an open file that is in the format of the CMU
    Pronouncing Dictionary.

    >>> small_pd = open('datasets/pronunciation_dictionary_small.txt')
    >>> word_to_phonemes = read_pronunciation(small_pd)
    >>> small_pd.close()
    >>> word_to_phonemes == {'CAMPBELL': ('K', 'AE1', 'M', 'B', 'AH0', 'L'),
    ...                      'GRIES': ('G', 'R', 'AY1', 'Z'),
    ...                      'SMITH': ('S', 'M', 'IH1', 'TH')}
    True
    """
    word_to_phonemes = {}
    for line in pronunciation_file:
        line = line.strip()
        if line == '' or line[0] == ';':
            continue
        word, phonemes = line.split('  ')
        phonemes = tuple(phonemes.split())
        word_to_phonemes[word] = phonemes
    return word_to_phonemes


def read_poetry_form_descriptions(poetry_forms_file: TextIO) \
        -> POETRY_FORMS_DICT:
    """Return a dictionary of poetry form name to poetry form description for
    the poetry forms in poetry_forms_file.

    >>> small_pf = open('datasets/poetry_forms_small.txt')
    >>> name_to_description = read_poetry_form_descriptions(small_pf)
    >>> small_pf.close()
    >>> name_to_description == {
    ...     'Haiku': ((5, 7, 5), ('*', '*', '*')),
    ...     'Limerick': ((8, 8, 5, 5, 8), ('A', 'A', 'B', 'B', 'A'))}
    True
    """


if __name__ == '__main__':
    import doctest
    # Uncomment the line below if you prefer to test your examples with doctest
    # doctest.testmod()
