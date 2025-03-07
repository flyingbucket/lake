import pandas as pd
import numpy as np
from scipy.interpolate import SmoothBivariateSpline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
# 读取Excel文件
file_path = 'D:\\mypython\\math_modeling\\lake\\envlake\\data.xlsx' 
data = pd.read_excel(file_path)

# 提取x, y, z数据
x = data['x'].values
y = data['y'].values
z = -1 * data['z'].values

# 创建二维插值函数
spline = SmoothBivariateSpline(x, y, z)

# 定义拟合函数
def fitted_function(x, y):
    return spline.ev(x, y)

# 计算插值结果
zi_fitted = fitted_function(x, y)

# 计算残差
residuals = z - zi_fitted

# 计算均方误差（MSE）
mse = np.mean(residuals ** 2)
print(f"均方误差（MSE）: {mse}")

# 绘制残差图
plt.figure()
plt.scatter(zi_fitted, residuals)
plt.xlabel('插值结果')
plt.ylabel('残差')
plt.title('残差图')
plt.axhline(y=0, color='r', linestyle='--')
plt.show()

# 创建网格
xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 100)
xi, yi = np.meshgrid(xi, yi)

# 计算插值结果
zi = fitted_function(xi, yi)

# 绘制3D图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xi, yi, zi, cmap='viridis')
ax.scatter(x, y, z, color='r', marker='o')  # 原始数据点
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# 输出拟合函数
print("拟合函数已创建，可以使用fitted_function(x, y)来计算任意(x, y)点的深度值。")

'''
# a=[1,2,3]
# x = np.linspace(0, 1, 5)
# y = np.linspace(0, 1, 5)

# # 定义函数值
# z = np.sin(x[:, None] * np.pi) * np.cos(y[None, :] * np.pi)
# print(np.array([a]))
# print(np.array([a]).shape)


import pandas as pd

# 创建一个五行三列的DataFrame
# data = {
#     'A': [1, 2, 3, 4, 5],
#     'B': [6, 7, 8, 9, 10],
#     'C': [11, 12, 13, 14, 15]
# }
# df = pd.DataFrame(data)
# a=[0,2,4]
# # 选取第1、3、5行
# selected_rows = df.loc[a]

# print(type(selected_rows))
# print(selected_rows)

# from lake import get_f,get_data
# data=get_data()
# A=get_f(data,0)
# breakpoint()
# print(type(A))
# print(A)


# from lake import get_f,get_data
# data=get_data()
# A=get_f(data,0)
# z=A(0.5,0.5)
# z=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0]
# print(sum(z))

import numpy as np

# 假设 circle_properties 列表已经存在
circle_properties = [
    {'center': (1, 2), 'tension': 10},
    {'center': (3, 4), 'tension': 20},
    # 其他圆的信息
]

# 从 circle_properties 列表中提取所有圆的 tenssion 值
tensions = [circle['tension'] for circle in circle_properties]
print(type(tensions[0]))
# 找出 tenssion 值最大的五个圆的索引
top_5_indices = np.argsort(tensions)[-5:]

# 打印这些圆的中心坐标和 tenssion 值
for idx in top_5_indices:
    center = circle_properties[idx]['center']
    tension = circle_properties[idx]['tension']
    #print(f"Circle {idx}: Center = {center}, Tension = {tension:.2f}")