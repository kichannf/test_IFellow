from random import random, randint


def gen_and_give():
    """функция генерирует массив случайного размера с цифрами [0, 1].
    Выоводит min, max, avg массива"""

    arr = [round(random(), 3) for i in range(randint(3, 100))]
    return print(
        f'Max: {max(arr)}, Min: {min(arr)}, '
        f'Avg: {round((sum(arr) / len(arr)), 5)}'
    )


gen_and_give()
