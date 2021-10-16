import numpy as np
import re
import matplotlib.pyplot as plt


class Perceptron:

    def __init__(self, numOfInputs, learningRate):
        self.learningRate = learningRate
        self.weights = [1.0, 1.0, 1.0]
        self.acc = []

    def __str__(self):
        res = ''
        for i in range(len(self.weights)-1):
            res = res+('w'+str(i+1)+' : ' + str(self.weights[i])+'\n')
        res = res+('b'+' : ' + str(self.weights[len(self.weights)-1]))
        return res

    def train(self, data, labels):
        miss = 0
        for j in range(len(data)):
            w1 = self.weights[0]
            w2 = self.weights[1]
            b = self.weights[2]
            x1 = data[j][0]
            x2 = data[j][1]
            y = w1*x1 + w2*x2 + b

            if y > 0:
                y = 1.0
            else:
                y = 0.0

            out = labels[j]
            if (float(out) != float(y)):
                miss += 1

            self.weights[2] = b + self.learningRate*(out-y)
            self.weights[0] = w1 + self.learningRate*x1*(out-y)
            self.weights[1] = w2 + self.learningRate*x2*(out-y)
        self.acc.append(miss)


def main():
    epoch = 8000
    labels = []
    data = []
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    accList = []
    p = Perceptron(2, 0.05)
    dataFile = open('data.txt', 'r')
    dataList = re.split('\,|\\n', dataFile.read())
    for i in range(0, len(dataList)-1, 3):
        labels.append(float(dataList[i+2]))
        if float(dataList[i+2]) == 1.0:
            x2.append(float(dataList[i]))
            y2.append(float(dataList[i+1]))
        else:
            x1.append(float(dataList[i]))
            y1.append(float(dataList[i+1]))
        data.append((float(dataList[i]), float(dataList[i+1])))

    for i in range(epoch):
        p.train(data, labels)

    w1 = p.weights[0]
    w2 = p.weights[1]
    b = p.weights[2]
    dataFile.close()
    print(p)
    print('Acc : '+str(100-p.acc[epoch-1]/2) + '%')
    a = -w1 / w2
    c = -b / w2

    plt.figure('Q3')
    plt.scatter(x1, y1, c='blue', alpha=0.8)
    plt.scatter(x2, y2, c='red', alpha=0.8)
    x = np.arange(-200, -50)
    plt.plot(x, a*x+c)

    plt.show()

    plt.figure('Q3')

    x = np.arange(0, epoch)
    xAcc = []
    yAcc = []
    for i in range(0, epoch, 50):
        xAcc.append(x[i])
        yAcc.append(p.acc[i]/200*100)
    plt.plot(xAcc, yAcc)

    plt.show()


if __name__ == "__main__":
    main()
