from copy import copy, deepcopy


def deep_cpy(d):
    nd = deepcopy(d)
    nd['a'] = 'zmiana_a'
    nd['c'][1] = 'zmienilem'


def just_cpy(d):
    nd = copy(d)
    nd['a'] = 'zmiana_a'
    nd['c'][1] = 'zmienilem'


def no_cpy(d):
    d['a'] = 'zmiana_a'
    d['c'][1] = 'zmienilem'


if __name__ == '__main__':
    x = {'a': 'A', 'b': 'B', 'c': {1: 1, 2: 2}}
    print('x:        ', x)
    no_cpy(x)       # obiekt przekazany przez referencje zostanie zmieniony
    print('no copy:  ', x)

    print('-'*20)

    x = {'a': 'A', 'b': 'B', 'c': {1: 1, 2: 2}}
    print('x:        ', x)
    just_cpy(x)     # obiekt jest kopiowany z uzyciem copy - pierwsza warstwa zostanie skopiowana, natomiast obiekt 'c'
                    # nie jest kopiowany. obiekt pod kluczem 'c' zmieni sie
    print('copy:     ', x)

    print('-'*20)

    x = {'a': 'A', 'b': 'B', 'c': {1: 1, 2: 2}}
    print('x:        ', x)
    deep_cpy(x)     # deep copy powoduje, ze funkcja bedzie pracowac na kompletnej kopii - obiekt x nie ulegnie zmianie
    print('deep cpy: ', x)
