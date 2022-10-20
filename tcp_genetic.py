from ctypes import pointer
import math

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
cityIndex = {"Mexicalli": [40, 280], "La Paz": [90, 130], "Hermosillo":[80, 200], "Chihuahua": [140, 180], "Saltillo": [200, 140], "Monterrey": [280, 150], 
             "Ciudad Victoria": [290, 120], "San Luis Potosi": [200, 100], "Zacatecas": [190, 180], "Durango": [160, 130], "Culiacan": [130, 140], "Tepic": [150, 90], 
             "Guadalajara":[160, 80], "Colima": [150, 70], "Aguascalientes": [180, 170], "Tlaxcala":[230, 70], "Guanajuato": [190, 90], "Queretaro": [200, 80], "Pachuca":[220, 70],
             "Xalapa": [240, 70], "Puebla":[230, 60], "Cuernavaca":[210, 60], "CDMX":[210, 70], "Toluca":[200, 65], "Morelia":[190, 70], "Chilpancingo":[220, 30], 
             "Oaxaca":[250, 30], "Tuxtla Gutierrez": [290, 20], "Villahermosa": [280, 30], "Campeche":[320, 60], "Merida":[330, 80], "Chetumal": [350, 40]}

def calculateDist(a, b):
    return math.sqrt(
                    (((a[0] - b[0])**2) 
                     + ((a[1] - b[1]) **2))
                    ) 

def geneticAlgorithm(cityIndex):
    ruta = "La Paz --> Mexicalli --> Hermosillo"
    distanciaForzosa = calculateDist(cityIndex["La Paz"], cityIndex["Mexicalli"]) + calculateDist(cityIndex["Mexicalli"], cityIndex["Hermosillo"])
    cityIndex.pop("La Paz")
    cityIndex.pop("Mexicalli")
    pointer = cityIndex["Hermosillo"]
    pointerCity = "Hermosillo"
    while len(cityIndex) > 1:
        ruta += " --> "
        cityIndex.pop(pointerCity)
        dist_list = []
        keyList = []
        for key in cityIndex:
            dist_list.append(calculateDist(pointer, cityIndex[key]))
            keyList.append(key)
        minimalDist = min(dist_list)
        index_ofMinimal = dist_list.index(minimalDist)
        pointerCity = keyList[index_ofMinimal]
        pointer = cityIndex[pointerCity]
        ruta += pointerCity
        print(ruta)
    return ruta
        
        
            
            
    

def main():
    ruta = geneticAlgorithm(cityIndex)
    print("Esta es la ruta a seguir!! \n", ruta)

    
    
    

main()
    