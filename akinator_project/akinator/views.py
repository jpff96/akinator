# -*- coding: utf-8 -*-
import numpy as np
import math
from django.shortcuts import render

p_Pelo = "¿Su color de Pelo es "
p_Deporte = "¿Su Deporte favorito es "
p_Sexo = "¿Su sexo es "
p_Interior = "¿Vive en el Interior? "

opciones = np.array([["Rubio", "Marron", "Morocho"],["Futbol", "Rugby", "Tennis"],["Masculino", "Femenino", "Invalid"],["Si", "No", "Invalid"]])

preguntas = np.array([p_Pelo, p_Deporte, p_Sexo, p_Interior])

tabla = np.array([['Nombre', 'Pelo', 'Deporte', 'Sexo', 'Interior'],['Juan', opciones[0,0], opciones[1,0], opciones[2,0], opciones[3,1]],['Pablo', opciones[0,1], opciones[1,1], opciones[2,0], opciones[3,0]],['Maria', opciones[0,2], opciones[1,2], opciones[2,1], opciones[3,1]],['Guillermina', opciones[0,0], opciones[1,2], opciones[2,1], opciones[3,0]],['Ricardo', opciones[0,1], opciones[1,0], opciones[2,0], opciones[3,0]]])

repeticiones =  np.zeros((np.size(opciones,0),np.size(opciones,1)), dtype=int)

def init(opciones,repeticiones):
	for i in range (0,np.size(opciones,0)):
	    for j in range (0,np.size(opciones,1)):
	        a = (opciones[i,j]==tabla)
	        repeticiones[i,j] = sum(sum(a))

	estado = repeticiones
	candidatos = tabla[1:np.size(tabla,0),0:np.size(tabla,1)]
	return estado,candidatos




# Create your views here.
def home(request):
	return render(request,'akinator/index.html')

def question(request):
	estado,candidatos = init(opciones,repeticiones)
	mensaje = pregunta_seleccionada(candidatos,estado)
	print (mensaje)
	return render(request,'akinator/question.html')

def answer(request):
	return render(request,'akinator/answer.html')

def pregunta_seleccionada(candidatos,estado):
	if np.size(candidatos,0) > 1:
		n = np.size(candidatos,0)
		print(candidatos)

		dif_min = math.inf
		min_pos = np.array([0,0])
		for i in range(0,np.size(estado,0)):
			for j in range(0,np.size(estado,1)):
				if(abs(estado[i,j] - n/2) < dif_min and estado[i,j] !=0):
					dif_min = abs(estado[i,j] - n/2)
					min_pos = [i,j]

		pos_caract = min_pos
		caracterisitica = opciones[pos_caract[0],pos_caract[1]]

		if pos_caract[1] == 4:
		    mensaje = p_Interior + ' (Si/No): '
		    print(mensaje)
		    return mensaje
		else:
		    mensaje = preguntas[pos_caract[0]] +' '+ caracterisitica + "? (Si/No): "
		    return mensaje

def prototipo_akinator(request):
	resp = request.POST.get("yes")
	if resp == 'Si':
	    indexes = np.argwhere(candidatos==caracterisitica)
	    filas = np.zeros(len(indexes), dtype=int)
	    contador = 0
	    for j in indexes:
	        filas[contador] = j[0]
	        contador = contador + 1
	    contador = 0
	    
	    eliminar = np.setdiff1d(np.arange(0,np.size(candidatos,0),1),filas)
	    print('chau')
	   # eliminar = np.subtract(np.arange(0,np.size(candidatos,0),1),filas)
	if resp == 'No':
	    indexes = np.argwhere(candidatos==caracterisitica)
	    filas = np.zeros(len(indexes), dtype=int)
	    contador = 0
	    for j in indexes:
	        filas[contador] = j[0]
	        contador = contador + 1
	    contador = 0
	    eliminar = filas

	for i in range(0,np.size(eliminar,0)):
		indx = eliminar[i] - i
		candidatos = np.delete(candidatos,indx,0)
	
	repeticiones = np.zeros((np.size(opciones,0),np.size(opciones,1)), dtype=int)
	for j in range(0,np.size(opciones,0)-1):
		for k in range(0,np.size(opciones,1)):
			a = np.argwhere(opciones[i,j] == candidatos)
			if len(a) is not 0:
				repeticiones[i,j] = sum(sum(a))

	estado = repeticiones
	estado[pos_caract] = 0 

	("Estas pensando en: " + candidatos[0,0])
	return render(request, 'akinator/question.html')


