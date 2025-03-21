from scipy.optimize import curve_fit
import numpy as np

xVals, yVals = np.loadtxt("data/A-test.txt", unpack=True)
def testFunc(x: float, a: float, b:float):
    return a * x + b * x ** 2
opt, cov = curve_fit(testFunc, xVals, yVals)

from src.generate import SkiJump, Hill
from pathlib import Path

sk = SkiJump.from_json_file("config/A-test.json")

hill = Hill(10, -30)
print(sk.landing(hill))