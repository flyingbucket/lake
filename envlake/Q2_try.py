import random
import numpy as np
from tqdm import trange
import pandas as pd  # 导入pandas库用于处理Excel文件
from scipy.interpolate import CloughTocher2DInterpolator


class Individual(object):
    def __init__(self, genes):
        self.genes = genes
        self.id = None  # 初始化 ID 为 None
        self.fitness = None  # 初始化 fitness 为 None
        self.interpolator = None  # 添加 interpolator 属性

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def set_interpolator(self, interpolator):
        self.interpolator = interpolator

    def get_interpolator(self):
        return self.interpolator

    # def __len__(self):
    #     return len(self.genes)
    
    # def __getitem__(self, index):
    #     return self.genes[index]
    
    # def __setitem__(self, index, value):
    #     self.genes[index] = value

    def __repr__(self):
        return str(self.genes)


def make_ind():
    """创建一个包含97个1和3个0的个体"""
    ones = np.ones(97)
    zeros = np.zeros(3)
    individual = np.concatenate([ones, zeros])  # 合并数组
    np.random.shuffle(individual)  # 打乱数组顺序
    return individual.tolist()


def divide(ind):
    """按照individual选择训练集和测试集"""
    file_path = 'D:\mypython\math_modeling\lake\data1.xlsx'
    data = pd.read_excel(file_path)
    zero_loc = []  # 0元素位置
    ones_loc = []  # 1元素位置
    for i in range(len(ind.genes)):
        if ind.genes[i] == 0:
            zero_loc.append(i)
        else:
            ones_loc.append(i)
    train_data = data.loc[ones_loc]
    test_data = data.loc[zero_loc]
    return train_data, test_data  # 以DataFrame形式返回训练集和测试集


def train(train_data, ind):
    """训练模型"""
    x = train_data['x'].values
    y = train_data['y'].values
    z = -1 * train_data['z'].values
    func = CloughTocher2DInterpolator(list(zip(x, y)), z)
    ind.set_interpolator(func)


# 测试模型并返回残差
def test(test_data, ind):
    """测试模型"""
    x = test_data['x'].values
    y = test_data['y'].values
    z_real = -1 * test_data['z'].values
    err = []
    for j in range(len(test_data)):
        z_pred = ind.get_interpolator()(x[j], y[j])
        err.append(np.abs(z_real[j] - z_pred))
    return sum(err)


def evaluate(individual):
    """适应度函数: 计算个体的适应度"""
    train_data, test_data = divide(individual)
    train(train_data, individual)
    fitness = test(test_data, individual)
    individual.set_fitness(fitness)


def select(population, k):
    selected_population = []
    used_ids = set()  # 用于跟踪已使用的 ID
    for _ in range(k):
        temp_pop = random.sample(population, k)
        temp_pop.sort(key=lambda x: x.get_fitness())
        selected_individual = temp_pop[0]

        # 确保新的 ID 未被使用过
        new_id = 0
        while new_id in used_ids:
            new_id += 1

        selected_individual.set_id(new_id)
        used_ids.add(new_id)
        selected_population.append(selected_individual)

    return selected_population


def mutate(individual, mut_prob):
    """执行变异操作，确保始终有97个1和3个0"""
    # 先记录变异前0和1的数量
    num_zeros = sum(1 for gene in individual.genes if gene == 0)
    num_ones = len(individual.genes) - num_zeros

    # 变异
    for i in range(len(individual.genes)):
        if random.random() < mut_prob and num_ones > 97 and num_zeros > 3:
            # 只当1的数量超过97或者0的数量超过3时才考虑变异
            individual.genes[i] = 1 - individual.genes[i]  # 翻转基因
            num_zeros += -2 if individual.genes[i] == 0 else 2
            num_ones += 2 if individual.genes[i] == 1 else -2

    # 检查变异后的0和1的数量
    new_num_zeros = sum(1 for gene in individual.genes if gene == 0)
    new_num_ones = len(individual.genes) - new_num_zeros

    # 如果数量不符合要求，则回滚变异
    if new_num_zeros != 3 or new_num_ones != 97:
        return individual  # 回滚变异
    else:
        return individual  # 变异成功

# def mutate(ind,prob):
#     '''变异:随机选择一个0元素和一个1元素进行交换'''
#     if random.random()<=prob:
#         zero_loc=[] # 0元素位置
#         for i in range(len(ind)):
#             if ind[i]==0:
#                 zero_loc.append(i)
#         if len(zero_loc)!=3:
#             raise ValueError(f'个体中有{len(zero_loc)}个0元素,需要3个')
#         ones_loc=list(set(range(len(ind)))-set(zero_loc)) # 1元素位置
#         k=random.choice(ones_loc)
#         j=random.choice(zero_loc)
#         ind[k],ind[j]=ind[j],ind[k]
#         new_ind=ind
#         new_ind.id=ind.id
#         evaluate(new_ind)
#         return new_ind
#     else:
#         return ind



def GA(init_pop, ngen, mut_prob, k):
    for individual in init_pop:
        evaluate(individual)
    population = select(init_pop, k)
    for _ in trange(ngen):
        for i in range(len(population)):
            new_individual = mutate(population[i], mut_prob)
            population[i] = Individual(new_individual.genes)  # 创建一个新的 Individual 实例
            evaluate(population[i])
        population = select(population, k)
    return population


if __name__ == '__main__':
    popsize = 100
    ngen = 50
    mut_prob = 0.1
    k = 15

    file_path = 'D:\mypython\math_modeling\lake\data1.xlsx'
    data = pd.read_excel(file_path)

    init_pop = [Individual(make_ind()) for _ in range(popsize)]
    population = GA(init_pop, ngen, mut_prob, k)
    best_individual_id = population[0].get_id()
    best_fitness = population[0].get_fitness()
    print(f'最佳个体id: {best_individual_id}, 三点残差和: {best_fitness}')
    print(f"最佳个体: {population[0]}")