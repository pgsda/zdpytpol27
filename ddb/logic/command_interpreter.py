import re


class CommandInterpreter:
    def interpret(self, user_command):

        # ADD (1, Maria, Nowak, 22, K) TO uczestnicy
        # SELECT (imie) FROM uczestnicy
        # DELETE FROM uczestnicy WHERE plec=M
                         # CREATE DOCUMENT zoo    (id, gatunek, np, liczba_osobnikow)
        create_pattern = r'CREATE DOCUMENT (\w+) \(([\w\s,]+)\)'
        found_pattern = re.search(create_pattern, user_command)

        if found_pattern is not None:
            print(found_pattern)

        # (command,                     columns,                 values,             document)
        # create/add/select/delete      ['id', 'gatunek'...]     ['1', 'Maria'...]   zoo/uczestnicy
