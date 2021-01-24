if __name__ == "__main__":
    print("uzytkowniku kochany, podaj liczby do dzielenia")
    a = int(input("liczba a: "))
    b = int(input("liczba b: "))

    print("a / b = ")
    try:                            # probujemy wykonac kod
        wynik = a / b
        print(wynik)
        print("bardzo dobrze")
    except ZeroDivisionError as e:  # jesli sie nie uda, obslugujemy wyjatek
        print("nigdy nie dziel przez zero")
        print("co sie stanelosie")
    finally:                        # zamykamy wszystkie zasoby - ten kod wykona sie zawsze!
        print("to sa operacje, ktore wykonaja sie bez wzgledu na to" +
              " czy wyjatek sie pojawil, czy nie")

    print("a + b = ")
    print(int(a) + int(b))
