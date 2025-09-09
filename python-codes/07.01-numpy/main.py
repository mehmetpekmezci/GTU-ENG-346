import numpy as np
a = np.array([1, 2, 3])
print(f"type(a)={type(a)}")
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(f"a={a}")
b = np.array([[1,2,3],[4,5,6]])
print(f"b.shape={b.shape}")                
print(f"b[0, 0]={b[0, 0]}, b[0, 2]={b[0,2]}") 
print(f"np.matmul(b.T,b)={np.matmul(b.T,b)}")
print(f"np.zeros((2,2))={np.zeros((2,2))}")
print(f"np.ones((1,2))={np.ones((1,2))}")
print(f"np.full((2,2), 7)={np.full((2,2), 7)}")
d = np.eye(2)
print(f"d={d}")
e = np.random.random((2,2))
print(f"e={e}")
print(f"d*e:{d*e}")
print(f"np.matmul(d,e):{np.matmul(d,e)}")
f=np.concatenate((d, e), axis=0)
print(f"f={f}")
g=np.concatenate((d, e), axis=1)
print(f"g={g}")
data = np.array([1.0, 2.0])
data = data * 1.6
print(f"data={data}")


