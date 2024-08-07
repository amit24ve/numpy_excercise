import numpy as np
print(np.zeros(10))
print(np.ones(10))
print((np.zeros(10,dtype="i")+7))
print(np.arange(1,10,2))
print(np.linspace(1,5,5))
print(np.arange(1,17,1).reshape(4,4))
print(np.eye(3))
print(np.linspace(0,1,50).reshape(10,5))
a=np.arange(1,26).reshape(5,5)
print(a.view())
print(np.random.rand(3))
print(a)
print(a[2:5,1:5])
print(a.sum())
print(a.sum(axis=1))
print(np.arange(10).reshape(2,5))
a=np.random.random((5,3))
b=np.random.random((3,2))
c=np.dot(a,b)
print(c)
a=np.array([0,4,-2,-5,2])
boolean_arr=a>0
print(boolean_arr)
a=np.arange(1,11)
p=np.array([4,5,67,7,4,2,5,7])
p[p%2==0]*=-1
print(p)
p=np.arange(11)
a=np.flip(p)
print(a)
print(p[::-1])
a=np.array([4,5,67])
b=np.array([2,5,7])
print(np.stack((a,b),axis=1))

a=np.zeros((5,5))
a+=np.arange(5)
print(a)

a=np.array([2,3,4,5,1])
a[:2]=np.mean(4)
print(a)

a=np.ones((5,5))
a[1:-1,1:-1]=np.zeros((3,3))
print(a)

a=np.array([1,2,3,2,3,1,4,6,7,8])
b,c=np.unique(a,return_counts=True)
print(b)
print(c)

a=np.arange(1,10).reshape(3,3)
a[a>3]=1
a[a<2]=0
print(a)

a=np.array([1,2,4])
b=np.array([8,6,5])
c=np.array([9,5,3])

print(np.concatenate((a,b,c)))
print(np.stack((a,b,c)))
print(np.multiply(a,b))
print(np.square((a,b)))
print(np.sqrt((a,b)))