# Code for finding Basis from set of vectors for non square matrix

import numpy as np
a=eval(input("Input size of the square coefficient matrix="))
b=eval(input("Input number of vectors="))
c=1
matrix=[] #list
vector=[] #Constant vector
for i in range(b): #Column
    r=1
    column=[]
    for i in range(a): #rows
        print("Enter value of column",c)
        x=eval(input())
        column.append(x) #add an element at the end of list
        r=r+1
    c=c+1
    matrix.append(column)
matrix = np.asarray(matrix)
matrix=np.transpose(matrix)
print(matrix)
aug=np.copy(matrix)
###########################
def row_interchange(mat,row1,row2):
    t1=mat[row1].copy()
    t2 = mat[row2].copy()
    mat[row1]=t2
    mat[row2]=t1
    return mat
############################
def sclar_multiply(mat,scalar):
    return mat*scalar
############################
def row_addition(mat,vector,rownum):
    mat[rownum]=mat[rownum]+vector
    return mat
###############################
for i in range(0,b):
    for j in range(i+1,a):
        ratio=aug[j][i]/aug[i][i]
        mul_result=sclar_multiply(aug[i],ratio) #row*ratio
        aug=row_addition(aug,-mul_result,j)
        print("My new Aug=",aug)
for i in range(a):
    for j in range(b):
        if aug[i][j]!=0:
            print("Your vector",matrix[:j])
            break