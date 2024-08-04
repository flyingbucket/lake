import numpy as np
from deap import base, creator, tools, algorithms
import pickle
import tqdm

creator.create("ErrorMin" , base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.ErrorMin,id=int)

toolbox = base.Toolbox()

def make_ind():
    '''个体模型:从长为100的全1数组中随机抽取3个元素将其置为0'''
    ones=np.ones(100)
    change=np.random.sample(range(100),3,replace=False)
    for i in change:
        ones[i]=0
    ind=ones.tolist()
    return ind