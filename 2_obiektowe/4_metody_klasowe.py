from abc import ABC


class Zwierze(ABC):
    imie: str
    wiek: int
    x = 0
    y = 0

    @classmethod            # metoda klasowa zachowuje sie tak, jak statyczna - ale jako pierwszy parametr jest do niej
    def nowe_zwierze(cls):  # przypisywana klasa, z użyciem ktorej metoda zostala wykonana
        print(cls)
        return cls()        # najczesciej sluzy jako generator obiektow


class Okon(Zwierze):
    pass


class Lew(Zwierze):
    pass


if __name__ == '__main__':
    zoo = []

    o = Okon.nowe_zwierze() # do metody nowe_zwierze (z klasy Zwierze) przekazujemy klase Okon
                            # dzieki temu, metoda wie, ze zwrocic ma obiekt o klasie Okon
    l = Lew.nowe_zwierze()  # do metody nowe_zwerze przekazujemy klase Lew - dzieki temu utorzymy Lwa, nie Okonia
    zoo.append(o)
    zoo.append(l)

    print(zoo)
