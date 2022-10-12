import random
import numpy as np

class NodeGenerator:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.nodesNumber = nodesNumber
        


    def generate(self):
        #Aqui se anotan las coordenadas X y Y de las capitales 
        '''
        Las capitales iran en el siguiente orden:
        1. Mexicalli (40, 250)
        2. La Paz (90, 130)
        3. Hermosillo (80, 200)
        4. Chihuahua (140, 180)
        5. Saltillo (200, 140)
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
        16. Tlaxcala
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
        coordinates = [[40, 280], [90, 130], [80, 200], [140, 180], [200, 140], [280, 150], [290, 120], [200, 100], [190, 180], [160, 130], [130, 140], [150, 90], [190, 80], [180, 70], [180, 170], [230, 70], [190, 90], [200, 80], 
        [220, 70], [240, 70], [230, 60], [210, 70], [200, 80], [190, 70], [220, 30], [250, 30], [290, 20], [280, 30], [320, 60], [330, 80], [350, 40]] 
        #Aqui se van a acomodar en dos arreglos, uno para X y el otro para Y, finalmente se regresa un column stack.
        xs = []
        ys = []
        for coord in coordinates:
            xs.append(coord[0])
            ys.append(coord[1])

        return np.column_stack((xs, ys))
