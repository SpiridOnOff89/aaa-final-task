import random
from typing import Callable
from functools import wraps
from pizza import Pizza


def log(text: str) -> Callable:
    """Принимает функцию выводит время ее выполнения"""
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(pizza):
            print(f'{text.format(random.randint(1, 20))} пиццу {pizza.name}.')
        return inner_wrapper
    return outer_wrapper


@log('Приготовили за {} минут')
def _bake(pizza: 'Pizza') -> None:
    """Пицца приготовлена!"""
    print(f'Готовится пицца {pizza.name}!')


@log('Доставили за {} минут')
def _delivery(pizza: 'Pizza') -> None:
    """Доставляет пиццу"""
    print(f'Пицца {pizza.name} доставляется!')
