from logic.command_interpreter import CommandInterpreter
from user_interface.ui import UI


class Main:
    def __init__(self):
        self.ui = UI()
        self.ci = CommandInterpreter()

    def run(self):
        self.ui.say_hello()

        while True:
            user_command = self.ui.user_input()
            self.ci.interpret(user_command)
