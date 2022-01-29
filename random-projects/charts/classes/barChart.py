import matplotlib.pyplot as plt
from PIL import ImageGrab

class BarChart:
    def __init__(self, data, labels, chartName):
        self.data = data
        self.labels = labels
        self.chartName = chartName

    def createChart(self):

        img = ImageGrab.grab()

        plt.bar(len(self.data), self.data, self.labels, color = ['red', 'green', 'blue'])

        plt.xlabel('x - axis')

        plt.ylabel('y - axis')

        plt.title(self.chartName)

        plt.show()
    
    def __repr__(self):
        return self.createChart()
