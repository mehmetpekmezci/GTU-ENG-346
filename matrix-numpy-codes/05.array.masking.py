import numpy as np

print("INITIAL ARRAY")
a = np.arange(15)
print(f"MATRIX DIM : {a.shape}")
print(f"MATRIX : {a}")

wanted_indices=[3,8,12]

b=np.copy(a[wanted_indices])
print(f"\nMATRIX DIM : {b.shape}")
print(f"MATRIX : {b}")

