import numpy as np
theta = np.radians(30)
c, s = np.cos(theta), np.sin(theta)
R = np.array(((c, -s), (s, c)))
green_vector=np.array([np.sqrt(3),1])
print(green_vector)
red_vector=np.dot(R,green_vector)
print(red_vector)

