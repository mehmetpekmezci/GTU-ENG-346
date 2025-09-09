import numpy as np

a = np.array( [   [1, 2,3,4] , [5, 6, 7,8 ] ] )
print(f"MATRIX A : {a}")

b,c=np.hsplit(a,2)
print(f"\n First Split:{b} \n")
print(f"\n Second Split:{c} \n")

