import numpy as np
import pickle
from scipy.integrate import dblquad
from scipy.spatial import ConvexHull, Delaunay
import pandas as pd

# 从pkl文件中加载拟合函数
with open(r'D:\mypython\math_modeling\lake\result\res_func_best.pkl', 'rb') as f:
    lake_surface_fit = pickle.load(f)

# 读取数据并构建凸包
data = pd.read_excel(r'D:\mypython\math_modeling\lake\data1.xlsx')
x = data['x'].values
y = data['y'].values
points = np.vstack((x, y)).T
hull = ConvexHull(points)
delaunay = Delaunay(points)

# 定义湖底曲面函数
def lake_surface(x, y):
    return lake_surface_fit(x, y)

# 定义湖水深度函数（假设湖底最低点为0）
def lake_depth(x, y):
    return min(0, lake_surface(x, y))

# 定义积分区域的边界
def in_hull(x, y, delaunay):
    new_points = np.vstack((x, y)).T
    return delaunay.find_simplex(new_points) >= 0

# 计算湖水体积
xmin, xmax = np.min(x), np.max(x)
ymin, ymax = np.min(y), np.max(y)

def integrand(y, x):
    if in_hull(x, y, delaunay):
        return lake_depth(x, y)
    else:
        return 0

# 分割积分区域
x_mid = (xmin + xmax) / 2
y_mid = (ymin + ymax) / 2

volume1, error1 = dblquad(integrand, xmin, x_mid, lambda x: ymin, lambda x: y_mid,epsabs=1.492e-2,epsrel=1.492e-2)
volume2, error2 = dblquad(integrand, xmin, x_mid, lambda x: y_mid, lambda x: ymax,epsabs=1.492e-2,epsrel=1.492e-2)
volume3, error3 = dblquad(integrand, x_mid, xmax, lambda x: ymin, lambda x: y_mid,epsabs=1.492e-2,epsrel=1.492e-2)
volume4, error4 = dblquad(integrand, x_mid, xmax, lambda x: y_mid, lambda x: ymax,epsabs=1.492e-2,epsrel=1.492e-2)

total_volume = volume1 + volume2 + volume3 + volume4
total_volume=abs(total_volume)
total_error = error1 + error2 + error3 + error4

print(f"Estimated lake volume: {total_volume:.2e} m^3")