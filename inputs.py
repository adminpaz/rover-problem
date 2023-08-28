from simulation import IInput


class DummyInput(IInput):

    def __init__(self, commands: list) -> None:
        self.commands = commands

    def read(self) -> list:
        return self.commands


class FileInput(IInput):

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> list:
        with open(self.file_path, 'r') as f:
            output = f.read().split('\n')
        return output
