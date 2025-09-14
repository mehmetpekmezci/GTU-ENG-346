import numpy as np
from numpy.linalg import norm

A = np.array([[2, 1, 2], [3, 2, 9], [-1, 2, -3]])
B = np.array([3, 4, 2])

cosine = np.dot(A, B) / (norm(A, axis=1) * norm(B))
print("Cosine Similarity:", cosine)
