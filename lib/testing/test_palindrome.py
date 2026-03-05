
import pytest
from lib.palindrome import longest_palindromic_substring


# ----------------------------
# BASIC TEST CASES
# ----------------------------

def test_babad():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]


def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"


# ----------------------------
# EDGE CASES
# ----------------------------

def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_different_characters():
    assert longest_palindromic_substring("ac") in ["a", "c"]


def test_entire_string_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


# ----------------------------
# LONG STRING CASE
# ----------------------------

def test_long_string():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"


# ----------------------------
# SPECIAL CASES
# ----------------------------

def test_numbers():
    assert longest_palindromic_substring("12321") == "12321"


def test_even_length_palindrome():
    assert longest_palindromic_substring("abccba") == "abccba"


def test_no_long_palindrome():
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]