import json


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
    'e': {"123": None}
}
go = Cla()

# zrzucanie do jsona
for key, value in slownik.items():
    with open(f'jsonowane/{key}.json', 'w') as f:
        json.dump(value, f)

# zrzucanie obiektu - obejście z __dict__
with open(f'jsonowane/go.json', 'w') as f:
    json.dump(go.__dict__, f)

# odjosonowywanie, sprawdzenie typów
for plik in slownik.keys():
    with open(f'jsonowane/{plik}.json', 'r') as f:
        variable = json.load(f)
    print(variable)
    print(type(variable))
    print()

# obiekt
with open(f'jsonowane/go.json', 'r') as f:
    json.load(f)
print(variable)
print(type(variable))
print()
