def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	import numpy as np
	a = np.array(vectors)
	cov = np.cov(a)
	return cov