class Szesciennie:      # generujemy kolejne szesciany liczb
    def __init__(self, start=0, stop=None):
        self.number = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self): # metoda __next__ zwraca kolejne elementy
        n = self.number ** 3
        self.number += 1
        if self.stop is not None and self.number > self.stop:
            raise StopIteration()   # gdy dojdziemy do konca, rzucamy wyjatek StopIteration - for zatrzyma dzialanie
        return n


for i in Szesciennie(0, 12):
    print(i)
