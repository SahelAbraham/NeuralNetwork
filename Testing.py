import numpy as np
import csv
from Layer import Layer
#Tester class for basic debugging of individual classes

with open('Network1.csv', 'r') as file:
    csvreader = csv.reader(file)
    if next(csvreader) == "Layer":
        layer = Layer()