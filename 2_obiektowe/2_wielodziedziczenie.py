class A:
    def jeden(self):
        print('A1')

    def dwa(self):
        print('A2')


class B:
    def jeden(self):
        print('B1')

    def dwa(self):
        print('B2')

    def trzy(self):
        print('B3')


class C(A):
    def trzy(self):
        print('C3')


class AB(A, B):
    pass


class BA(B, A):
    pass


class BC(B, C):
    pass


class CB(C, B):
    pass


if __name__ == '__main__':
    print('AB:')
    ab = AB()
    ab.jeden()      # dziedziczymy od lewej wglab, wiec metoda jeden z klasy A
    ab.dwa()        # metoda dwa z klasy A
    ab.trzy()       # metody 3 nie znaleziono w klasie A, wiec dziedziczymy po klasie B
    print('-'*20)

    print('BA:')
    ba = BA()
    ba.jeden()      # dziedziczymy od lewej wglab, wiec metoda jeden z klasy B
    ba.dwa()        # metoda dwa z klasy B
    ba.trzy()       # metoda trzy z klasy B
    print('-' * 20)

    print('BC:')
    bc = BC()
    bc.jeden()      # dziedziczymy od lewej wglab, wiec metoda jeden z klasy B
    bc.dwa()        # metoda dwa z klasy B
    bc.trzy()       # metoda trzy z klasy B
    print('-' * 20)

    print('CB:')
    cb = CB()
    cb.jeden()      # dziedziczymy od lewej wglab, wiec metoda jeden z klasy A
    cb.dwa()        # metoda dwa z klasy A
    cb.trzy()       # metody 3 z klasy C
    print('-' * 20)
