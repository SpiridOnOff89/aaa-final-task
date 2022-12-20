import click
from pizza import all_pizza
from pizza_operations import _bake, _delivery


@click.group()
def cli():
    pass


@cli.command
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    pizza_names = list(map(lambda x: x.name, all_pizza))
    while True:
        if pizza.lower().capitalize() not in pizza_names:
            print('Такой пиццы в меню нет. Введите название из списка:')
            print(", ".join(pizza_names))
            pizza = input()
        else:
            break

    # ищу элемент класса Pizza по введенному названию пиццы
    pizza = list(
        filter(
            lambda x: x.name.lower() == pizza.lower(), all_pizza
        )
    )[0]

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
