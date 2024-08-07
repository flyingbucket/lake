import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from scipy.spatial import ConvexHull , Delaunay
import pandas as pd
import pickle


data = pd.read_excel('D:\mypython\math_modeling\lake\data1.xlsx')

'''-----构建凸包-----'''
x = data['x'].values
y = data['y'].values

x=x.reshape(-1,1)
y=y.reshape(-1,1)

# 将 x 和 y 合并为一个二维数组
points = np.hstack((x, y))

# 计算凸包
hull = ConvexHull(points)

'''-----构造开覆盖-----'''
# 创建 Delaunay 三角剖分对象
delaunay = Delaunay(points)

# 计算凸包的边界框
min_x, min_y = np.min(points, axis=0)
max_x, max_y = np.max(points, axis=0)

# 圆的半径
radius = ((max_x-min_x)+(max_y-min_y))/40  # 你可以根据需要调整半径

# 判断圆心是否在凸包内
def is_circle_valid(center, radius, delaunay):
    # 生成圆上的点
    angles = np.linspace(0, 2 * np.pi, 100)
    circle_points = np.array([center[0] + radius * np.cos(angles), center[1] + radius * np.sin(angles)]).T
    # 判断圆上的点是否在凸包内
    inside_points = delaunay.find_simplex(circle_points) >= 0
    return np.sum(inside_points) >= len(angles)/3  # 大于 1/3 的点在凸包内

# 生成网格点
grid_x1 = np.linspace(min_x, max_x, 15)
grid_y1 = np.linspace(min_y, max_y, 15)
grid_points = np.array(np.meshgrid(grid_x1, grid_y1)).T.reshape(-1, 2)

# 过滤有效的圆心
valid_centers = [center for center in grid_points 
                 if is_circle_valid(center, radius, delaunay)]

# 沿着边界取50个圆心
boundary_centers = []
for simplex in hull.simplices:
    edge_points = points[simplex]
    num_points = 50 // len(hull.simplices)  # 平均分配到每条边
    t_values = np.linspace(0, 1, num_points, endpoint=False)[1:]  # 不包括起点
    for t in t_values:
        boundary_center = (1 - t) * edge_points[0] + t * edge_points[1]
        if is_circle_valid(boundary_center, radius, delaunay):
            boundary_centers.append(boundary_center)
    if len(boundary_centers) >= 20:
        break

# 合并所有有效的圆心
all_centers = valid_centers + boundary_centers[:20]

# 绘制第一张图：凸包和散点
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(points[:, 0], points[:, 1], 'o', label='Data Points')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], 'c', alpha=0.3)
plt.title('Convex Hull and Data Points')
plt.legend()

# 绘制第二张图：凸包、散点和开覆盖的圆
plt.subplot(1, 2, 2)
plt.plot(points[:, 0], points[:, 1], 'o', label='Data Points')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], 'c', alpha=0.3)
for center in all_centers:
    circle = plt.Circle(center, radius, color='r', fill=False, linestyle='--')
    plt.gca().add_patch(circle)
plt.title('Convex Hull, Data Points, and Open Cover Circles')
plt.legend()

plt.tight_layout()
plt.show()