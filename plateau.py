
import numpy as np
from rover import IPlateau


class OutOfPlateauError(Exception):
    """Exception when some of the rovers access to a forbidden place"""
    pass


class CollisionError(Exception):
    """Exception when some of the rovers try to access to some place
    where another rover is already possitioned"""
    pass


class SquaredPlateau(IPlateau):  # Observer
    """
    Implementation of Plateau with squared shape that implements the interface
    IPlateau. This ensures that can be the observer of rovers objects
    """
    def __init__(self, x_max: int, y_max: int):
        self.x_max = x_max
        self.y_max = y_max
        # Initialize all positions
        self.positions = np.zeros((self.x_max + 1, self.y_max + 1),
                                  dtype='bool')

    def take_place(self, x, y) -> None:
        try:
            if x >= 0 and y >= 0:
                if not self.positions[x, y]:
                    self.positions[x, y] = True
                else:
                    raise CollisionError()
            else:
                raise OutOfPlateauError()
        except IndexError:
            raise OutOfPlateauError()

    def release_place(self, x, y) -> None:
        self.positions[x, y] = 0
