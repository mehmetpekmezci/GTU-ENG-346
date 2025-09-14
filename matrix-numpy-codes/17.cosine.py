import numpy as np
from numpy.linalg import norm

A = np.array([2, 4])
B = np.array([4, 2])

# compute cosine similarity
cosine = np.dot(A, B) / (norm(A) * norm(B))
print("Cosine Distance:", 1-cosine)

