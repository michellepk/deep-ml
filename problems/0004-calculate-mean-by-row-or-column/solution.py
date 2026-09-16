import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	a = np.array(matrix)
	if mode == 'column':
		means = a.mean(axis=0)
	else:
		means = a.mean(axis=1)
	return means