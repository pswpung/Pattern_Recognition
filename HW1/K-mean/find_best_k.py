import pandas as pd
import numpy as np
import random

df = pd.read_csv("raw_data.csv")
x_iter = pd.DataFrame()
y_iter = pd.DataFrame()

def random_centoid(k_cluster):
    centoid =[]
    for i in range(k_cluster):
        random_centoid = [random.randint(min(df['x']), max(df['x'])),random.randint(min(df['y']), max(df['y']))]
        centoid.append(random_centoid)
    return centoid

def get_distance(centoid):
    distance = []
    for i in centoid:
        distance.append(list(np.sqrt((df['x'] - i[0])**2 + (df['y'] - i[1])**2)))
    return distance

def group_data(distance):
    group = []
    distance = np.transpose(np.array(distance))
    # print(distance)
    min_check = [min(distance[i]) for i in range(len(distance))]
    # print(min_check)
    for i in range(len(distance)):
        for j in range(len(distance[i])):
            if distance[i][j] == min_check[i]:
                group.append(j)
    return group

def update_centoid(k_cluster, group):
    new_centoid_x,  new_centoid_y = [], []
    for n in range(k_cluster):
        # print(n)
        sum_x, sum_y = [], []
        for i in range(len(group)):
            if group[i] == n:
                sum_x.append(df['x'][i])
                sum_y.append(df['y'][i])
        # print(f"sum_x : {sum_x}")
        # print(f"sum_y : {sum_y}")
        if len(sum_x) != 0:  
            average_x = sum(sum_x)/len(sum_x)
            average_y = sum(sum_y)/len(sum_y)
        else:
            average_x, average_y = None,None      
        # print(f"average group {n} : ({average_x}, {average_y})")
        new_centoid_x.append(average_x)
        new_centoid_y.append(average_y)
        # print(f"new centoid x : {new_centoid_x}")
        # print(f"new centoid x : {new_centoid_y}")
    for i in range(len(new_centoid_x)):
        if new_centoid_x[i] != None:
            centoid[i][0] = new_centoid_x[i]
        if new_centoid_y[i] != None:
            centoid[i][1] = new_centoid_y[i]
    return centoid


# for k_cluster in range(2,10):
k_cluster = int(input("How many group do you want? : "))
centoid = random_centoid(k_cluster)
print(f"random centoid : {centoid}")
for round in range (100):
    distance = get_distance(centoid)
    group = group_data(distance)
    centoid = update_centoid(k_cluster, group)
print(f"final centoid : {centoid}")
# for i in range(k_cluster):
#     pass