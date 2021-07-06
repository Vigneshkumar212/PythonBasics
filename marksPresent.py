import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path): 
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    marksInPersentage = []
    daysPresent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marksInPersentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return {"x": marksInPersentage, "y": daysPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation between Marks In Percentage and Days Present sales is ", correlation[0,1])

def setup():
    datapath = "./MarksDaysPresent.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)
    plotFigure(datapath)

setup()