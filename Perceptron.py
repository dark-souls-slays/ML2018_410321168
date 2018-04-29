
from PIL import Image
import numpy as np

"""
    # Estimate Perceptron weights using stochastic gradient descent
    def train_weights(dataset, W, alpha, n_epoch,E):
    w_previous  = np.zeros((400*300, 3))
    vig = np.full((400*300, 3), .0001)
    a = np.zeros((400*300,1))
    e = np.zeros((400*300,1))
    while (epoch==1) or (epoch<n_epoch) and (np.any((np.absolute(np.array(W) - np.array(w_previous)))>vig))
    for k in range (120000):
    a[k] = W[k].dot(dataset[k])
    e[k] = E[k] - a[k]
    w_previous[k] = W[k]
    W[k] = W[k] + np.dot(dataset[k], (alpha * e[k]))
    epoch = epoch + 1
    return W
    """
#MAIN
with Image.open('/Users/ClaudiaEspinoza/Desktop/I.png').convert('L') as imgI: #.open opens file, .convert('L') changes it to grayscale image
    I = list(imgI.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/key1.png').convert('L') as key1:
    key1 = list(key1.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/key2.png').convert('L') as key2:
    key2 = list(key2.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/E.png').convert('L') as E:
    E = list(E.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/Eprime.png').convert('L') as Eprime:
    print(Eprime.size)
    Eprime = list(Eprime.getdata())


alpha = 0.00001
n_epoch = 10
W = []
dataset = []
Iprime = np.zeros((400*300,1))

for i in range(len(I)):
    dataset.append([])
    dataset[i].append(key1[i])
    dataset[i].append(key2[i])
    dataset[i].append(I[i])

#W = train_weights(dataset,W,alpha,n_epoch,E)
W = np.zeros((400*300+1,3))
W[0] = np.random.rand(1,3)
w_previous  = np.zeros((400*300+1, 3))
vig = np.full((400*300+1, 3), .00001)
a = np.zeros((400*300,1))
e = np.zeros((400*300,1))
epoch = 1
c = 0
while (epoch==1) or (epoch<n_epoch) and (np.any((np.absolute(np.array(W) - np.array(w_previous)))>vig)):
    for k in range (120000):
        a[k] = W[k].dot(dataset[k])
        e[k] = E[k] - a[k]
        step = alpha * e[k]
        w_previous[k] = W[k]
        W[k+1] = W[k] + (dataset[k] * step)
    print epoch
    epoch = epoch + 1

for i in range(120000):
    if W[i][2] == 0: c = 1
    else: c = 0
    Iprime[i] = (Eprime[i]- (W[i][0]*key1[i]) - (W[i][1]*key2[i])) / (W[i][2]+c)


output = Image.new('L', (400,300))
output.putdata(Iprime)
output.save('output2.png')

