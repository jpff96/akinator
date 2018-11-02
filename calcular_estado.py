import numpy as np
def calcular_estado(candidatos_viejos, opciones, eliminar):
    candidatos = candidatos_viejos

    for i in range(0,np.size(eliminar,0)):
        indx = eliminar[i] - i
        
        candidatos = np.delete(candidatos,indx,0) #VER ESTO
        print(candidatos)
    
    repeticiones = np.zeros((np.size(opciones,0),np.size(opciones,1)), dtype=int)
    for j in range(0,np.size(opciones,0)-1):
        for k in range(0,np.size(opciones,1)):
            a = (opciones[i,j] == candidatos)
            repeticiones[i,j] = sum(sum(a))

    estado = repeticiones
    return estado,candidatos
    