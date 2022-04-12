import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()
fig = ff.create_distplot([data], ["Average"], show_hist=False)
#fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print(mean, stdev)

def sampling() :
    dataSet = []
    for i in range(0, 400) :
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)

    sampleMean = statistics.mean(dataSet)
    return sampleMean

meanList = []
for i in range(0, 1000) :
    samplingMean = sampling()
    meanList.append(samplingMean)

meanOfSamples = statistics.mean(meanList)
sampleStdev = statistics.stdev(meanList)
print(meanOfSamples, sampleStdev)

fig = ff.create_distplot([meanList], ["Sampling"], show_hist=False)
fig.show()
