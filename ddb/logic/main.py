from logic.command_interpreter import CommandInterpreter
from model.files_handling import FilesHandling
from user_interface.ui import UI
from utils.exceptions import InvalidCommand


class Main:
    def __init__(self):
        self.ui = UI()
        self.ci = CommandInterpreter()
        self.fh = FilesHandling()

    def run(self):
        self.ui.say_hello()

        while True:
            user_command = self.ui.user_input()
            try:
                command, cols, vals, doc = self.ci.interpret(user_command)
            except InvalidCommand:
                self.ui.error()
                continue

            if command == 'create':
                self.fh.write(doc, ','.join(cols))
            if command == 'add':
                self.fh.write(doc, ','.join(vals))
