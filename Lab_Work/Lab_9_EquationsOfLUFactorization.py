import numpy as np
a=eval(input("Input size of the square coefficient matrix="))
r=1
matrix=[]
for i in range(a):
    c=1
    row=[]
    for i in range(a):
        print("Enter value of row",r,"column",c)
        x=eval(input())
        row.append(x)
        c=c+1
    matrix.append(row)
    r=r+1
m=np.asarray(matrix)
print("Coefficient Matrix",m)
print("Size of Matrix",m.shape)

def row_interchange(mat,row1,row2):
    t1=mat[row1].copy()
    t2=mat[row2].copy()
    mat[row1]=t2
    mat[row2]=t1
    return mat

def scalar_multiply(mat,scalar):
    return mat*scalar

def row_addition(mat,vect,rownum):
    mat[rownum]=mat[rownum]+vect
    return mat

L=np.eye(a)
print("Your Identity Matrix of order",a,"x",a,"=",L)
for i in range(0,a):
    for j in range(i+1,a):
        if m[i][i]==0:
            m=row_interchange(m,i,j)
        else:
            ratio=m[j][i]/m[i][i]
            L[j][i]=np.round(ratio,2)
            mul_result=scalar_multiply(m[i],np.round(ratio,2))
            print("Mul_result",mul_result)
            U=row_addition(m,-mul_result,j)
            print("My new upper matrix is=\n",U)
            print("My new lower matrix is=\n", L)
mul=np.dot(L,U)
print("LxU=,\n",mul)
vtr1=[]
c=1
while c<=a:
    print("please enter the constant of equations:")
    x=eval(input())
    vtr1.append(x)
    c=c+1
vtr2=np.asarray(vtr1)
m=np.asarray(matrix)
v1=np.asarray(vtr1)
print("Your square matrix=\n",m)
print("Your contant vector=\n",v1)
aug=np.copy(m)
new_v1=[]
for i in v1:
    new_v1.append([i])
new_v1=np.asarray(new_v1)
print("Your column vector=\n", new_v1)
aug=np.append(aug,new_v1,axis=1)
print("Your final augmented matrix=\n", aug)
#FORWARD SUBSTITUTION
ans1=np.zeros(a)
for i in range(a+1):
    if i==a:
        break
    pro=0
    tmp=aug[i][a]
    for j in range(i):
        print("i=",i,"j=",j)
        pro+=aug[i][j]*ans1[j]
        print("pro",pro)
    tmp=tmp-pro
    ans1[i]=tmp
    print("y is=",ans1[i])

for i in range(len(ans1)):
    print("Value of y[",i+1,"]=",np.round(ans1[i],2),end='\t')
new_vector2=[]
for i in ans1:
    new_vector2.append([i])
new_vector2=np.array(new_vector2)
print(new_vector2)

aug2=np.append(U,new_vector2,axis=1)
print("Your Ux=",aug2)
#Back Substitution
ans2=np.zeros(a)
ans2[a-1]=aug2[a-1][a]/aug2[a-1][a-1]
for i in range(a-2,-1,-1):
    ans2[i]=aug2[i][a]
    for j in range(i+1,a):
        ans2[i]=ans2[i]-aug2[i][j]*ans2[j]
    ans2[i]=ans2[i]/aug2[i][i]

for i in range(len(ans2)):
    print("Value of x[",i+1,"]=",np.round(ans2[i],2),end='\t')