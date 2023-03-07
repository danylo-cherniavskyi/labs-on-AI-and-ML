import numpy as np

def randomize_matrix_01(n: int, m: int) -> np.ndarray:
    '''n - amount of columns, m - amount of rows'''
    return np.random.rand(m, n)

def randomize_matrix_int10(n: int, m: int) -> np.ndarray:
    '''n - amount of columns, m - amount of rows'''
    return np.random.randint(-10, 11, (m, n))

def randomize_matrix_int0_20(n: int, m: int) -> np.ndarray:
    '''n - amount of columns, m - amount of rows'''
    return np.random.randint(0, 21, (m, n))

def randomize_matrix_10(n: int, m: int) -> np.ndarray:
    '''n - amount of columns, m - amount of rows'''
    return np.random.uniform(-10, 10, (m, n))

def swap_rows(matrix: np.ndarray) -> np.ndarray:
    max_value_row_idx = matrix.max(1).argmax()
    min_value_row_idx = matrix.min(1).argmin()

    new_matrix = matrix.copy()

    max_value_row = new_matrix[max_value_row_idx].copy()
    min_value_row = new_matrix[min_value_row_idx].copy()

    new_matrix[max_value_row_idx] = min_value_row
    new_matrix[min_value_row_idx] = max_value_row

    return new_matrix