from scipy.optimize import curve_fit
import numpy as np

xVals, yVals = np.loadtxt("data/A-test.txt", unpack=True)


def testFunc(x: float, a: float, b: float):
    return a * x + b * x**2


opt, cov = curve_fit(testFunc, xVals, yVals)

print(1/(2 * 0.7071067811865476**2))

from src.generate import SkiJump, Hill
from pathlib import Path

sk = SkiJump.from_json_file("config/A-test.json")

hill = Hill(10, -30)
print(sk.landing(hill))
<<<<<<< HEAD

def vec(v, alpha):
    v_vec = np.array([v *np.cos(alpha), v * np.sin(alpha)])
    return v_vec
=======
>>>>>>> refs/remotes/origin/main
