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
grid_x1 = np.linspace(min_x, max_x, 10)
grid_y1 = np.linspace(min_y, max_y, 10)
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

'''-----遍历圆并测出圆内湖深变化剧烈程度-----'''
# 加载插值函数
with open(r'D:\mypython\math_modeling\lake\result\res_func0.pkl', 'rb') as f:
    interpolator = pickle.load(f)

# 计算每个圆的 tension
circle_properties =[]
for center in all_centers:
    # 生成圆上的点
    angles = np.random.uniform(0, 2 * np.pi, 100)
    # radii = np.sqrt(np.random.uniform(0, 1, 10)) * radius*2
    circle_points = np.array([center[0] + radius * np.cos(angles),
                               center[1] + radius * np.sin(angles)]).T
    
    # 过滤在凸包内的点
    valid_points = [point for point in circle_points if delaunay.find_simplex(point) >= 0]
    if len(valid_points) == 100:
        depths = interpolator(valid_points)
        tension =np.ptp(depths)  # 计算极差
        circle_properties.append({'center': center, 'tension': tension})

# 从 circle_properties 列表中提取所有圆的 tenssion 值
tensions = [circle['tension'] for circle in circle_properties]
print(len(circle_properties))
# 找出 tenssion 值最大的五个圆的索引
top_5_indices = np.argsort(tensions)[-5:]

# 打印这些圆的中心坐标和 tenssion 值
for idx in top_5_indices:
    center = circle_properties[idx]['center']
    tension = circle_properties[idx]['tension']
    print(f"Circle {idx}: Center = ({center[0]:.2f},{center[1]:.2f}) Tension = {tension:.2f}")

'''-----绘图-----'''

# 提取圆心的 x 和 y 坐标
x = [circle['center'][0] for circle in circle_properties]
y = [circle['center'][1] for circle in circle_properties]
tensions = [circle['tension'] for circle in circle_properties]
x=np.array(x)
y=np.array(y)

x=x.reshape(-1,1)
y=y.reshape(-1,1)
points1=np.hstack((x,y))
# 绘制散点图，使用 tension 值作为颜色映射
plt.scatter(x, y, c=tensions, cmap='YlOrBr', edgecolor='k')

# 标出 top_5_indices 中的五个圆
for idx in top_5_indices:
    plt.scatter(circle_properties[idx]['center'][0], circle_properties[idx]['center'][1], 
                color='red', edgecolor='black', s=100, label=f'Circle {idx}')
    
grid_x1, grid_y1 = np.meshgrid(np.linspace(min_x, max_x, 100), np.linspace(min_y, max_y, 100))
grid_points = np.vstack((grid_x1.ravel(), grid_y1.ravel())).T

# 过滤掉凸包外的网格点
hull_path = Delaunay(points)
inside_hull = hull_path.find_simplex(grid_points) >= 0
grid_points = grid_points[inside_hull]

# 计算每个网格点的加权平均 tension 值
weighted_tensions = []
for gp in grid_points:
    distances = np.linalg.norm(points1 - gp, axis=1)
    weights = 1 / distances
    weights /= np.sum(weights)  # 归一化权重
    weighted_tension = np.dot(weights, tensions)
    weighted_tensions.append(weighted_tension)

# 绘制散点图，使用 tension 值作为颜色映射
plt.scatter(x, y, c=tensions, cmap='YlOrBr', edgecolor='k')

# 绘制凸包区域的颜色渐变
plt.tripcolor(grid_points[:, 0], grid_points[:, 1], weighted_tensions, cmap='YlOrBr')

# 绘制凸包
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

# 添加颜色条
plt.colorbar(label='Tension')

# 设置图形属性
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Convex Hull with Tension Gradient')
plt.gca().set_aspect('equal', adjustable='box')

# 显示图形
plt.show()