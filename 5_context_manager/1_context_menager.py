class MyCM:
    def __init__(self, filename):
        self.name = filename

    def __enter__(self):            # metoda __enter__ wywolywana jest w momencie wchodzenia do bloku with
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):  # metoda __exit__ wywolywana na koniec bloku lub w momencie
                                    # wystapienia wyjatku. Powinna zamykac wszystkie zasoby
        return self.file.close()


from contextlib import contextmanager

@contextmanager                     # CM mozemy rowniez stworzyc z uzyciem dekoratora @contextmanager, definiujac
def open_file(name):                # funkcje, ktora zawiera slowo kluczowe yield
    f = open(name, 'w')
    yield f                         # slowo yield "pauzuje" wykonanie funkcji, do momentu zamkniecia bloku with
    f.close()


with MyCM("my_file_cm.txt") as f:
    f.write("Witamson z context managera w postaci klasy")

with open_file("my_file_cm_as_f.txt") as f:
    f.write("Witamson z context managera w postaci funkcji")
