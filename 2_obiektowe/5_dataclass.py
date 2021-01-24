from dataclasses import dataclass


@dataclass      # udekorowana klasa otrzymuje konstruktor oraz metody __eq__ i __repr__, wiec jej zapis jest skrocony
class User:
    first_name: str
    last_name: str
    nick: str


class User_bez_dataclass:   # ta klasa zachowuje sie tak samo jak klasa User, ale jej implementacja jest duzo dluzsza
    def __init__(self, first_name, last_name, nick):
        self.first_name = first_name
        self.last_name = last_name
        self.nick = nick

    def __repr__(self) -> str:
        return f"User_bez_dataclass(first_name='{self.first_name}', last_name='{self.last_name}', nick='{self.nick}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, User_bez_dataclass) and \
               (self.first_name, self.last_name, self.nick) == (other.first_name, other.last_name, other.nick)


if __name__ == '__main__':
    u1 = User('Piotr', 'Gie', 'grabe')
    u2 = User('Piotr', 'Gie', 'grabe')
    print(u1, u2)
    print(u1 == u2)
    print('-'*20)

    u1 = User_bez_dataclass('Piotr', 'Gie', 'grabe')
    u2 = User_bez_dataclass('Piotr', 'Gie', 'grabe')
    print(u1, u2)
    print(u1 == u2)
