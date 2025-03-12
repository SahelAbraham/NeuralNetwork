import numpy as np
from Layer import Layer
#Tester class for basic debugging of individual classes

nodes = np.array([3, 2, 3, 2, 5])
biases = np.array([0.2, 0.5, 0.1, 0.3, 0.8])

layer1 = Layer(nodes, biases)
layer2 = Layer(nodes)

print("Layer 1")
print(layer1)
print("Layer 2")
print(layer2)
