import numpy as np
import csv
from Layer import Layer
#Tester class for basic debugging of individual classes

with open('Network1.csv', 'r') as file:
    csvreader = csv.reader(file)
    layer = Layer(np.array(next(csvreader)), np.array(next(csvreader)))
    weight_row = [next(csvreader)]
    weights = np.array(weight_row)
    while(weight_row != [['End']]):
        weights = np.append(weights, weight_row, axis=0)
        weight_row = [next(csvreader)]
    print(weights)
    print(layer)
    