import numpy as np
import csv
from Layer import Layer
from NeuralNetwork import NeuralNetwork
#Tester class for basic debugging of individual classes

network = NeuralNetwork("Network1.csv", "Test Network")
print(network)