from random import randint

data = [(0, 0), (0, 1), (1, 0), (1, 1)]
labels = [1, 0, 0, 0]
w1 = randint(0, 100)
w2 = randint(0, 100)
b = randint(0, 100)
learningRate = 0.1
# err = 100

for i in range(10000):
    for i in range(len(data)):
        x1 = data[i][0]
        x2 = data[i][1]
        y = w1*x1 + w2*x2 + b
        out = labels[i]
        b = b + learningRate*(out-y)
        w1 = w1 + learningRate*x1*(out-y)
        w2 = w2 + learningRate*x2*(out-y)
        # learningRate -= 0.001

print('b : ', b)
print('w1 : ', w1)
print('w2 : ', w2)
