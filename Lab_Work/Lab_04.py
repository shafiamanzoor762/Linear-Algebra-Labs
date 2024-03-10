a=eval(input("Enter a no. "))
print (a)
i=1
while i<=a:
    print(i,'my name is Shafia')
    i=i+1
import numpy as np
m1=np.array([[2,5],[3,6]])
print (m1)
m2=np.transpose(m1)
print(m2)
m3=np.linalg.det(m1)
print(m3)
m4=np.linalg.inv(m1)
print(m4)
m5=np.dot(m1,m2)
print(m5)
# code for solving n*n System of Linear Equation
n=eval(input("Enter the Size of Matrix:"))
r=1
matrix=[]
while r<=n:
    c=1
    row=[]
    while c<=n:
        print("Enter the value of row",r,"coloumn",c)
        x=eval(input())
        row.append(x)
        c=c+1
        matrix.append(row)
        r=r+1
m=np.asarray(matrix)
print("cofficient matrix=",m)
n5=np.linalg.det(m)
print("Determininant of matrix is =",n5)
m7=np.linalg.inv(m)
print("inverse of the matrix is=",m7)
vtr1=[]
c=1
while c<=n:
    print("please enter the constant of equations")
    x=eval(input())
    vtr1.append(x)
    c=c+1
vtr2=np.asarray(vtr1)
ans=np.dot(m7,vtr2)
print(ans)
for i in range (len(ans)):
    print("value of x[",i+1,"]=",np.round(ans))
