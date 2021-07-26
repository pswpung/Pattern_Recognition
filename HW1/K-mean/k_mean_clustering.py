import numpy as np
from numpy.core.function_base import linspace
import pandas as pd
from pandas.core.frame import DataFrame


# Declare variable
iteration_number: int = 20
iteration_x: DataFrame = pd.DataFrame()
iteration_y: DataFrame = pd.DataFrame()
df : DataFrame = pd.read_csv("raw_data.csv")
######################################################
# HW 1, given data...
# for question 1
centoid_1: list = {'x': 3, 'y': 3}
centoid_2: list = {'x': 2, 'y': 2}
centoid_3: list = {'x': -3, 'y': 3}

# # for question 2
# centoid_1: list = {'x': -3, 'y': -3}
# centoid_2: list = {'x': 2, 'y': 2}
# centoid_3: list = {'x': -7, 'y': -7}
######################################################

def get_distance(df: DataFrame, centoid: list) -> list:
    return list(round(np.sqrt((df['x'] - centoid['x'])**2 + (df['y'] - centoid['y'])**2),2))

def group_data(distance_1: list, distance_2: list, distance_3: list) -> list:
    group: list = []
    for i in range(len(distance_1)):
            check_min: float = min(distance_1[i], distance_2[i], distance_3[i])
            if check_min == distance_1[i]:
                group.append("1")
            elif check_min == distance_2[i]:
                group.append("2")
            elif check_min == distance_3[i]:
                group.append("3")
    return group

def calculate_centoid(iter: int,group: list) -> None:
    new_centoid_x,  new_centoid_y = [], []
    for n in range(1, 4, 1):
        sum_x, sum_y = [], []
        for i in range(len(group)):
            if group[i] == str(n):
                sum_x.append(df['x'][i])
                sum_y.append(df['y'][i])   
        average_x = round(sum(sum_x)/len(sum_x), 2)
        average_y = round(sum(sum_y)/len(sum_y), 2)
        new_centoid_x.append(average_x)
        new_centoid_y.append(average_y)
    centoid_1['x'] = new_centoid_x[0]
    centoid_1['y'] = new_centoid_y[0]
    centoid_2['x'] = new_centoid_x[1]
    centoid_2['y'] = new_centoid_y[1]
    centoid_3['x'] = new_centoid_x[2]
    centoid_3['y'] = new_centoid_y[2]
    iteration_x[iter] = new_centoid_x
    iteration_y[iter] = new_centoid_y

def main():
    for iter in range(iteration_number):
        # calculate distance between data and each centoid
        distance_1: list = get_distance(df, centoid_1)
        distance_2: list = get_distance(df, centoid_2)
        distance_3: list = get_distance(df, centoid_3)
        # group a data to the nearest centoid
        group = group_data(distance_1, distance_2, distance_3)
        # calculate mean of x,y of each group and set it as newcentoid
        calculate_centoid(iter,group)
    print(f"centoid 1: ({iteration_x[iteration_number-1][0]}, {iteration_y[iteration_number-1][0]})")
    print(f"centoid 2: ({iteration_x[iteration_number-1][1]}, {iteration_y[iteration_number-1][1]})")
    print(f"centoid 3: ({iteration_x[iteration_number-1][2]}, {iteration_y[iteration_number-1][2]})")

if __name__ == "__main__":
    main()
