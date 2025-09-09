import numpy as np

print("INITIAL ARRAY")
a = np.array( [   [1, 2] , [3, 4] , [5,6] ] )
print(f"MATRIX DIM : {a.shape}")
print(f"MATRIX : {a}")

print("\nRESHAPED TO (2,3) ARRAY")
b=a.reshape((2,3))
print(f"MATRIX DIM : {b.shape}")
print(f"MATRIX : {b}")


print("\nRESHAPED TO (6,1) ARRAY")
c=a.reshape((6,))
print(f"MATRIX DIM : {c.shape}")
print(f"MATRIX : {c}")

