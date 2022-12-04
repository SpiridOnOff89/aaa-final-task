import click
import random
from typing import Callable, Type
from functools import wraps


class Pizza:

    sizes = ['L', 'XL']

    def __init__(self, name, ingredients, size='L'):
        if size not in self.sizes:
            raise ValueError(f'Возможные размеры: {"/".join(self.sizes)}')
        self.name = name
        self.size = size
        self.ingredients = ingredients

    def dict(self) -> str:
        return f'{self.name}: {", ".join(self.ingredients)}'

    def __eq__(self, other) -> bool:
        return (self.name == other.name) \
               and (self.ingredients == other.ingredients)


margharita = Pizza(name='Margharita',
                   ingredients=[
                       'tomato sauce',
                       'mozzarella',
                       'tomatoes'
                   ]
                   )
pepperoni = Pizza(name='Pepperoni',
                  ingredients=[
                      'tomato sauce',
                      'mozzarella',
                      'pepperoni'
                  ]
                  )
hawaiian = Pizza(name='Hawaiian',
                 ingredients=[
                     'tomato sauce',
                     'mozzarella',
                     'chicken',
                     'pineapples'
                 ]
                 )
all_pizza = [margharita, pepperoni, hawaiian]


def log(text: str) -> Callable:
    """Принимает функцию выводит время ее выполнения"""
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(pizza):
            print(f'{text.format(random.randint(1, 20))} пиццу {pizza.name}.')
        return inner_wrapper
    return outer_wrapper


@log('Приготовили за {} минут')
def _bake(pizza: Type[Pizza]) -> None:
    """Пицца приготовлена!"""
    print(f'Готовится пицца {pizza.name}!')


@log('Доставили за {} минут')
def _delivery(pizza: Type[Pizza]) -> None:
    """Доставляет пиццу"""
    print(f'Пицца {pizza.name} доставляется!')


@click.group()
def cli():
    pass


@cli.command
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    pizza = list(filter(lambda x: x.name.lower() == pizza, all_pizza))[0]
    _bake(pizza)
    if delivery:
        _delivery(pizza)


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for pizza in all_pizza:
        print(pizza.dict())


if __name__ == '__main__':
    cli()
