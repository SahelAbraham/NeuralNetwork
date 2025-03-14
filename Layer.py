import numpy as np
#A class that represents a layer in a neural network

class Layer():
    def __init__(self, nodes_vector: np.ndarray=None, bias_vector=None, weights_matrix=None):
        self.nodes = nodes_vector
        self.weights_matrix = weights_matrix
        self.biases = bias_vector
        if bias_vector is None:
            self.biases = np.zeros([len(self.nodes)])
    
    #Take in a numpy array
    def setNodes(self, new_nodes):
        self.nodes = new_nodes
    
    def getNodes(self):
        return self.nodes
    
    #Take in a numpy array
    def setBiases(self, new_biases):
        if new_biases.size != self.nodes.size:
            num1 = self.nodes.size
            num2 = new_biases.size
            raise ValueError(f"The biases must be an array of size {num1} but is instead {num2}")
        self.biases = new_biases
    
    def getBiases(self):
        return self.biases
    
    #Take in a numpy matrix
    def setWeights(self, new_weights):
        self.weights_matrix = new_weights
        
    def getWeights(self):
        return self.weights_matrix
    
    def __str__(self):
        out = ""
        for i in range(len(self.nodes)):
            if self.weights_matrix is not None:
                out += f"[{self.nodes[i]}] ({self.biases[i]}) {self.weights_matrix[:, i]}\n"
            else:
                out += f"[{self.nodes[i]}] ({self.biases[i]})\n"
        return out.rstrip()