import numpy as np
a=eval(input("Input size of the square coefficient matrix="))
c=1
matrix=[]
vector=[]
for i in range(a):
    r=1
    column=[]
    for i in range(a):
        print("Enter value of column",c)
        x=eval(input())
        column.append(x)
        r = r + 1
    c=c+1
    matrix.append(column)
    r=r+1
matrix.append(column)
print("your column=",matrix)
matrix=np.asarray(matrix)
print("your orignal matrix Matrix=",matrix)
matrix=np.transpose(matrix)
print("Rrequired Matrix=",matrix)
vector=np.zeros(a)
print(vector)
new_vector=[]
for i in vector:
    new_vector.append([i])
new_vector=np.array(new_vector)
aug=np.append(matrix,new_vector,axis=1)#axis=0
print("your augumented matrix with zero's=",aug)
#######################################
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

for i in range(0,a):
    for j in range(i+1,a):
      ratio=aug[j][i]/aug[i][i]
      mul_result=scalar_multiply(aug[i],ratio)
      print("Mul_result",mul_result)
      aug=row_addition(aug,-mul_result,j)
      print("My new aug=",aug)

    # Back Substitution
ans2 = np.zeros(a)
ans2[a - 1] = aug[a - 1][a] / aug[a - 1][a - 1]
for i in range(a - 2, -1, -1):
    ans2[i] = aug[i][a]
    for j in range(i + 1, a):
        ans2[i] = ans2[i] - aug[i][j] * ans2[j]
    ans2[i] = ans2[i] / aug[i][i]
#Dispalying soution
print("\n Required solution is=")

for i in range (len(ans2)):
    print("Value of x[", i + 1, "]=", np.round(ans2[i], 2), end='\t')

if ans2.all()==0:
    print("\n Your Given Vectors from Space",a,"x",a,"=Linearly Independent")
else:
    print("\n Your Given Vectors from Space", a, "x", a, "=Linearly dependent")
