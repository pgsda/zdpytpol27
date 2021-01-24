class Obliczenia:
    @staticmethod           # metoda statyczna nie dokonuje zman na obiekcie, bo dziala bez powolywania obiektu!
    def dodawanie(a, b):
        return a + b

    @staticmethod
    def odejmowanie(a, b):
        return Obliczenia.dodawanie(a, b * -1)

    @staticmethod
    def mnozenie(a, b):
        return a * b


if __name__ == '__main__':
    print(Obliczenia.mnozenie(3, 4))    # nie tworzymy obiektow, a jedynie wywolujemy metody statyczne jak funkcje
    print(Obliczenia.odejmowanie(7, 12))
    print(Obliczenia.dodawanie(95, 5))
