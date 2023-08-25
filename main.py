from plateau import SquaredPlateau, CollisionError, OutOfPlateauError
from rover import Rover


class ForbiddenCommand(Exception):
    """Exception when a not available command is received"""
    pass

class ISimulation():

    def run(self, cmd_lines: list) -> list:
        pass


class SquaredSequentialSurfaceSimulation(ISimulation):

    def __init__(self):
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

    def run(self, cmd_lines: list) -> list:
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


if __name__ == "__main__":
    sample_input = ["5 5", "1 2 N", "L M L M L M L M M", "3 3 E", "M M R M M R M R R M"]
    result = SquaredSequentialSurfaceSimulation().run(sample_input)
    print(result)
