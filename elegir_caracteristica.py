import numpy as np
import math
def elegir_caracteristica(estado,n):
    
    dif_min = math.inf
    min_pos = np.array([0,0])

    for i in range(0,np.size(estado,0)):
        for j in range(0,np.size(estado,1)):
            if(abs(estado[i,j] - (n+1)/2) < dif_min and estado[i,j] !=0):
                dif_min = abs(estado[i,j] - (n+1)/2)
                min_pos = [i,j]

    return min_pos