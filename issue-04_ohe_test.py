from typing import List, Tuple
import pytest
from one_hot_encoder import fit_transform

def test_countries():
    actual = fit_transform(['Russia', 'USA', 'France', 'USA', 'Italy'])
    expected = [('Russia', [0, 0, 0, 1]),
                ('USA', [0, 0, 1, 0]),
                ('France', [0, 1, 0, 0]),
                ('USA', [0, 0, 1, 0]),
                ('Italy', [1, 0, 0, 0])]
    assert actual == expected


def test_numbers():
    actual = fit_transform([1, 2, 3, 4, 2, 3])
    expected = [(1, [0, 0, 0, 1]),
                (2, [0, 0, 1, 0]),
                (3, [0, 1, 0, 0]),
                (4, [1, 0, 0, 0]),
                (2, [0, 0, 1, 0])]
    assert actual == expected


def test_no_args_error():
    with pytest.raises(TypeError):
        fit_transform()


def test_empty_list():
    assert fit_transform([]) == []
