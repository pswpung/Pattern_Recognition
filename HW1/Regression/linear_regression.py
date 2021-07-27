# Import Packages
import pandas as pd
import numpy as np

# Create Pandas DataFrame
df = pd.DataFrame()
df["Answer"] = [0, 5, 1]
df["data0"] = 1
df["data1"] = [1,2,3]
df["data2"] = [2,3,1]

# Declare  Global Variable
lr = 0.01
round = 10000
feature = ["data0", "data1", "data2"]

#### Solution 1 : For Loop ####
data = np.array(df[feature])
y = np.array(df["Answer"])
theta = np.array([0 for i in range(len(data[0]))])

print("Solution 1 : For Loop")
for round in range(round):
    sum_data = [0 for i in range(len(theta))]
    for i in range(len(data)):
        lin = theta.dot(data[i].reshape((len(data[i]),1)))[0]
        for n in range(len(sum_data)):
            sum_data[n] += (y[i] - lin) * data[i][n]
    theta = theta + lr * np.array(sum_data)
for i in range(len(theta)):
    print(f"theta_{i}(feature : {feature[i]}) : {theta[i]}")

#### Solution 2 : Vectorization ####
data = np.array(df[feature]).transpose()
y = np.array(df["Answer"]).reshape((1,3))
theta = np.array([0 for i in range(len(data[0]))]).reshape((1,3))

print("Solution 2 : Vectorization")
for round in range(round):
    lin = theta.dot(data) 
    sum_data = ((y - lin) * data).sum(axis = 1)
    theta = theta + lr * sum_data
for i in range(len(theta[0])):
    print(f"theta_{i}(feature : {feature[i]}) : {theta[0][i]}")