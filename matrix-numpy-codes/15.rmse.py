import numpy as np

a = np.array( [   [1, 2] ,[3,4]  ] )
print(f"MATRIX A : {a}")

b = np.array( [   [5, 6] ,[7,8]  ] )
print(f"MATRIX B : {b}")

rmse = np.sqrt((np.square(a - b)).mean())
print(rmse)
