import pytest
from pizza import Pizza, _delivery, _bake, pepperoni
from io import StringIO
import sys


def test_pizza_name():
    actual = Pizza(name='chilli_pepper_pizza',
                   ingredients=['chilli pipper',
                                'mozzarella',
                                'tomatoes']).name
    expected = 'chilli_pepper_pizza'
    assert actual == expected


def test_pizza_ingredients():
    actual = Pizza(name='chilli_pepper_pizza',
                   ingredients=['chilli pipper',
                                'mozzarella',
                                'tomatoes']).ingredients
    expected = ['chilli pipper', 'mozzarella', 'tomatoes']
    assert actual == expected


def test_pizza_no_name_error():
    with pytest.raises(TypeError):
        Pizza(ingredients=['chilli pipper',
                           'mozzarella',
                           'tomatoes'])


def test_pizza_no_ingredients_error():
    with pytest.raises(TypeError):
        Pizza(name='chilli_pepper_pizza')


def test_pizza_eq():
    first_pizza = Pizza(name='chilli_pepper_pizza',
                        ingredients=['chilli pipper',
                                     'mozzarella',
                                     'tomatoes'])
    second_pizza = Pizza(name='chilli_pepper_pizza',
                         ingredients=['chilli pipper',
                                      'mozzarella',
                                      'tomatoes'],
                         size='XL')
    assert first_pizza == second_pizza


def test_pizza_not_eq():
    first_pizza = Pizza(name='chilli_pizza',
                        ingredients=['chilli pipper',
                                     'mozzarella',
                                     'tomatoes'])
    second_pizza = Pizza(name='chilli_pepper_pizza',
                         ingredients=['chilli pipper',
                                      'mozzarella',
                                      'tomatoes'],
                         size='XL')
    assert first_pizza == second_pizza


def test_pizza_wrong_size():
    with pytest.raises(ValueError):
        Pizza(name='chilli_pepper_pizza',
              ingredients=['chilli pipper',
                           'mozzarella',
                           'tomatoes'],
              size='XXL')


def test_delivery():
    original_delivery_func = _delivery.__wrapped__
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    original_delivery_func(pepperoni)
    sys.stdout = sys.__stdout__
    actual = capturedOutput.getvalue()
    expected = 'Пицца Pepperoni доставляется!\n'
    assert actual == expected


def test_bake():
    original_bake_func = _bake.__wrapped__
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    original_bake_func(pepperoni)
    sys.stdout = sys.__stdout__
    actual = capturedOutput.getvalue()
    expected = 'Готовится пицца Pepperoni!\n'
    assert actual == expected
