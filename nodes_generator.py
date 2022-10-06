import random
import numpy as np


class NodeGenerator:



    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.nodesNumber = nodesNumber
        #Aqui se anotan las coordenadas X y Y de las capitales 
        '''
        Las capitales iran en el siguiente orden:
        1. Mexicalli
        2. La Paz
        3. Hermosillo 
        4. Chihuahua
        5. Saltillo
        6. Monterrey
        7. Ciudad Victoria
        8. San Luis Potosi
        9. Zacatecas
        10. Durango
        11. Culiacan
        12. Tepic
        13. Guadalajara
        14. Colima
        15. Aguascalientes 
        17. Guanajuato
        18. Queretaro
        19. Pachuca
        20. Xalapa
        21. Puebla 
        22. Cuernavaca
        23. CDMX
        24. Toluca
        25. Morelia
        26. Chilpancingo
        27. Oaxaca
        28. Tuxtla Gutierrez
        29. Villahermosa
        30. Campeche
        31. Merida
        32. Chetumal
        '''
        coordinates = [[2, height], [], ] 


    def generate(self):
        #Aqui se van a acomodar en dos arreglos, uno para X y el otro para Y, finalmente se regresa un column stack.
        xs = []
        ys = []

        return np.column_stack((xs, ys))
