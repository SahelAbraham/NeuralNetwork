import numpy as np
#The basic individual node component in a network

class Neuron:
    
    #constructor
    #index refers to the index of the node in its layer. The first neuron in layer 1 would have an index of 0
    #layer refers to the specific layer that the node is in. An input node will be on the first layer, layer 0
    #state refers to whether it is an input, output, or hidden node. An input node is represtented by 0, a hidden node is 1, and an output node is 2
    #connections is the numpy array of all weighted connections from this neuron to all the neurons on the next layer
    def __init__(self, index=0, layer=0, state=1, connections=np.array([])):
        self.index = index
        self.layer = layer
        self.state = state
        self.connections = connections
    
    #Neuron index setter method
    def set_index(self, index: int):
        self.index = index
    #Neuron index getter method
    def get_index(self):
        return self.index
    #Neuron layer setter method
    def set_layer(self, layer: int):
        self.layer = layer
    #Neuron layer getter method
    def get_layer(self):
        return self.layer
    #Neuron state setter method
    def set_state(self, state: 0 | 1 | 2):
        if state != 0 or state != 1 or state != 2:
            raise ValueError("The state must either be 0 (input), 1 (hidden), or 2 (output)")
        self.state = state
    #Neuron state getter method
    def get_state(self):
        return self.state
    
    #Add a new connection or several connections to list
    #Can take in either an integer
    def add_connection(self, connection: int | float):
        self.connections = np.append(self.connections, connection)
    
    
    #A custom print method for a Neuron
    def __str__(self):
        state = "Hidden" if self.state == 1 else ("Input" if self.state == 0 else "Output")
        return f"Neuron Index: {self.index} | Neuron Layer: {self.layer} | Neuron State: {state} | Neuron Connections: {self.connections.tolist()}"
    