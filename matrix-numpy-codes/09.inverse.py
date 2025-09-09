import numpy as np

print("INITIAL ARRAY")
a = np.array( [   [1,2,3] , [5,7,11] , [13,17,23] ] )
print(f"MATRIX DIM : {a.shape}")
print(f"MATRIX : {a}")

b=np.linalg.inv(a)
print(f"\n INVERSE MATRIX:{b} \n")


c=np.matmul(b,a)
print(f"\n A INVERSE * A :{c} \n")


