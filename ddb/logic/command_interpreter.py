import re

from utils.exceptions import InvalidCommand


class CommandInterpreter:
    def interpret(self, user_command):
        # ADD (1, Maria, Nowak, 22, K) TO uczestnicy
        # SELECT (imie) FROM uczestnicy
        # DELETE FROM uczestnicy WHERE plec=M
        # CREATE DOCUMENT zoo    (id, gatunek, np, liczba_osobnikow)

        create_pattern = r'\s*CREATE\s+DOCUMENT\s+(\w+)\s+\(([\w\s,]+)\)\s*'
        add_pattern = r'\s*ADD\s+\(([\w\s,]+)\)\s+TO\s+(\w+)\s*'

        found_create_pattern = re.search(create_pattern, user_command, re.I)
        found_add_pattern = re.search(add_pattern, user_command, re.I)

        if found_create_pattern is not None:
            return 'create', found_create_pattern.group(2).replace(' ', '').split(','), None, found_create_pattern.group(1)

        if found_add_pattern is not None:
            return 'add', None, found_add_pattern.group(1).replace(' ', '').split(','), found_add_pattern.group(2)

        raise InvalidCommand

        # (command,                     columns,                 values,             document)
        # create/add/select/delete      ['id', 'gatunek'...]     ['1', 'Maria'...]   zoo/uczestnicy
