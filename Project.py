import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go 
import random
import statistics as st

df = pd.read_csv('prodata.csv')
data = df['reading_time'].tolist()

pm = st.mean(data)
pstdev = st.stdev(data)
print(pm)
print(pstdev)
def randomsetofmeans(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean 
meanlist = []
for i in range(0,1000):
    setofmeans = randomsetofmeans(100)
    meanlist.append(setofmeans)
stdev = st.stdev(meanlist)
mean = st.mean(meanlist)
# print(mean)
# print(stdev)

fstdev_start,fstdev_end = mean-stdev, mean+stdev 
sstdev_start,sstdev_end = mean-2*(stdev), mean+2*(stdev)
tstdev_start,tstdev_end = mean-3*(stdev), mean+3*(stdev)
graph = ff.create_distplot([meanlist],['reading_time'],show_hist=False)
graph.add_trace(go.Scatter(x=[mean,mean],y=[0,1.2],mode='lines',name='mean'))
graph.add_trace(go.Scatter(x=[fstdev_start,fstdev_start],y=[0,1.2],mode='lines',name = 'fstdev_start'))
graph.add_trace(go.Scatter(x=[sstdev_start,sstdev_start],y=[0,1.2],mode='lines',name = 'sstdev_start'))
graph.add_trace(go.Scatter(x=[tstdev_start,tstdev_start],y=[0,1.2],mode='lines',name = 'tstdev_start'))
graph.add_trace(go.Scatter(x=[fstdev_end,fstdev_end],y=[0,1.2],mode='lines',name = 'fstdev_end'))
graph.add_trace(go.Scatter(x=[sstdev_end,sstdev_end],y=[0,1.2],mode='lines',name = 'sstdev_end'))
graph.add_trace(go.Scatter(x=[tstdev_end,tstdev_end],y=[0,1.2],mode='lines',name = 'tstdev_end'))
graph.show()

zscore = (mean-pm)/stdev
print(zscore)