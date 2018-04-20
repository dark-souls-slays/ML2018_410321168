
# Make a prediction with weights
def predict(x, w):
	E = w[0] #bias
	for i in range(len(x)-1):
		E += weights[i + 1] * row[i]
