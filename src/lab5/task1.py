import numpy as np

def randomize_array_01(size: int) -> np.ndarray:
    return np.random.rand(size)

def randomize_array_int10(size: int) -> np.ndarray:
    return np.random.randint(-10, 11, size)

def randomize_array_int0_50(size: int) -> np.ndarray:
    return np.random.randint(0, 51, size)

def shift(array: np.ndarray, k: int) -> np.ndarray:
    bounded_k = k % len(array)

    [first_k, rest] = np.split(array, [bounded_k])
    rest.append(first_k)