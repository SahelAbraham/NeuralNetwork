from Layer import Layer
import numpy as np
#The Neural Network, which is an array of layers

def __init__(self, layer_array):
    self.network = layer_array
    for i in range(self.network.size - 1):
        weights_matrix = np.ones(self.network[i], self.network[i+1])
        self.network[i].setWeights(weights_matrix)
    print("All Layers Initialized")

def __str__(self):
    output = "///////////////////////////"
    for layer in self.network:
        output += layer.__str__()
    return output + "\n///////////////////////////"