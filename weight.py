import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd

df = pd.read_csv("./StudentsPerformance.csv")
mathScore_list = df["math score"].to_list()

mathScore_mean= statistics.mean(mathScore_list)
mathScore_median = statistics.median(mathScore_list)
mathScore_mode = statistics.mode(mathScore_list)
std_deviation = statistics.stdev(mathScore_list)

print("mean {}".format(mathScore_mean))
print("median {}".format(mathScore_median))
print("mode {}".format(mathScore_mode))
print("Standard Devation {}".format(std_deviation))

first_std_deviation_start, first_std_deviation_end = mathScore_mean - std_deviation, mathScore_mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mathScore_mean - (std_deviation*2), mathScore_mean+(std_deviation*2)
third_std_deviation_start, third_std_deviation_end = mathScore_mean - (std_deviation*3), mathScore_mean+(std_deviation*3)

fig = ff.create_distplot([mathScore_list], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mathScore_mean, mathScore_mean], y=[0,0.17], mode = "lines", name="MEANS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.17], mode = "lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,0.17], mode = "lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0,0.17], mode = "lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.17], mode = "lines", name="STANDARD DEVIATION 2"))
fig.show()

stdev_within_1_std_devation = [result for result in mathScore_list if result > first_std_deviation_start and result<first_std_deviation_end]
stdev_within_2_std_devation = [result for result in mathScore_list if result > second_std_deviation_start and result<second_std_deviation_end]
stdev_within_3_std_devation = [result for result in mathScore_list if result > third_std_deviation_start and result<third_std_deviation_end]

print("{}% of data lies in 1 Standard Devation ".format(len(stdev_within_1_std_devation)*100.0/len(mathScore_list)))
print("{}% of data lies in 2 Standard Devation ".format(len(stdev_within_2_std_devation)*100.0/len(mathScore_list)))
print("{}% of data lies in 3 Standard Devation ".format(len(stdev_within_3_std_devation)*100.0/len(mathScore_list)))