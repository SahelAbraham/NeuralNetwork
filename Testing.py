import numpy as np
from Neuron import Neuron
#A tester class to do base level testing on individual classes

test_connections = np.array([34.0, 2.0, 12.2])
empty_neuron = Neuron()
test_neuron1 = Neuron(1, 3, 2, test_connections)
test_neuron2 = Neuron(1, 3, 2, np.array([2, 3]))

test_neuron2.add_connection(test_connections)
test_neuron2.add_connection(3.823)

print(empty_neuron)
print(test_neuron1)
print(test_neuron2)
