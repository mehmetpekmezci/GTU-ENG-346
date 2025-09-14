import numpy as np
from scipy import stats as st

speed= [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean=np.mean(speed)
median=np.median(speed)
mode=st.mode(speed)

print(f"Mean={mean}")
print(f"Median={median}")
print(f"Mode={mode[0]},  appears {mode[1]} times in the list.")
