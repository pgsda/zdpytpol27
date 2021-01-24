import time


def how_long(func):                 # dekorator stoper
    def wrapper(*args, **kwargs):   # definiujemy wrapper
        t1 = time.time()            # startujemy stoper
        s = func(*args, **kwargs)   # wywolujemy funkcje dekorowana, przechwytujemy wynik
        t2 = time.time()            # stopujemy stoper
        print(f"funkcja dzialala: {t2 - t1}")   # wypisujemy czas dzialania
        return s                    # zwracamy przechwycony wynik
    return wrapper                  # dekorator zwraca wrapper, ktory zostanie wywolany zamiast funkcji udekorowanej


@how_long                           # dekorujemy naszym wrapperem
def owinieta_funkcja_hw(imie_swiata):
    print("bardzo ciezkie operacje dla swiata")
    time.sleep(2)
    return "hello world " + imie_swiata


s = owinieta_funkcja_hw("EEEEE MAKARENA")   # wywolanie nie rozni sie, od wywolania nieudekorowanej funkcji
print(s)
