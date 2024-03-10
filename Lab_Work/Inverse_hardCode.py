import numpy as np
m1=np.array([[2,9,-3,5],[-3,2,5,-1],[5,1,9,-10],[4,2,3,-4]])
print (m1)
m4=np.linalg.inv(m1)
print(m4)

m=np.asarray(m1)
n5=np.linalg.det(m)
m7=np.linalg.inv(m)
print("inverse of the matrix is=",m7)
vtr1=np.asarray([7,8,-1,5])
ans=np.dot(m7,vtr1)
print(ans)
for i in range (len(ans)):
    print("value of x[",i+1,"]=",np.round(ans))
