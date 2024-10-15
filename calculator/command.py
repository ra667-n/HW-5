class Command:
    def execute(self, a, b):
        pass

class AddCommand(Command):
    def execute(self, a, b):
        return a + b

class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

class MultiplyCommand(Command):
    def execute(self, a, b):
        return a * b

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError:("Cannot divide by zero")
        return a/b
