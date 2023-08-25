from plateau import IPlateau


class NotAllowedDirection(Exception):
    """Exception when the direction command is not in the available ones"""
    pass


class Rover():  # Observable

    DIRECTIONS_STR = ["N", "E", "S", "W"]
    VECTOR_DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self):
        pass

    def land(self, x_ini: int, y_ini: int, direction: str, plateau: IPlateau):
        # Attach function
        self._direction = self._str_to_dir(direction)
        self._x = x_ini
        self._y = y_ini
        self._plateau = plateau
        self._plateau.take_place(self._x, self._y)

    def _str_to_dir(self, direction_str: str) -> int:
        for idx, available_dir in enumerate(self.DIRECTIONS_STR):
            if direction_str == available_dir:
                return idx

        raise NotAllowedDirection()

    def turn_right(self) -> None:
        self._direction += 1

    def turn_left(self) -> None:
        self._direction -= 1

    def move(self) -> None:
        dx, dy = self.VECTOR_DIR[self._direction % 4]
        self._plateau.release_place(self._x, self._y)
        self._plateau.take_place(self._x + dx, self._y + dy)
        self._x += dx
        self._y += dy

    def __str__(self):
        direction = self.DIRECTIONS_STR[self._direction % 4]
        return f"{self._x} {self._y} {direction}"
