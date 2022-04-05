"""CSC108H1: Assignment 3: Poetry Form Checker

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

DO NOT MAKE CHANGES TO THIS FILE.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108 Teaching Team.
"""

import sys
import subprocess
import importlib
from typing import Tuple, Optional

PYTHON_TA_VERSION = '2.2.0'


def attempt_python_ta_installation(version: int) -> int:
    """Attempt installation of PythonTA.
    Returns the next version to attempt if there is one, or -1 if there
    are no other versions after version.
    """
    executables = ['python3.9', sys.executable]
    attempts = [f'-m pip install python-ta=={PYTHON_TA_VERSION}',
                # Turn off SSL verification (certificate errors)
                f'-m pip install python-ta=={PYTHON_TA_VERSION} '
                f'config --global http.sslVerify false',
                # Set pypi as a trusted host
                f'-m pip install python_ta=={PYTHON_TA_VERSION} '
                f'--trusted-host pypi.python.org'
                ]

    try:
        # Switch between python3.9 and sys.executable
        executable = executables[version % 2]
        attempt = attempts[version // 2]

        # python3.9 uses Popen, while sys.executable uses check_call
        if executable == 'python3.9' or executable == 'python3.10':
            subprocess.Popen(executable + ' ' + attempt,
                             shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        else:
            subprocess.check_call([executable] + attempt.split(),
                                  stderr=subprocess.DEVNULL,
                                  stdout=subprocess.DEVNULL)
    except:
        pass

    if version < len(attempts) * 2:
        return version + 1

    return -1


def reimport_python_ta() -> Optional['python_ta']:
    """Try to import and return python_ta.
    If unsuccessful, return None"""
    try:
        if 'python_ta' in sys.modules:
            del sys.modules['python_ta']

        import python_ta
        importlib.reload(python_ta)
        return python_ta
    except:
        return None


def python_ta_installed() -> bool:
    """Return True if PythonTA is installed."""
    try:
        python_ta = reimport_python_ta()
        installed_version = python_ta.__version__
        return installed_version == PYTHON_TA_VERSION
    except:
        return False


def install_python_ta():
    """Tries to install PythonTA."""
    if not python_ta_installed():
        print("Installing / Updating the style checker", end='')
    else:
        print("Running style checker...")
        return

    i = 0
    while not python_ta_installed() and i != -1:
        print(".", end='')
        i = attempt_python_ta_installation(i)

    print("")


def run_pyta(filename: str, config_file: str) -> None:
    """Run PYTA with configuration config_file on the file named filename.
    """
    import json
    install_python_ta()

    error_message = '\nCould not install or run the style checker correctly.\n' \
                    'Please try to re-run the checker once more.\n\n' \
                    'If you have already tried to re-run it, please go to office hours\n' \
                    'in order to resolve this. ' \
                    'For now, you may upload your code to MarkUs and run the self-test\n' \
                    'to see the style checker results.'

    python_ta = reimport_python_ta()
    if python_ta:
        try:
            with open(config_file) as cf:
                config_dict = json.loads(cf.read())
                config_dict['output-format'] = 'python_ta.reporters.PlainReporter'

            python_ta.check_all(filename, config=config_dict)
        except:
            print(error_message)
    else:
        print(error_message)


def check(func: callable, args: list,
          expected: type) -> Tuple[bool, object]:
    """Check if func(args) returns a result of type expected.

    Return (True, result-of-call) if the check succeeds.
    Return (False, error-or-failure-message) if anything goes wrong.
    """

    try:
        returned = func(*args)
    except Exception as exn:
        return (False, _error_message(func, args, exn))

    if isinstance(returned, expected):
        return (True, returned)

    return (False, _type_error_message(func, expected, returned))


def _type_error_message(func: callable, expected: type,
                        got: object) -> str:
    """Return an error message for function func returning got, where the
    correct return type is expected.

    """

    return ('{} should return a {}, but returned {}' +
            '.').format(func.__name__, expected.__name__, got)


def _error_message(func: callable, args: list,
                   error: Exception) -> str:
    """Return an error message: func(args) raised an error."""

    return 'The call {}({}) caused an error: {}'.format(
        func.__name__, ','.join(map(str, args)), error)
