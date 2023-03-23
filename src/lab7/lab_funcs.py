import numpy as np

interval = {
    "start": 1.0,
    "end": 4.0
}

def func(x: float) -> float:
    factor1 = np.sin(1 / x)
    factor2 = np.cos(x ** 2 + 1 / x)
    return 5 * factor1 * factor2 ** 2