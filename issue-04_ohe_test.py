from typing import List, Tuple
import pytest
from one_hot_encoder import fit_transform

def test_countries():
    assert fit_transform(['Russia', 'USA', 'France', 'USA', 'Italy']) == [('Russia', [0, 0, 0, 1]),
                                                                          ('USA', [0, 0, 1, 0]),
                                                                          ('France', [0, 1, 0, 0]),
                                                                          ('USA', [0, 0, 1, 0]),
                                                                          ('Italy', [1, 0, 0, 0])]


def test_numbers():
    assert fit_transform([1, 2, 3, 4, 2, 3]) == [(1, [0, 0, 0, 1]),
                                                 (2, [0, 0, 1, 0]),
                                                 (3, [0, 1, 0, 0]),
                                                 (4, [1, 0, 0, 0]),
                                                 (2, [0, 0, 1, 0])]


def test_no_args_error():
    with pytest.raises(TypeError):
        fit_transform()


def test_empty_list():
    assert fit_transform([]) == []
