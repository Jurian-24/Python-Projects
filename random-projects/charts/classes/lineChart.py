import matplotlib.pyplot as plt
from PIL import ImageGrab

class LineChart:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def createChart(self):
        plt.plot(self.labels, self.data)

    # def __repr__(self):
    #     return self.createChart()