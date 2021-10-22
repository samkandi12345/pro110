import csv
import plotly.figure_factory as pff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
mean = statistics.mean(data)
print(mean)
stdev = statistics.stdev(data)
print(stdev)

randomdata = []
for i in range (0,100):
    randomIndex = random.randint(0,len(data))
    value = data[randomIndex]
    randomdata.append(value)

print("/////////////////")
mean2 = statistics.mean(randomdata)
print(mean)
stdev = statistics.stdev(randomdata)
print(stdev)

def randomsetofmean(counter):
    randomdata = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        randomdata.append(value)
    mean = statistics.mean(randomdata)
    return mean

def showmean(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    figure = pff.create_distplot([df],["temperature"],show_hist = False)
    figure.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    figure.show()

def main():
    meanlist = []
    for i in range(0,1000):
        setofmean = randomsetofmean(100)
        meanlist.append(setofmean)
    showmean(meanlist)
    mean = statistics.mean(meanlist)
    print(mean)

main()

populationmean = statistics.mean(data)
print(populationmean)
def std():
    meanlist = []
    for i in range(0,1000):
        setofmean = randomsetofmean(100)
        meanlist.append(setofmean)
    stdev = statistics.stdev(meanlist)
    print("??????")
    print(stdev)

std()

figure = pff.create_distplot([data],["temp"],show_hist=False)
figure.show()
