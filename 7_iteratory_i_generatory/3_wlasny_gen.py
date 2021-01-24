import random


def random_numbers(x):
    for wi in range(x):
        print('przed')
        yield random.random()   # pauza i zwroc losowa liczbe
        print('po')


def szesciany(x):
    for wi in range(x):
        yield wi ** 3   # pauza i zwroc szescian


for i in random_numbers(10):
    print(i)

print('-'*20)

for i in szesciany(10):
    print(i)
