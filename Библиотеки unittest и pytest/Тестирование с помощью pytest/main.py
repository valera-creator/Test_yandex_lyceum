# pip install pytest
from yandex_testing_lesson import reverse
import pytest


def test_empty_string():
    assert reverse('') == ''


def test_one_simvol():
    assert reverse('a') == 'a'


def test_palindrome():
    assert reverse('ALLA') == 'ALLA'


def test_not_palindrome():
    assert reverse('ABC') == 'CBA'


def test_not_string_not_iteration():
    with pytest.raises(TypeError):
        reverse(42)


def test_not_string_iteration():
    with pytest.raises(TypeError):
        reverse([1, 2, 3])
