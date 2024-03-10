import numpy as np
List1=[10,20,30,40,50]
# we are creating a horizon list
vtr1=np.array(List1)
print(vtr1)
List2=[[12],
       [15],
       [17],
       [19]]
# we are creating a coloumn vector from list
vtr2=np.array(List2)
print(vtr2)
vtr1=np.array(List1)
print(vtr1)
List3=[11,12,15,17,20]
# ('we are creating')
vtr3=np.array(List3)
# (Addiction of two vectors)
vtr_add=vtr1+vtr3
print(vtr_add)
# (Subtraction of two vectors)
vtr_sub=vtr1-vtr3
print(vtr_sub)
# (Multiplication of two vectors)
vtr_mul=vtr1*vtr3
print(vtr_mul)
# (dot product of two vectors)
vtr_product=vtr1.dot(vtr3)
print(vtr_product)
scalar_value=6
print('any scalar multiplication with vector')
vtr_scalar=vtr1* scalar_value
print (vtr_scalar)
# create a matrix 2*3 dimensions
# create an origin point, from
import matplotlib.pyplot as plt
# create the origin point from where vector could be originated
# plot a 3D fields of arrows using the quiver method
# with origin, data, color and scale
start=[0,0]
u=[2,2]
v=[1, -1]
fig, ax=plt.subplots( figsize=(16, 16))
ax.quiver (start[0], start[ 1],u[0],u[1], color="r", scale=7)
plt.show()
ax.quiver (start[0], start[ 1],v[0],v[1], color="b", scale=7)
plt.show()
import matplotlib.pyplot as plt
start=[0,0,0]
u=[2,2,3]
v =[1,-1,4]
w= [3,-1,2]
fig, ax = plt.subplots(figsize=(12,12))
ax=plt.axes(projection='3d')
ax.quiver(start[0], start[1], start[2], u[0], u[1],u[2], color="b")
ax.quiver(start[0], start[ 1], start [2],v[0],v[1],v[2],color="r")
ax.quiver(start[0], start[ 1], start[2],w[0],w[1],w[2 ], color="y")
ax.view_init(0,10)
ax.set_xlim ([-10,10])
ax.set_ylim ([-10,10])
ax.set_zlim ([-10,10])
plt.show()

import matplotlib.pyplot as plt
start=[0,0,0]
u = [2, 2, 3]
v = [1,-1,4]
w = [3, - 1, 2]
e = [- 3, 12, - 2]
h = [9,6,12]
g = [3, 8, 9]
fig, ax = plt.subplots( figsize=(12,12))
ax = plt.axes (projection='3d')
ax.quiver(start[0], start[1], start[2], u[0], u[1],u[2], color ="b")
ax.quiver(start[0], start[1], start[2], v[0],v[1],v[2], color ="r")
ax.quiver(start[0], start[1], start[2], w[0],w[1],w[2 ], color ="y")
ax.quiver(start[0], start[1], start[2], e[0], [1],[2],color="y")
ax.quiver(start[0], start[1], start[2], h[0], h[1], h[2],color="g")
ax.quiver(start[0], start[1], start[2], g[0], g[1], g [2],color="b")
ax.quiver(start[0], start[1], start[2], e[0], [1], [2], color="y")
ax.quiver(start[0], start[0], start[2],h[0],h[1],h[2],color="g")
ax.quiver(start[0], start[1], start[2],g[0],g[1],g[21],color="b")
ax.view_init(0,10)
ax.set_xlim ([-10,10])
ax.set_ylim([-10,10])
ax.set_zlim ([-10,10])
plt.show()

