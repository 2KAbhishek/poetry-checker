from typing import TextIO, List, Tuple

from src.poetry_constants import (POETRY_FORMS_DICT, PRONUNCIATION_DICT)


# ===================== Add Your Helper Functions Here =====================
def get_poetry_form_names(poetry_forms_file: TextIO) -> List[str]:
    """Return a list of poetry form names in poetry_forms_file.
    >>> import os
    >>> small_pf = open(os.path.dirname(__file__) +\
     '/../data/poetry_forms_small.txt')
    >>> poetry_form_names = get_poetry_form_names(small_pf)
    >>> small_pf.close()
    >>> poetry_form_names == ['Haiku', 'Limerick']
    True
    """
    poetry_forms_file.seek(0)
    poetry_form_names = []
    for line in poetry_forms_file:
        line = line.strip()
        if line == '':
            continue
        if len(line.split()[0]) > 3:
            poetry_form_names.append(line)
    return poetry_form_names


def get_poetry_form_name_lines(poetry_forms_file: TextIO,
                               poetry_form_name: str) -> List[int]:
    """Return the first and last lines in poetry_forms_file that contain
    details for poetry_form_name.
    >>> import os
    >>> small_pf = open(os.path.dirname(__file__) +\
        '/../data/poetry_forms_small.txt')
    >>> poetry_form_name_lines = get_poetry_form_name_lines(small_pf, 'Haiku')
    >>> small_pf.close()
    >>> poetry_form_name_lines == [1, 3]
    True
    """
    start, end, index = -1, -1, 0
    poetry_forms_file.seek(0)
    for line in poetry_forms_file:
        line = line.strip()
        if len(line) == 0 and start != -1:
            end = index - 1
        if line.strip() == poetry_form_name:
            start = index + 1
        if start != -1 and end != -1:
            break
        index += 1
    end = index - 1 if end == -1 else end
    return [start, end]


def get_poetry_form_details(poetry_forms_file: TextIO,
                            lines: List[int]) -> Tuple[Tuple[int], Tuple[str]]:
    """Return the details for the poetry form in poetry_forms_file that
    starts at the first lines[0] and ends at the lines[1].
    >>> import os
    >>> small_pf = open(os.path.dirname(__file__) +\
        '/../data/poetry_forms_small.txt')
    >>> poetry_form_details = get_poetry_form_details(small_pf, [1, 3])
    >>> small_pf.close()
    >>> poetry_form_details == ((5, 7, 5), ('*', '*', '*'))
    True
    """
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
    return tuple([tuple(syllable_counts), tuple(rhyming_part)])


# ===================== Required Functions =================================

def read_pronunciation(pronunciation_file: TextIO) -> PRONUNCIATION_DICT:
    """Return the pronunciation dictionary formed from reading
    pronunciation_file, an open file that is in the format of the CMU
    Pronouncing Dictionary.

    >>> import os
    >>> small_pd = open(os.path.dirname(__file__) +\
         '/../data/pronunciation_dictionary_small.txt')
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

    >>> import os
    >>> small_pf = open(os.path.dirname(__file__) +\
         '/../data/poetry_forms_small.txt')
    >>> name_to_description = read_poetry_form_descriptions(small_pf)
    >>> small_pf.close()
    >>> name_to_description == {
    ...     'Haiku': ((5, 7, 5), ('*', '*', '*')),
    ...     'Limerick': ((8, 8, 5, 5, 8), ('A', 'A', 'B', 'B', 'A'))}
    True
    """
    poetry_forms = {}
    poetry_form_names = get_poetry_form_names(poetry_forms_file)
    for name in poetry_form_names:
        lines = get_poetry_form_name_lines(poetry_forms_file, name)
        poetry_forms[name] = get_poetry_form_details(poetry_forms_file, lines)
    return poetry_forms


if __name__ == '__main__':
    import doctest
    # Uncomment the line below if you prefer to test your examples with doctest
    doctest.testmod()
