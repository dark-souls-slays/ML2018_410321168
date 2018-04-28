
from PIL import Image
import numpy as np


def predict(row, W):
    arg_max = 0
    predicted_class = 0
    
    for c in range(254):
        current_activation = np.dot(row, W[c])
        if current_activation >= arg_max:
            arg_max, predicted_class = current_activation, c+1
    return predicted_class

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(dataset, W, l_rate, n_epoch,E):
    
    for epoch in range(n_epoch):
        c = 0
        error = 0
        for row in dataset:
            prediction = predict(row, W)
            print( E[c], prediction)
            if not (E[c] == prediction):
                step = [i * l_rate for i in row]
                a = np.array(W[E[c]])
                b = np.array(step)
                W[E[c]] = a+b
                W[prediction] = a-b
                error = error+1
            c = c+1
    return W

#MAIN
with Image.open('/Users/ClaudiaEspinoza/Desktop/I.png').convert('L') as imgI: #.open opens file, .convert('L') changes it to grayscale image
    I = list(imgI.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/key1.png').convert('L') as key1:
    key1 = list(key1.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/key2.png').convert('L') as key2:
    key2 = list(key2.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/E.png').convert('L') as E:
    E = list(E.getdata())

#output.save('output.png')

l_rate = 0.0001
n_epoch = 1
W = []
dataset = []
for i in range(255):
    W.append([])
    for j in range(4):
        W[i].append(0.0)

for i in range(len(I)):
    dataset.append([])
    dataset[i].append(1)
    dataset[i].append(key1[i])
    dataset[i].append(key2[i])
    dataset[i].append(I[i])

W = train_weights(dataset,W,l_rate,n_epoch,E)


#weights0 = train_weights(dataset, l_rate, n_epoch, 0)

