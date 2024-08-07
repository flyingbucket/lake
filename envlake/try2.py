import numpy as np
import pandas as pd
data=pd.read_excel('D:\mypython\math_modeling\lake\data.xlsx',header=0)
X=data['x'].values
Y=data['y'].values
Z=data['z'].values
ptp1=np.ptp(X)
ptp2=np.ptp(Y)
ptp3=np.ptp(Z)
print(ptp1,ptp2,ptp3)