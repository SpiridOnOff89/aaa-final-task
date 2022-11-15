from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


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


def test_exception():
    with pytest.raises(TypeError):
        fit_transform()


def test_empty():
    assert fit_transform([]) == []
