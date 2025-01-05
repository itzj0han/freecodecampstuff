import sys
import numpy as np
z=0
list1=[]
dict1={
    'mean':[],
    'variance':[],
    'standard deviation':[],
    'max':[],
    'min':[],
    'sum':[]

}
while z<9:
    list1.append(int(input()))
    z=z+1
def calculate(list):
    matrix1=np.array(list1).reshape(3,3)
    matrixflattened=matrix1.flatten()
    dict1['mean'].append(matrix1.mean(axis=0).tolist())
    dict1['mean'].append(matrix1.mean(axis=1).tolist())
    dict1['mean'].append(matrixflattened.mean().tolist())
    dict1['variance'].append(matrix1.var(axis=0).tolist())
    dict1['variance'].append(matrix1.var(axis=1).tolist())
    dict1['variance'].append(matrixflattened.var().tolist())
    dict1['standard deviation'].append(matrix1.std(axis=0).tolist())
    dict1['standard deviation'].append(matrix1.std(axis=1).tolist())
    dict1['standard deviation'].append(matrixflattened.std().tolist())
    dict1['max'].append(matrix1.max(axis=0).tolist())
    dict1['max'].append(matrix1.max(axis=1).tolist())
    dict1['max'].append(matrixflattened.max().tolist())
    dict1['min'].append(matrix1.min(axis=0).tolist())
    dict1['min'].append(matrix1.min(axis=1).tolist())
    dict1['min'].append(matrixflattened.min().tolist())
    dict1['sum'].append(matrix1.sum(axis=0).tolist())
    dict1['sum'].append(matrix1.sum(axis=1).tolist())
    dict1['sum'].append(matrixflattened.sum().tolist())
    print(dict1) 
calculate(list1)