import random
import numpy as np


class NodeGenerator:



    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.nodesNumber = nodesNumber
        coordinates = [[2, height], [], ] #Aqui se anotan las coordenadas X y Y de las capitales 

    def generate(self):
        #Aqui se van a acomodar en dos arreglos, uno para X y el otro para Y, finalmente se regresa un column stack.
        xs = []
        ys = []

        return np.column_stack((xs, ys))
