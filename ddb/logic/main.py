from logic.command_interpreter import CommandInterpreter
from model.files_handling import FilesHandling
from user_interface.ui import UI


class Main:
    def __init__(self):
        self.ui = UI()
        self.ci = CommandInterpreter()
        self.fh = FilesHandling()

    def run(self):
        self.ui.say_hello()

        while True:
            user_command = self.ui.user_input()
            command, cols, vals, doc = self.ci.interpret(user_command)
            if command == 'create':
                self.fh.create_and_write(doc, ','.join(cols))
