"""Contains the necessary tools to generate a dataset."""

import argparse
from dataclasses import dataclass
import pathlib
import numpy as np
from scipy.optimize import curve_fit, fsolve
import json

EARTH_GRAVITY = 1.0  # [a.u.]
"""Acceleration on earth due to gravity."""
# ↑ for simplicity we use arbitrary units every where - how to restore SI units?


@dataclass(frozen=True)
# ↑ this is the `dataclass` decorator, whose documentation can be found
# here: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass .
# Data classes are a convenient way to define a class, which mainly
# just holds some attributes (as is the case here).
# The only method is fully derived from the attributes and the class has no
# additional logic.
class Hill:
    """The hill from which the jumpers fly off.

    .. code::
            ^
            --------------> x
            |
            |     <- offset
            |\
            | \
            |  \
    """

    offset: float
    """Vertical offset of slope - should be negative."""
    slope: float
    """Slope of the hill - should be negative."""

    def y(self, x: float) -> float:
        """Returns shape of the hill."""
        return self.offset + self.slope * x


HILL = Hill(offset=-2.0, slope=-1.0)
"""The present hill."""


@dataclass(frozen=True)
class SkiJump:
    """The true jumping trajectory."""

    v0: float  # [a.u.]
    """Initial velocity."""
    alpha: float  # [rad]
    """Initial angle."""

    def preFactors(self):
        a = np.tan(self.alpha)
        b = - EARTH_GRAVITY / 2 / (np.cos(self.angle)**2 * self.v0**2)
        return [a, b]

    def y(self, x: float) -> float:
        """Return the trajectory."""
        # Work here in Step 1!
<<<<<<< HEAD
        a, b = self.preFactors()
        return a * x + b * x ** 2
=======
        return -2.18130377e-12 * x + -1.00000000e00 * x**2
>>>>>>> refs/remotes/origin/main

    @staticmethod
    # ↑ this is the `staticmethod` decorator, whose documentation can be found
    # here: https://docs.python.org/3/library/functions.html#staticmethod .
    # This makes the method bound to the class _itself_, rather then to a specific
    # object.
    def from_json_file(path: pathlib.Path):
        """Read configuration from JSON file."""
        # Work here in Step 1!
        # Create a `SkiJump` object with the specification given in the file.
        # The `dataclass` decorator adds, e.g., a constructor with keyword arguments,
        # as is used above for creating the `Hill` object.
        f = open(
            path,
        )
        data = json.load(f)
        return SkiJump(data["v0"], data["alpha"])

    def landing(self, hill: Hill) -> float:
        """Returns the intersection of the trajectory and the hill."""

        # Work here in Step 1!
        def checkInter(x):
<<<<<<< HEAD
            return hill.y(x) - self.y(x) # Solve for jump trajectory = hill, or jump trajectory - hill = 0
=======
            return hill.y(x) - self.y(x)

>>>>>>> refs/remotes/origin/main
        return fsolve(checkInter, 1)[0]

    def sample(self, hill: Hill, n: int) -> tuple[np.ndarray, np.ndarray]:
        """Discretize trajectory with `n` points until the landing.

        Parameters
        ----------
            hill :
                Jumping location
            n :
                number of points

        Returns
        -------
            xs :
                x points
            ys :
                y points
        """
        # Work here in Step 3!
        # 1. Compute the landing point
        # 2. Generate `n` equally space x points between the landing point and 0. using
        #    [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy-linspace)
        xs = np.array([])
        # 3. Compute the trajectory for each x point
        ys = np.array([])
        return xs, ys


if __name__ == "__main__":
    # Python provides the argparse library to provide simple command line interfaces.
    # The official tutorial can be found here: https://docs.python.org/3/howto/argparse.html#argparse-tutorial
    # To see it in action just execute this file: `$ python src/generate.py -h` (the `-h` opens immediately the help page)
    parser = argparse.ArgumentParser(
        description="Generate data files from a given configuration."
    )
    parser.add_argument(
        "input", help="Jumping configuration file - should end in .json"
    )
    parser.add_argument("output", help="Target file for output - should end in .txt")
    parser.add_argument("-n", type=int, default=10, help="Number of points")
    args = parser.parse_args()
    # 1. Read the configuration
    my_obj = SkiJump.from_json_file(args.input)
    # 2. Sample
    my_xs, my_ys = my_obj.sample(HILL, args.n)
    # 3. Dump the x points and the y points into the file `args.output` using
    #    [`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy-savetxt).
    #    Make x the first column and y the second column.
