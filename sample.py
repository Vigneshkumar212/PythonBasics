import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv("./data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Mean of population is ",population_mean)
print("Standard Deveation of population is ",std_deviation)

dataSet = []
for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataSet.append(value)
    
mean = statistics.mean(dataSet)
std_deviation = statistics.stdev(dataSet)
print("Mean of sample is ",mean)
print("Standard Deveation of sample is ",std_deviation)

def random_set_of_mean(counter):
    dataSet = []
    for j in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataSet.append(value)
        
    mean = statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setUp():
    mean_list = []
    for k in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of sampling dist ", mean)

setUp()