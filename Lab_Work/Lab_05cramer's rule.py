# import numpy as np
#
# mat = np.array([[1, 2, 1], [1, 2, 1],[1, 2, 1]])
# constant = np.array([1, 2, 3])
#
#
# def cramer(mat, constant):  # takes the matrix and the costants
#
#     D = np.linalg.det(mat)  # calculating the determinant of the original matrix
#
#     # substitution of the column with constant and creating new matrix
#     mat1 = np.array([constant, mat[1], mat[2]])
#     mat2 = np.array([mat[0], constant, mat[2]])
#     mat3 = np.array([mat[0], mat[1], constant])
#
#     # calculatin determinant of the matrix
#     D1 = np.linalg.det(mat1)
#     D2 = np.linalg.det(mat2)
#     D3 = np.linalg.det(mat3)
#
#     # finding the X1, X2, X3
#     X1 = D1 / D
#     X2 = D2 / D
#     X3 = D3 / D
#
#     print(X1, X2, X3)
#
#
# cramer(mat, constant)
#--------------------------------------------------

import numpy as np
#
# Mat1 = np.array([[2, 3, -4], [4, 6, 1], [3, 7, -2]])
# print("your orignal matrix is =", Mat1)
#
#
# def row_int(mat, r1, r2):
#     t1 = mat[[r1 - 1]].copy()
#     t2 = mat[[r2 - 1]].copy()
#     mat[[r1 - 1]] = t2
#     mat[[r2 - 1]] = t1
#
#
# row_int(Mat1, 1, 2)
# print(Mat1)


# construction of function for scalar multiplication
# Mat1=np.array([[2,3,-4],[4,6,1,],[3,7,-2]])
# print("your orignal matrix is =", Mat1)
#
# def sclr_mul(mat,scalar,row):
#     mat[row]=scalar*mat[row]
#
# sclr_mul(Mat1,-8,1)
# print("after scalar multiplication ,matrix is=",Mat1)
# construction of the function of adding two rows
Mat1=np.array([[2,3,-4],[4,6,1],[3,7,-2]])
print("your orignal matrix is =", Mat1)
def add_mat(mat,r1,r2):
    mat[r1-1]=mat[r1-1]+mat[r2-1]
add_mat(Mat1,2,3)
print("after addition, matrix is=", Mat1)


# code for solving n*n System of Linear Equation by using cramer's rule
# n=eval(input("Enter the Size of Matrix:"))
# r=1
# matrix=[]
# while r<=n:
#     c=1
#     row=[]
#     while c<=n:
#         print("Enter the value of row",r,"coloumn",c)
#         x=eval(input())
#         row.append(x)
#         c=c+1
#     matrix.append(row)
#     r=r+1
# m=np.asarray(matrix)
# print("cofficient matrix=",m)
# n5=np.linalg.det(m)
# print("Determininant of matrix is =",n5)
# m7=np.linalg.inv(m)
# print("inverse of the matrix is=",m7)
# vtr1=[]
# c=1
# while c<=n:
#     print("please enter the constant of equations")
#     x=eval(input())
#     vtr1.append(x)
#     c=c+1
# vtr2=np.asarray(vtr1)
# ans=np.dot(m7,vtr2)
# print(ans)
# for i in range (len(ans)):
#     print("value of x[",i+1,"]=",np.round(ans[i],2))
# det=[]
# ans1=[]
# print("your orignal matrix=",m)
# print("your orignal vector=",vtr2)
# for i in range(n):
#     m1=m.copy()
#     m1[:,i]=vtr2
#     print("after =",m1)
#     d=np.linalg.det(m1)
#     ans1.append(d/n5)
# for i in range(n):
#     print(ans1)
#     print("value of x[", i + 1, "]=", np.round(ans[i],2))