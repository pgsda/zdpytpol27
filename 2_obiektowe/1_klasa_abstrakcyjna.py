import abc


class Instrument(abc.ABC):          # klasa abstrakcyjna Instrument dziedziczy po ABC z pakietu abc
    def __init__(self, glosnosc):
        self.glosnosc = glosnosc

    @abc.abstractmethod             # metoda abstrakcyjna graj - sama nie ma implementacji, bo każdy instr. gra inaczej
    def graj(self):
        pass


class Gitara(Instrument):           # klasa Gitara dziedziczy po interfejsie Instrument
    def graj(self):                 # musi implementowac metode graj
        if self.glosnosc == 0:
            print()
            return
        if self.glosnosc == 1:
            print("brzdek brzdek brzdek")
            return
        print("BRZDEK BRZDEK BRZDEK")


class Skrzypce(Instrument):
    def graj(self):                 # musi implementowac metode graj, ale robi to inaczej niz gitara
        print(f"{self.glosnosc} skrzyp skrzyp")


class Beben(Instrument):
    def graj(self):                 # musi implementowac metode graj, ale robi to inaczej niz gitara i skrzypce
        if self.glosnosc > 3:
            print("BUM BUM BUM BUM")
            return
        print("bum bum bum")


if __name__ == '__main__':
    orkiestra = []
    orkiestra.append(Skrzypce(1))
    orkiestra.append(Beben(4))
    orkiestra.append(Gitara(2))
    orkiestra.append(Skrzypce(2))
    orkiestra.append(Beben(2))
    orkiestra.append(Gitara(0))
    orkiestra.append(Gitara(1))

    for instrument in orkiestra:
        instrument.graj()           # dzieki temu, ze wiemy, ze wszystkie instrumenty implementuja interfejs Instrument
                                    # jestesmy pewni, ze mozemy na nich wywolac metode graj - mimo, iz dziala ona
                                    # za kazdym razem inaczej
