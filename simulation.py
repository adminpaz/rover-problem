from abc import ABCMeta
from abc import abstractmethod

from plateau import SquaredPlateau, CollisionError, OutOfPlateauError
from rover import Rover


class ForbiddenCommand(Exception):
    """Exception when a not available command is received"""
    pass


class IInput(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'read') and
            callable(subclass.read)
        )

    @abstractmethod
    def read(self) -> list:
        raise NotImplementedError


class IOutput(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'write') and
            callable(subclass.write)
        )

    @abstractmethod
    def write(self) -> None:
        raise NotImplementedError


class Simulation():

    def __init__(self, input_obj: IInput = None,
                 output: IOutput = None) -> None:
        self._input = input_obj
        self._output = output

    def read_input(self) -> list:
        return self._input.read()

    def write_output(self, cmds: list) -> None:
        return self._output.send(cmds)


class SquaredSequentialSurfaceSimulation(Simulation):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self._plateau = None
        self._rover = Rover()

    def place_new_rover(self, cmd: str) -> None:
        x, y, direction = cmd.split(" ")
        self._rover.land(int(x), int(y), direction, self._plateau)

    def move_rover(self, cmds: list) -> None:
        for cmd in cmds.split(" "):
            if cmd == "M":
                self._rover.move()
            elif cmd == "L":
                self._rover.turn_left()
            elif cmd == "R":
                self._rover.turn_right()
            else:
                raise ForbiddenCommand()

    def calculate(self, cmd_lines: list) -> list:
        # Initialize plateau
        x_max, y_max = map(int, cmd_lines[0].split(" "))
        self._plateau = SquaredPlateau(x_max, y_max)

        rovers_number = int((len(cmd_lines)-1)/2)
        results = []
        for rover_line_id in range(1, rovers_number*2, 2):
            try:
                self.place_new_rover(cmd_lines[rover_line_id])
                self.move_rover(cmd_lines[rover_line_id + 1])
                results.append(str(self._rover))
            except CollisionError:
                results.append("Collision!")
            except OutOfPlateauError:
                results.append("Out of Plateau!")
        return results

    def run(self) -> None:
        cmds = self.read_input()
        result = self.calculate(cmds)
        self.write_output(result)
        return
