class NegativeNumber(Exception):    # wlasny wyjatek musi dziedziczyc po klasie Exception
    pass


def dodaj_liczy_dodatnie(a, b):
    if a < 0 or b < 0:              # jezeli liczby nie spelniaja warunkow...
        raise NegativeNumber        # wyrzuc wyjatek z uzyciem slowa kluczowego raise
    return a + b                    # w przeciwnym wypadku zwracamy sume


if __name__ == '__main__':
    try:
        print(dodaj_liczy_dodatnie(9, -11))
    except NegativeNumber:          # prawidłowa obsługa wyjątku
        print('ta metoda nie obsluguje dodawania liczb ujemnych')

    print(dodaj_liczy_dodatnie(4, 5))

    print(dodaj_liczy_dodatnie(-9, 8))  # brak obsługi wyjątku powoduje zatrzymanie programu i wypisanie domyślnego
                                        # komunikatu o błędzie
