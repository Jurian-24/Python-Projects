from classes.barChart import BarChart
from classes.lineChart import LineChart
import matplotlib.pyplot as plt


def lineChart():
    print('456')

def areaChart(): 
    print('789')

data = ['2', '6' , '4']

labels = ['Januari', 'Februari', 'Maart']

# charts = [LineChart(data, labels, 'testChart')]

LineChart(data, labels).createChart()
plt.show()


# print(charts[0]); print('completed')