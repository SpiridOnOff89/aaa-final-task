"""
Написать в функциональном стиле функции get_names и get_object_names
реализующие (x['name'] for x in users) и (x.name for x in users).

Попробуйте сделать максимально переиспользуюемую реализацию:
1) Хотелось бы переиспользовать код, для работы со словарями и объектами
2) Что если нужно будет возвращать не names, а что-то другое?


Помогут:
1) from operator import itemgetter, attrgetter
2) from functools import partial
"""

from dataclasses import dataclass
from operator import itemgetter, attrgetter
from functools import partial
from typing import List, Callable


def get_item(dictionary: dict, key: str) -> str:
    """Возвращает значение из словаря по ключу."""
    return itemgetter(key)(dictionary)


# возвращает значение из словаря по ключу "name"
get_name = partial(get_item, key='name')


def get_names(elems: List[dict]) -> List[str]:
    """Возвращает список из значений переданных словарей по ключу "name"."""
    return (get_name(elem) for elem in elems)


def get_attr(object: Callable, attr: str) -> str:
    """Возвращает атрибут класса."""
    return attrgetter(attr)(object)


# возвращает атрибут "name" класса
get_object_name = partial(get_attr, attr='name')


def get_object_names(users: List[Callable]) -> List[str]:
    """Возвращает список из атрибутов "name" переданных классов."""
    return (get_object_name(user) for user in users)


@dataclass
class User:
    name: str
    age: int


if __name__ == '__main__':
    users_objects = [User(name='Paul', age=28), User(name='Liz', age=18)]
    users = [
        {'name': 'Paul', 'age': 28},
        {'name': 'Liz', 'age': 18},
    ]
    assert list(get_names(users)) == ['Paul', 'Liz']
    assert list(get_object_names(users_objects)) == ['Paul', 'Liz']
    print(list(get_names(users)))
    print(list(get_object_names(users_objects)))
