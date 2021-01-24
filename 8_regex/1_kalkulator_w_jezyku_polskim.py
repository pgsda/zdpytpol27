import re


operacje = {                        # dzieki takiemu rozwiazaniu unikamy ifologii w glownej czesci
    'dodaj': lambda a, b: a + b,    # jak i definiowania wielu malych funkcji
    'odejmij': lambda a, b: b - a,
    'podziel': lambda a, b: a / b,
    'pomnoz': lambda a, b: a * b,
    'poteguj': lambda a, b: a ** b,
}


if __name__ == "__main__":
    while True:                             # nieskonczona petla pozwala na wpisywanie wielu polecen
        text1 = input('podaj polecenie: ')  # czekamy na polecenie uzytkownika
        if text1.lower() == 'exit':         # komenda exit powoduje zakonczenie dzialania programu
            break

        pattern = r"^(\w+) (\d+) (\w+) (\d+)$"  # pattern, do jakiego bedziemy dopasowywac str od uzytkownika

        match = re.search(pattern, text1)   # sprawdz dopasowanie

        if match is not None:               # jezeli znaleziono dopasowanie
            command = match.group(1)        # string z komenda
            a = int(match.group(2))         # pierwsza liczba (do int)
            b = int(match.group(4))         # 2 liczba (do int)
        else:
            print('Wprowadzono nieprawidlowe dane')
            continue                        # jezeli nastapil blad w poleceniu przechodzimy do nastepnego obiegu while

        try:
            print(operacje[command](a, b))  # probujemy wywolac funkcje ze slownika pod kluczem odpowiadajacemu operacji
        except KeyError:                    # jezeli brak klucza w slowniku (np. uzytkownik wpisal "modulo" albo "dsasw"
            print('Nie rozpoznano operacji')
            continue                        # wyswietlamy komunikat i przechodzimy do kolejnego obiegu while
