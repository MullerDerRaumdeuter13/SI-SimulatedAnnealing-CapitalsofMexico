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
        6. Monterrey (280, 150)
        7. Ciudad Victoria (290, 120)
        8. San Luis Potosi (40, 280)
        9. Zacatecas (90, 130)
        10. Durango (160, 130)
        11. Culiacan (130, 140)
        12. Tepic (150, 90)
        13. Guadalajara (160, 80)
        14. Colima (150, 70)
        15. Aguascalientes (180, 170)
        16. Tlaxcala (230, 70)
        17. Guanajuato (190, 90)
        18. Queretaro (200, 80)
        19. Pachuca (220, 70)
        20. Xalapa (240, 70)
        21. Puebla (230, 60)
        22. Cuernavaca (210, 60)
        23. CDMX (210, 70)
        24. Toluca (200, 65)
        25. Morelia (190, 70)
        26. Chilpancingo (220, 30)
        27. Oaxaca (250, 30)
        28. Tuxtla Gutierrez (290, 20)
        29. Villahermosa (280, 30)
        30. Campeche (320, 60)
        31. Merida (330, 80)
        32. Chetumal (350, 40)
        '''
        coordinates = [[40, 280], [90, 130], [80, 200], [140, 180], [200, 140], [280, 150], [290, 120], [200, 100], [190, 180], [160, 130], [130, 140], [150, 90], 
                        [160, 80], [150, 70], [180, 170], [230, 70], [190, 90], [200, 80], [220, 70],[240, 70], [230, 60], [210, 60], [210, 70], [200, 65], 
                        [190, 70], [220, 30], [250, 30], [290, 20], [280, 30], [320, 60], [330, 80],[350, 40]]

        #Aqui se van a acomodar en dos arreglos, uno para X y el otro para Y, finalmente se regresa un column stack.
        xs = []
        ys = []
        for coord in coordinates:
            xs.append(coord[0])
            ys.append(coord[1])

        return np.column_stack((xs, ys))
