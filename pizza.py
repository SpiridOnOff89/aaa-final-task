class Pizza:

    sizes = ['L', 'XL']

    def __init__(self, name: str, ingredients: str, size='L'):
        if size not in self.sizes:
            raise ValueError(f'Возможные размеры: {"/".join(self.sizes)}')
        self.name = name
        self.size = size
        self.ingredients = ingredients

    def dict(self) -> str:
        return '{:<11}: {:<50}'.format(self.name, ", ".join(self.ingredients))

    def __eq__(self, other: 'Pizza') -> bool:
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
