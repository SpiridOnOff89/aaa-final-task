from typing import Callable


class Seq:
    def __init__(self, sequence: list):
        self.sequence = sequence

    def filter(self, filter_func: Callable) -> Callable:
        """Сохраняет фильтрующую функцию в качестве переменной класса."""
        self.filter_func = filter_func
        return self

    def map(self, transform_func: Callable) -> Callable:
        """
        Сохраняет трансформирующую функцию
        в качестве переменной класса.
        """
        self.transform_func = transform_func
        return self

    def take(self, number: int) -> list:
        """
        Возвращает необходимое количество
        отфильтрованных и трансформированных элементов.
        """
        self.sequence_filtered = []
        for i in range(len(self.sequence)):
            if self.filter_func(self.sequence[i]):
                self.sequence_filtered.append(self.sequence[i])
            if len(self.sequence_filtered) == number:
                break
        self.sequence_transformed = [self.transform_func(elem) for elem in self.sequence_filtered]
        return self.sequence_transformed


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(3)
    assert res == [12, 14]
    print(res)