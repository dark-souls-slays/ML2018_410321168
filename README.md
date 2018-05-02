Version Controlled Image Decryption by Single Layer Neural Network

PROBLEM DESCRIPTION

Perceptron receives input from training data K1,K2,I, and expected output E; find weights (w1, w2, w3).


![alt text](https://github.com/dark-souls-slays/ML2018_410321168/blob/master/E.png?raw=true)
![alt text](https://github.com/dark-souls-slays/ML2018_410321168/blob/master/I.png?raw=true)
![alt text](https://github.com/dark-souls-slays/ML2018_410321168/blob/master/key1.png?raw=true)
![alt text](https://github.com/dark-souls-slays/ML2018_410321168/blob/master/key2.png?raw=true)

The weights of the Perceptron algorithm must be estimated from the training data.
For each pixel (120000), find the weights that were used to encrypt image I into image E. Then we use this same weights to decrypt image I'.



FINDING W

Objective: Train the function by following the gradients of the cost function (minimize the cost function).

1. Learning Rate: Used to limit the amount each weight is corrected each time it is updated.
2. Epochs: The number of times to run through the training data while updating the weight.
These, along with the training data will be the arguments to the function.
update w in each iteration : w = w + learning_rate * (expected - predicted) * x

Weights are updated based on the error. The error is calculated as the difference between the expected output value and the prediction made with the candidate weights.


CODE
*include numpy to manipulate lists more easily
*open the images using Pillow
*save the values of the grayscale image (0-255) in a list. We now have 4 list with 120000 pixel values each.
*save list I, key1, key2, into a list of list. This will make it easier to index our training data. For example, dataset[0] = [key1[0], key2[0], I[0]].
*function used to train weights  --->   W[k+1] = W[k] + (dataset[k] * step)

TRAINING function

while (epoch==1) or (epoch<n_epoch) and (np.any((np.absolute(np.array(W) - np.array(w_previous)))>vig)): //avoids recursion if the vector has no changes
    for k in range (120000):
        a[k] = W[k].dot(dataset[k]) //prediction = key1w1 + key2w2 + Iw3
        e[k] = E[k] - a[k]         // ERROR pixel k of image E - prediction with vector W at k
        step = alpha * e[k]        // multiply error by small constant
        w_previous[k] = W[k]
        W[k+1] = W[k] + (dataset[k] * step)
    print epoch
    epoch = epoch + 1

INPUT

![alt text](https://github.com/dark-souls-slays/ML2018_410321168/blob/master/Eprime.png?raw=true)

DECRYPTING THE IMAGE
for i in range(120000):
    if W[i][2] == 0: c = 1 //avoid division by 0
    else: c = 0
    Iprime[i] = (Eprime[i]- (W[i][0]*key1[i]) - (W[i][1]*key2[i])) / (W[i][2]+c)

OUTPUT
![alt text](https://github.com/dark-souls-slays/ML2018_410321168/blob/master/output2.png?raw=true)
