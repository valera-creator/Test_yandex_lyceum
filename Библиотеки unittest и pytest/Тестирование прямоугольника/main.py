# pip install pytest
from yandex_testing_lesson import Rectangle
import pytest


def test_not_num_type():
    with pytest.raises(TypeError):
        rect = Rectangle('a', 'b')


def test_list():
    with pytest.raises(TypeError):
        rect = Rectangle([1], 2)


def test_book_and_num():
    with pytest.raises(TypeError):
        rect = Rectangle('a', 2)


def test_negative_num():
    with pytest.raises(ValueError):
        rect = Rectangle(-1, -2)


def test_negative_num_1():
    with pytest.raises(ValueError):
        rect = Rectangle(-1, 2)


def test_negative_float_1():
    with pytest.raises(ValueError):
        rect = Rectangle(-1.5, 2)


def test_work():
    rect = Rectangle(5, 5)
    assert rect.get_area() == 25
    assert rect.get_perimeter() == 20
