import pickle


def fun():
    return 123


class Cla:
    def __init__(self):
        self.imie = "imie"
        self.nazwisko = "nazwisko"

    def m(self):
        pass


slownik = {
    'a': 903812,
    'b': (2, 3, 4),
    'c': "1234567890",
    'd': [1, 2, 3, 4, 5],
    'e': {"123": "456"},
    'f': fun,
    'gc': Cla,
    'go': Cla()
}

# piklowanie
for key, value in slownik.items():
    with open(f'zapiklowane/{key}.pickled', 'wb') as f:
        pickle.dump(value, f)

# odpiklowanie, sprawdzenie typów
for plik in slownik.keys():
    with open(f'zapiklowane/{plik}.pickled', 'rb') as f:
        variable = pickle.load(f)
    print(variable)
    print(type(variable))
    print()
