import numpy as np

print("INITIAL ARRAY")
a = np.array( [   [1, 2] , [3, 4] , [5,6] ] )
print(f"MATRIX DIM : {a.shape}")
print(f"MATRIX : {a}")

b=a.T
print(f"\n MATRIX:{b} \n")
