
from PIL import Image

def E (e):
    print(predict(e,weights0))
    print(predict(e,weights1))

# Make a prediction with weights
def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-2):
        activation += weights[i + 1] * row[i]
    return 1 if activation>=0 else 0

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch,K):
    weights = [0.0 for i in range(len(train[0]))]
    
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            if row[-1] == K:
                y = 1
            else: y = 0
            prediction = predict(row, weights)
            error = y - prediction
            sum_error += error**2
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return weights

# Calculate weights
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
n_epoch = 20
for i in range(len(I)-1):
    dataset = [1,key1[i],key2[i],I[i],E[i]]
#weights0 = train_weights(dataset, l_rate, n_epoch, 0)

