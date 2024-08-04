import pandas as pd
import numpy as np
from scipy.interpolate import CloughTocher2DInterpolator
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

RES_FUNCS={}

def get_data():
    '''提取数据'''
    # 读取Excel文件
    file_path = 'D:\mypython\math_modeling\lake\data1.xlsx' 
    data = pd.read_excel(file_path)

    # 提取x, y, z数据
    x = data['x'].values
    y = data['y'].values
    z = -1 * data['z'].values
    return x, y, z,

def get_f(data,i):
    '''获取插值函数,接受参数为数据和编号,data为元组(x,y,z),i为编号'''
    x,y,z=data[0],data[1],data[2]
    # 创建插值函数
    interp_func = CloughTocher2DInterpolator(list(zip(x, y)), z)
    # 保存插值函数到全局字典
    RES_FUNCS[i] = interp_func
    
    return interp_func

def pic(i):
    '''绘制拟合图像'''
    # 加载插值函数
    # with open(r'D:\mypython\math_modeling\lake\result\res_func0.pkl', 'rb') as file:
    #     interp_func_loaded = pickle.load(file)

    x, y, z = get_data()
    # 创建新的网格点进行插值
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)
    interp_func_loaded = RES_FUNCS[i]
    # 进行插值
    zi = interp_func_loaded(xi, yi)

    # 绘制3D图
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xi, yi, zi, cmap='viridis')
    ax.scatter(x, y, z, color='r', marker='o')  # 原始数据点
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


if __name__ == '__main__':
    data = get_data()
    
    res_func=get_f(data,0)
    # 保存插值函数
    with open(rf'D:\mypython\math_modeling\lake\result\res_func0.pkl', 'wb') as file:
        pickle.dump(res_func, file)
    pic(0)