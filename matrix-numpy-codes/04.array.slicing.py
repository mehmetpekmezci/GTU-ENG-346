import numpy as np

print("INITIAL ARRAY")
a = np.array( [   [1, 2,11] , [3, 4,12] , [5,6,13] ] )
print(f"MATRIX DIM : {a.shape}")
print(f"MATRIX : {a}")


b=np.copy(a[1,:2])
print(f"\nMATRIX DIM : {b.shape}")
print(f"MATRIX : {b}")

a[1:,1]=8
print(f"\nMATRIX DIM : {a.shape}")
print(f"MATRIX : {a}")

a[2:,1:]=b
print(f"\nMATRIX DIM : {a.shape}")
print(f"MATRIX : {a}")
