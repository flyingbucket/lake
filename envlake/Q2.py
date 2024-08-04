import numpy as np
import random
from tqdm import trange
import pickle
import pandas as pd
from lake import get_f
'''
问题：目前程序受随机数影响很大，是有bug的。

'''
random.seed(1)

FUNC_DIR={} # 存储插值函数

# 建立个体模型
class Individual(list):
    def __init__(self, *args):
        super(Individual, self).__init__(*args)
        self.id = None  # 初始化 ID 为 None
        self.fitness = None  # 初始化 fitness 为 None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

def make_ind():
    '''个体模型:从长为100的全1数组中随机抽取3个元素将其置为0'''
    ones=np.ones(100)
    change=random.sample(range(100),3)
    for i in change:
        ones[i]=0
    ind=ones.tolist()
    return ind

# def make_pop(n):
#     '''种群模型:生成n个个体'''
#     pop=[]
#     for i in range(n):
#         ind=make_ind()
#         pop.append(ind)
#     return pop


# 定义操作
def mutate(ind,prob):
    '''变异:随机选择一个0元素和一个1元素进行交换'''
    if random.random()<=prob:
        zero_loc=[] # 0元素位置
        for i in range(len(ind)):
            if ind[i]==0:
                zero_loc.append(i)
        if len(zero_loc)!=3:
            raise ValueError(f'个体中有{len(zero_loc)}个0元素,需要3个')
        ones_loc=list(set(range(len(ind)))-set(zero_loc)) # 1元素位置
        k=random.choice(ones_loc)
        j=random.choice(zero_loc)
        ind[k],ind[j]=ind[j],ind[k]
        new_ind=ind
        new_ind.id=ind.id
        evaluate(new_ind)
        return new_ind
    else:
        return ind

# 选择残差最小的k个个体
def select(pop,k):
    '''选择:锦标赛法,选择强度为k,重置个体id'''
    new_pop=[]
    for _ in range(len(pop)):
        temp_pop=random.sample(pop,k)
        temp_pop.sort(key=lambda x:x.get_fitness())
        new_pop.append(temp_pop[0])
    for i in range(len(new_pop)):
        new_pop[i].set_id(i)
    return new_pop


# 划分训练集和测试集
def divide(ind):
    '''按照individual选择训练集和测试集'''
    file_path = 'D:\mypython\math_modeling\lake\data1.xlsx' 
    data = pd.read_excel(file_path)
    zero_loc=[] # 0元素位置
    ones_loc=[] # 1元素位置
    for i in range(len(ind)):
        if ind[i]==0:
            zero_loc.append(i)
        else:
            ones_loc.append(i)
    train_data=data.iloc[ones_loc]
    test_data=data.iloc[zero_loc]
    return train_data,test_data # 以dataframe形式返回训练集和测试集

# 训练模型
def train(train_data,ind):
    '''训练模型'''
    x = train_data['x'].values
    y = train_data['y'].values
    z = -1 * train_data['z'].values
    temp=(x,y,z)
    func=get_f(temp,ind.id)
    FUNC_DIR[ind.id]=func
    
# 测试模型并返回残差
def test(test_data,ind):
    '''测试模型'''
    x = test_data['x'].values
    y = test_data['y'].values
    z_real = -1 * test_data['z'].values
    err=[]
    for j in range(len(test_data)):
        z_pred=FUNC_DIR[ind.id](x[j],y[j])
        err.append(np.abs(z_real[j]-z_pred))
    return sum(err)

# 适应度函数
def evaluate(ind):
    '''适应度函数:计算个体的适应度'''
    train_data,test_data=divide(ind)
    train(train_data,ind)
    fitness=test(test_data,ind)
    ind.set_fitness(fitness)
    
# 生成随机种群
def make_pop_random(popsize):
    '''生成种群'''
    pop=[]
    for i in range(popsize):
        ind=Individual(make_ind())
        ind.set_id(i)
        evaluate(ind)
        pop.append(ind)
    return pop

# 依据预测值生成种群
def make_pop_guessed(popsize):
    '''依据预测值生成种群'''
    return "waiting for implementation"

# 遗传算法
def GA(init_pop,ngen,mut_prob,k):
    '''遗传算法'''
    for ind in init_pop:
        evaluate(ind)
    pop=select(init_pop,k)
    for i in trange(ngen):
        for i in range(len(pop)):
            new_ind=mutate(pop[i],mut_prob)
            pop[i]=new_ind
        pop=select(pop,k)
    return pop

if __name__ == '__main__':
    popsize=100
    ngen=10
    mut_prob=0.1
    k=15

    # 使用随即种群测试代码
    init_pop=make_pop_random(popsize)
    pop=GA(init_pop,ngen,mut_prob,k)
    id=pop[0].get_id()
    fitness=pop[0].get_fitness()
    print(f'最佳个体id:{id},三点残差和:{fitness}')
    print(f"最佳个体:{pop[0]}")
    # 保存插值函数
    res_func=FUNC_DIR[id]
    with open(rf'D:\mypython\math_modeling\lake\result\res_func_test.pkl', 'wb') as file:
        pickle.dump(res_func, file)