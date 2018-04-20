Version Controlled Image Decryption

PROBLEM DESCRIPTION
Perceptron receives input from training data K1,K2,I, and expected output E; find weights and combine in a linear equation called the activation
E = sum(weight_i * x_i) + bias
The weights of the Perceptron algorithm must be estimated from your training data using stochastic gradient descent.



Stochastic gradient descent

Objective: Train activation function by following the gradients of the cost function (minimize the cost function).

1. Learning Rate: Used to limit the amount each weight is corrected each time it is updated.
2. Epochs: The number of times to run through the training data while updating the weight.
These, along with the training data will be the arguments to the function.
update w in each iteration : w = w + learning_rate * (expected - predicted) * x

Weights are updated based on the error. The error is calculated as the difference between the expected output value and the prediction made with the candidate weights.
