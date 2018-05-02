Version Controlled Image Decryption by Single Layer Neural Network

PROBLEM DESCRIPTION
Perceptron receives input from training data K1,K2,I, and expected output E; find weights (w1, w2, w3).
![alt text](https://github.com/dark-souls-slays/ML2018_410321168/blob/master/E.png?raw=true)



The weights of the Perceptron algorithm must be estimated from the training data.
For each pixel (120000), find the weights that were used to encrypt image I into image E. Then we use this same weights to decrypt image I'.



FINDING W
Objective: Train activation function by following the gradients of the cost function (minimize the cost function).

1. Learning Rate: Used to limit the amount each weight is corrected each time it is updated.
2. Epochs: The number of times to run through the training data while updating the weight.
These, along with the training data will be the arguments to the function.
update w in each iteration : w = w + learning_rate * (expected - predicted) * x

Weights are updated based on the error. The error is calculated as the difference between the expected output value and the prediction made with the candidate weights.


CODE
*open the images using Pillow
*save the values of the grayscale image (0-255) in a list. We now have 4 list with 120000 pixel values each.
*save list I, key1, key2, into a list of list. This will make it easier to index our training data. For example, dataset[0] = [key1[0], key2[0], I[0]].
