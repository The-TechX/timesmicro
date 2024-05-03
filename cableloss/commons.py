import numpy as np


def CL(frequency, distance) -> float:
    k1 = 0.122290
    k2 = 0.000260
    return (((k1 * np.sqrt(frequency)) + (k2 * frequency))*distance)/100
