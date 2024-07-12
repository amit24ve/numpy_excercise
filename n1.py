import numpy as np
print(np.linspace(0,5,10))
print(np.arange(10))
print(np.eye(3))
print(np.random.rand(10))
print(np.linspace(1,9,12).reshape(4,3))
print(np.arange(19).max())
print(np.arange(19).min())
print(np.zeros(10))
print(np.ones(10))
print(np.zeros(5)+3)
print(np.ones(5)*4)
a=np.linspace(1,10,15)
print(a)
b=np.arange(11,20).reshape(3,3)
print(np.concatenate((a,b),axis=0))
print(np.stack((a,b),axis=0))
print(np.shape(a))


import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
new_arr =arr[:,3]
print(new_arr)

import numpy as np
arr = np.array([1, 2, 1, 3, 5, 0, 0, 0, 2,3,6,6])
result = np.bincount(arr)
print(result)