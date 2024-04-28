# pip install pytest
from yandex_testing_lesson import is_under_queen_attack
import pytest


def test_not_correct_type_int():
    with pytest.raises(TypeError):
        is_under_queen_attack(12, 'a1')


def test_not_correct_type_list():
    with pytest.raises(TypeError):
        is_under_queen_attack(['a', '1'], 'a1')


def test_not_correct_valuer():
    with pytest.raises(ValueError):
        is_under_queen_attack('abc', 'a1')


def test_not_correct_valuer_num():
    with pytest.raises(ValueError):
        is_under_queen_attack('a9', 'a7')


def test_not_correct_book():
    with pytest.raises(ValueError):
        is_under_queen_attack('z7', 'a7')


def test_not_correct_place():
    with pytest.raises(ValueError):
        is_under_queen_attack('6a', 'a6')


def test_wrong_digit_queen():
    with pytest.raises(ValueError):
        is_under_queen_attack('a3', 'a0')


def test_wrong_length():
    with pytest.raises(ValueError):
        is_under_queen_attack('f8b7', 'd7')


def test_value():
    assert is_under_queen_attack('a1', 'd4')
    assert is_under_queen_attack('a1', 'c3')
    assert is_under_queen_attack('a1', 'b1')
    assert not is_under_queen_attack('h7', 'a2')
    assert not (is_under_queen_attack('a1', 'e4'))
