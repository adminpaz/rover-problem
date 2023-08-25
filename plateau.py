
import numpy as np


class OutOfPlateauError(Exception):
    """Exception when some of the rovers access to a forbidden place"""
    pass


class CollisionError(Exception):
    """Exception when some of the rovers try to access to some place
    where another rover is already possitioned"""
    pass


class IPlateau():

    def __init__(self):
        pass

    def take_place(self):
        pass

    def release_place(self):
        pass


class SquaredPlateau(IPlateau):  # Observer

    def __init__(self, x_max: int, y_max: int):
        self.x_max = x_max
        self.y_max = y_max
        # Initialize all positions
        self.positions = np.zeros((self.x_max + 1, self.y_max + 1),
                                  dtype='bool')

    def take_place(self, x, y) -> None:
        try:
            if not self.positions[x, y]:
                self.positions[x, y] = True
            else:
                raise CollisionError()
        except IndexError:
            raise OutOfPlateauError()

    def release_place(self, x, y) -> None:
        self.positions[x, y] = 0
