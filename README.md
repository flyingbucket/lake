# Lake Modeling Project
PS.此readme文档由copilot自动生成

本项目旨在通过数据拟合和凸包算法对湖泊底面进行建模和分析。


## 文件说明

 - [`data.xlsx`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fdata.xlsx%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\mypython\math_modeling\lake\data.xlsx"),
 - [`data1.xlsx`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fdata1.xlsx%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\mypython\math_modeling\lake\data1.xlsx"): 数据文件，包含湖泊表面数据。
 - [`envlake/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\mypython\math_modeling\lake\envlake\"): 虚拟环境目录，包含项目依赖和脚本。
  - [`lake.py`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5Cmypython%5C%5Cmath_modeling%5C%5Clake%5C%5Cenvlake%5C%5Cvolume.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A38%7D%7D%5D%5D "Go to definition"): 主要的湖泊表面建模脚本。
  - [`volume.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\mypython\math_modeling\lake\envlake\volume.py"): 体积计算脚本。
  - 其他脚本文件用于不同的实验和测试。
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\mypython\math_modeling\lake\requirements.txt"): 项目依赖文件。
- [`result/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fresult%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\mypython\math_modeling\lake\result\"): 结果文件夹，包含拟合函数和其他结果文件。
  - [`res_func_best.pkl`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5Cmypython%5C%5Cmath_modeling%5C%5Clake%5C%5Cenvlake%5C%5Cvolume.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A50%7D%7D%5D%5D "Go to definition"): 最佳拟合函数。
  - [`temp result.txt`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5Cmypython%5C%5Cmath_modeling%5C%5Clake%5C%5Cenvlake%5C%5Cvolume.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A43%7D%7D%5D%5D "Go to definition"): 结果说明文档。

## 使用说明

1. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```


2. 查看结果：
    - 结果文件保存在 [`result/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fresult%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\mypython\math_modeling\lake\result\") 文件夹中。
    - [`temp result.txt`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5Cmypython%5C%5Cmath_modeling%5C%5Clake%5C%5Cenvlake%5C%5Cvolume.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A43%7D%7D%5D%5D "Go to definition") 文件包含了结果的详细说明。

## 结果说明

[`result/temp result.txt`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5Cmypython%5C%5Cmath_modeling%5C%5Clake%5C%5Cenvlake%5C%5Cvolume.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22path%22%3A%22%2Fd%3A%2Fmypython%2Fmath_modeling%2Flake%2Fenvlake%2Fvolume.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A43%7D%7D%5D%5D "Go to definition") 文件中包含了以下内容：

1. 图片解释：
    - `hull and coverage`: 拟合出的数据点边界，并标记了扫描所用的所有单位圆。
    - `tension.png`: 以每个单位圆各自的张力值（单位圆内深度变化极差）为权重进行着色绘制的深度变化剧烈程度图，颜色越深表示变化越剧烈。
    - `tension with mark.png`: 在 `tension.png` 的基础上标出了张力值最大的前十个圆。

2. 文档解释：
    - 第二问的运行结果，给出了测试集与训练集的最佳划分方案，及其对应的误差和拟合函数。

## 贡献

欢迎提交问题和贡献代码！

## 许可证

本项目采用 MIT 许可证。
