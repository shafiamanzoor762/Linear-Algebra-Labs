import numpy as np
# code for solving n*n System of Linear Equation by using cramer's rule
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
# m7=np.linalg.inv(m)
# print("inverse of the matrix is=",m7)
vtr1=[]
c=1
while c<=n:
    print("please enter the constant of equations")
    x=eval(input())
    vtr1.append(x)
    c=c+1
vtr2=np.asarray(vtr1)
# ans=np.dot(m7,vtr2)
# print(ans)
# for i in range (len(ans)):
#     print("value of x[",i+1,"]=",np.round(ans[i],2))
det=[]
ans1=[]
print("your orignal matrix=",m)
print("your orignal vector=",vtr2)
for i in range(n):
    m1=m.copy()
    m1[:,i]=vtr2
    print("after =",m1)
    d=np.linalg.det(m1)
    ans1.append(d/n5)
for i in range(n):
    print(ans1)
    print("value of x[", i + 1, "]=", np.round(ans1[i],2))