# -*- coding: utf-8 -*-
import numpy as np
import calcular_estado
import elegir_caracteristica


p_Pelo = "¿Su color de Pelo es "
p_Deporte = "¿Su Deporte favorito es "
p_Sexo = "¿Su sexo es "
p_Interior = "¿Vive en el Interior? "

opciones = np.array([["Rubio", "Marron", "Morocho"],["Futbol", "Rugby", "Tennis"],["Masculino", "Femenino", "Invalid"],["Si", "No", "Invalid"]])

preguntas = np.array([p_Pelo, p_Deporte, p_Sexo, p_Interior])

tabla = np.array([['Nombre', 'Pelo', 'Deporte', 'Sexo', 'Interior'],['Juan', opciones[0,0], opciones[1,0], opciones[2,0], opciones[3,1]],['Pablo', opciones[0,1], opciones[1,1], opciones[2,0], opciones[3,0]],['Maria', opciones[0,2], opciones[1,2], opciones[2,1], opciones[3,1]],['Guillermina', opciones[0,0], opciones[1,2], opciones[2,1], opciones[3,0]],['Ricardo', opciones[0,1], opciones[1,0], opciones[2,0], opciones[3,0]]])

repeticiones =  np.zeros((np.size(opciones,0),np.size(opciones,1)), dtype=int)
for i in range (0,np.size(opciones,0)):
    for j in range (0,np.size(opciones,1)):
        a = (opciones[i,j]==tabla)
        repeticiones[i,j] = sum(sum(a))

estado = repeticiones
candidatos = tabla[1:np.size(tabla,0),0:np.size(tabla,1)]

while np.size(candidatos,0) > 1:
    n = np.size(candidatos,0)
    print(candidatos)
    pos_caract = elegir_caracteristica.elegir_caracteristica(estado,n-1)
    caracterisitica = opciones[pos_caract[0],pos_caract[1]]

    if pos_caract[1] == 4:
        mensaje = p_Interior + ' (Si/No): '
        print(mensaje)
        resp = input("")
    else:
        mensaje = preguntas[pos_caract[0]] +' '+ caracterisitica + "? (Si/No): "
        print(mensaje)
        resp = input("")
    if resp == 'Si':
        indexes = np.argwhere(candidatos==caracterisitica)
        filas = indexes[0]
        print(filas)
        print(indexes)
        eliminar = np.subtract(np.array([1,np.size(candidatos,0)]),filas)
        print(eliminar[0])
    if resp == 'No':
        indexes = np.argwhere(candidatos==caracterisitica)
        eliminar = indexes[0]
    [estado, candidatos] = calcular_estado.calcular_estado(candidatos, opciones, eliminar)
    estado[pos_caract] = 0 

print("Estas pensando en: " + candidatos[0,0])

