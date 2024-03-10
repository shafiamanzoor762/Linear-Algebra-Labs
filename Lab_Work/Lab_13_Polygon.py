# code for translation and rotation transformation
import numpy as np
import matplotlib.pyplot as plt
# For Arrow (Regular Polygon, all vectors are connected and there is no break)
# x = [5, 5, 3, 8, 13, 11, 11]
# y = [0, 3, 3, 8, 3, 3, 0]

# for Car
x = [2, 14, 14, 12, 12, 5, 5, 1]
y = [1, 1, 2, 2, 3, 3, 2, 2]
plt.grid()

plt.fill(x, y, "Green", alpha=0.6)
# Create Translation Matrix
tx = 1.3
ty = -1.3
T = np.array([[1, tx], [0, ty]])
# Translate tx and ty units
points_translated_x = []
points_translated_y = []
print("T Matrix:")
print(T)
print("Your list:")
print(x)
print(y)
for i in range(len(x)):
    p_t = np.dot(T, [x[i], y[i]])
    points_translated_x.append(p_t[0])
    print("New x:")
    print(p_t[0])
    points_translated_y.append(p_t[1])
    print("New y:")
    print(p_t[1])
plt.fill(points_translated_x, points_translated_y, color="Gray", alpha=0.3)
theta = np.pi/2
R = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
points_rotation_x = []
points_rotation_y = []
for i in range(len(x)):
    p_r = np.dot(R, [x[i], y[i]])
    points_rotation_x.append(p_r[0])
    print("New x:")
    print(p_r[0])
    points_rotation_y.append(p_r[1])
    print("New y:")
    print(p_r[1])
plt.fill(points_rotation_x, points_rotation_y, "red", alpha=0.6)
plt.show()