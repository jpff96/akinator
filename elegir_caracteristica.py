import numpy as np
import math

def elegir_caracteristica(estado,n):
    
    dif_min = math.inf
    posibles = np.array([0,0])
    min_pos = np.array([0,0])

    for i in range(0,np.size(estado,0)):
        for j in range(0,np.size(estado,1)):
            if(abs(estado[i,j] - n/2) < dif_min and estado[i,j] !=0):
                dif_min = abs(estado[i,j] - n/2)
                posibles = [i,j]

            if(abs(estado[i,j] - n/2) == dif_min and estado[i,j] !=0):
                posibles = [[posibles],[i,j]]


    min_pos = posibles[random.randint(0,len(posibles),:]

    return min_pos