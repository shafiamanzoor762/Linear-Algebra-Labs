#Code for A=LxU Decomposition of nxn System of Linear Equation
import numpy as np
a=eval(input("input size of the square cofficient Matrix"))
r=1
matrix=[]
for i in range(a):#rows
    c=1
    row=[]
    for i in range(a):#columns
        print("Enter  value of row",r,"column",c)
        x=eval(input())
        row.append(x)#add an element at the end of list
        c=c+1
    matrix.append(row)
    r=r+1#r+=1
m=np.asarray(matrix)
print("Cofficient matrix :",m)
print("Size of matrix :",m.shape)
#######################################
def row_interchange(mat,row1,row2):
    t1 = mat[row1].copy()
    t2 = mat[row2].copy()
    mat[row1]=t2
    mat[row2] = t1
    return mat
########################################
def scalar_multiply(mat,scalar):
    return mat*scalar
########################################
def row_addition(mat,vect,rownum):
    mat[rownum]=mat[rownum]+vect
    return mat
########################################
L=np.eye(a)
print("Your Identity Matrix of order ",a,"x",a,"=",L)
for i in range(0,a):
    for j in range(i+1,a):
        if m[i][i]==0:
            m=row_interchange(m,i,j)
        else:
            ratio=m[j][i]/m[i][i]
            L[j][i]=np.round(ratio,2)
            mul_result=scalar_multiply(m[i],np.round(ratio,2))#row
            print("Mul_result",mul_result)
            U=row_addition(m,-mul_result,j)
            print("My new Upper matrix is=,\n",U)
            print("My new Lower matrix is=,\n", L)
mul=np.dot(L,U)
print("LxU,\n",mul)





