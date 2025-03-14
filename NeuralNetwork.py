from Layer import Layer
import numpy as np
#The Neural Network, which is an array of layers

#takes in either a list that specifies 
def __init__(self, layer_params=list, network_name="network"):
    self.network = []
    self.name = network_name
    
    #Take in a list of numbers. The size of that list is how many layers there are, and each value in the list is the size of each layer
    for i in layer_params:
        self.network.append(Layer(np.zeros([layer_params[i]])))
    
    #Initializing the weights matrix for each layer except for the output layer, which doesn't need any weights
    for i in range(self.network.size - 1):
        weights_matrix = np.ones(self.network[i], self.network[i+1])
        self.network[i].setWeights(weights_matrix)

    #Confirmation message
    print("All Layers Initialized")

def __str__(self):
    output = "///////////////////////////"
    for layer in self.network:
        output += layer.__str__()
    return output + "\n///////////////////////////"