import numpy as np
import pandas as pd
data=pd.read_excel('D:\mypython\math_modeling\lake\data.xlsx',header=0)
Z=data['z'].values
ptp=np.ptp(Z)
print(ptp)