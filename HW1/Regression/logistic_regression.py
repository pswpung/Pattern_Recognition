import pandas as pd
import numpy as np

df = pd.DataFrame()
df["Answer"] = [0, 5, 1]
df["data0"] = 1
df["data1"] = [1,2,3]
df["data2"] = [2,3,1]

lr = 0.01
feature = ["data0", "data1", "data2"]
data = np.array(df[feature])
y = np.array(df["Answer"])
theta = np.array([0 for i in range(len(data[0]))])

for round in range(10000):
    sum_data = [0 for i in range(len(theta))]
    for i in range(len(data)):
        lin = theta.dot(data[i].reshape((len(data[i]),1)))[0]
        g = 1/(1 + np.exp(-lin))
        for n in range(len(sum_data)):
            sum_data[n] += ((y[i] - g) * data[i][n])
    theta = theta + lr * np.array(sum_data)
for i in range(len(theta)):
    print(f"theta_{i}(feature : {feature[i]}) : {theta[i]}")