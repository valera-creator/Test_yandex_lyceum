# pip install pytest
import pytest
from yandex_testing_lesson import count_chars


def test_empty_string():
    assert count_chars('') == {}


def test_usuall_string():
    assert count_chars('aballacA') == {'a': 3, 'l': 2, 'c': 1, 'b': 1, 'A': 1}


def test_not_string_not_iteration():
    with pytest.raises(TypeError):
        count_chars(42)


def test_not_string_iteration():
    with pytest.raises(TypeError):
        count_chars([1, 2, 3])
