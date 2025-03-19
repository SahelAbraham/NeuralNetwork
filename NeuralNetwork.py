from Layer import Layer
import numpy as np
import csv
#The Neural Network, which is an array of layers

class NeuralNetwork():
    #takes in a csv file that contains the layers, values, weights, and sizes
    def __init__(self, filename = "default.csv", network_name="network"):
        #Initialize the network list and name it
        self.network = []
        self.name = network_name
        #Process the csv file and add each layer to the network
        with open('Network1.csv', 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                #An output row, which starts with 'out', has no weights
                if row[0] == 'out':
                    size = int(row[1])
                    layer = Layer(np.array(row[2:size+2]).astype(int), np.array(row[size+2:2*size+2]))
                #An input row, which starts with 'in' has no biases
                elif row[0] == 'in':
                    size = int(row[1])
                    wsize = int(len(row[size+2:])/size)
                    weights = np.empty(wsize)
                    for i in range(size + 2, len(row), wsize):
                        weights = np.vstack([weights, row[i:i+wsize]])
                    layer = Layer(np.array(row[2:size+2]).astype(int),weights_matrix=np.delete(weights, 0, axis = 0).astype(int))
                else:
                    size = int(row[0])
                    wsize = int(len(row[2*size + 1:])/size)
                    weights = np.empty(wsize)
                    for i in range(2*size + 1, len(row), wsize):
                        weights = np.vstack([weights, row[i:i+wsize]])
                    layer = Layer(np.array(row[1:size+1]).astype(int), np.array(row[size+1:2*size + 1]).astype(int), np.delete(weights, 0, axis = 0).astype(int))
                self.network.append(layer)
                print(layer)
    
    def process(self):
        for i in range(len(self.network)-1):
            self.network[i].update_next_layer(self.network[i+1])

    def __str__(self):
        output = "///////////////////////////\n"
        for i, layer in enumerate(self.network):
            if i == 0:
                output += f"Input Layer\n{layer.__str__()}\n\n"
            if i == len(self.network) - 1:
                output += f"Output Layer\n{layer.__str__()}\n"
            else:
                output += f"Hidden Layer\n{layer.__str__()}\n\n"
        return output + "///////////////////////////"