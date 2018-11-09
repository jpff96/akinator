# -*- coding: utf-8 -*-
import numpy as np
import math
from django.shortcuts import render
from django.http import HttpResponse
from akinator.models import Users
import csv

def init(request):
	global año_nacimiento
	año_nacimiento = "¿Nació en el "
	global p_Sexo
	p_Sexo = "¿Su sexo es "
	global p_Pelo
	p_Pelo = "¿Su color de Pelo es "
	global altura
	altura = "¿Lo considera "
	global p_Deporte
	p_Deporte = "¿Su Deporte favorito es "
	global vacaciones
	vacaciones = "¿Pasa sus vacaciones en "
	global instrumento
	instrumento = "¿Toca la/el "
	global p_Interior
	p_Interior = "¿Es del Interior? "
	global ciudad_nacimiento
	ciudad_nacimiento = "¿Nació en "
	global barrio
	barrio = "¿Vive en el barrio "
	global rol
	rol = "¿Su personaje es un "
	global materia
	materia = "¿Su profesor/a da la materia "
	global asesora
	asesora = "¿Es asesor "
	global carrera
	carrera = "¿Estudia la carrera "
	global generacion
	generacion = "¿Es de la generación "
	global asesor
	asesor = "¿su asesor es "
	global secundaria
	secundaria = "¿Hizo la secundaria en "
	global fellow
	fellow = "¿Es su personaje un fellow?"
	global ayudante
	ayudante = "¿Es su personaje ayudante de algún curso?"
	global al_dia
	al_dia = "¿Está con la carrera "
	global caracteristica
	global mensaje
	global primera_vez
	primera_vez = True
	global opciones
	opciones = np.array([["2000","1999","1998","1997","1996","1995","1994","1993","1957","1962","1974","1970","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Hombre", "Mujer", "Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Rubio", "Castaño", "Morocho","Colorado","Blanco","Pelado","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Alto (1,80m o +)","Medio (de 1,70m a1,80m)","Bajo (de 1,50m a 1,70m)","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Rugby", "Football", "Gimnasia","Tennis","Bridge","Taekwondo","Correr","Volleyball","Handball","Bicicleta","Natación","Basketball","Hockey","Gimnasio","Remo","Crossfit","Boxeo","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Playa Verde","Punta del Este","En el exterior","Punta Ballena","La Pedrera","Paysandú","Atlantida","Cuchilla Alta","Pueblo Chico Agroturismo", "Florianopolis", "La Tuna", "Piriápolis", "Punta del Diablo","La Paloma", "Rocha", "Santa Ana", "Brasil", "Manantiales", "Fomento","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Piano","Ninguno","Guitarra","Bajo","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Montevideo", "Interior", "Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Paysandú", "Salto","Maldonado", "Canelones", "Rivera", "Tacuarembó", "San Jose", "Soriano","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Carrasco", "Pocitos", "Parque Miramar", "Prado", "Colonia Nicolich", "Cerro", "Malvin", "Centro", "Punta Carretas", "Ituzaingo", "Unión", "Punta Gorda", "Barra de Carrasco","Brazo Oriental","Buceo","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Soy Estudiante","Soy Profesor", "Soy Funcionario","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],	
	["Sistemas Distribuidos", "Matlab", "Análisis Matemático","Sistemas Lineales","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Si", "No", "Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Ingenieria Telematica", "Ingenieria Industrial", "Ingenieria Civil","Ingenieria Informatica","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["2016","2018","2014","2017","2015","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Rafael Sotelo", "Daniel Jurburg", "Pepe Díaz", "Viviana Rocco", "Claudio Ruibal", "Adrián Santilli", "Martín Tanco","Analía Conde", "Fernando Machado", "Eduardo", "Gerardo Beltrame","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["PREU","La Mennais", "Crandon", "Stella Maris College", "Colegio Salesiano", "Scuola Italiana", "Instituto Uruguayo Argentino", "British School", "Canelones", "Colegio Maldonado", "Colegio y liceo nuestra señora del rosario", "Colegio Aleman","IHHC", "Liceo Dptal Nro. 1 Dra. Celia Pomoli", "Juan XXIII", "Colegio Seminario", "Saint Brendan's School", "Liceo 1 Paso de los Toros", "Liceo Damaso", "Liceo 1","Liceo departamental de San José de Mayo", "Elbio Fernández","Santa Rita", "Santa Luisa de Marillac","PUC","Colegio San Pablo","IAVA","Pinar 1"],
	["Si", "No", "Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Si", "No", "Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"],
	["Al dia", "Me atrase un 02, pero vamo arriba", "Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"]
	])
	global preguntas
	preguntas = np.array([año_nacimiento,p_Sexo,p_Pelo, altura, p_Deporte, vacaciones, instrumento, p_Interior, ciudad_nacimiento, barrio, rol, materia, asesora, carrera, generacion,asesor, secundaria, fellow, ayudante, al_dia])

    
	global tabla
	tabla = np.array([['Nombre completo','año nacimiento','sexo','color de pelo','altura','deporte','vacaciones','instrumento','int/montevideo','departamento','barrio','profesion','materias dadas','asesora','carrera','comienzo carrera','asesor','secundaria','fellow','ayudante','avance carrera']])
	dataReader = csv.reader(open("./akinator/static/akinator_data.csv"), delimiter=',', quotechar='"')
	for row in dataReader:
		user=Users()
		if (row[0] == 'Ignacio Blanco' or row[0] == 'Juan Fajardo'):
			print(row)
		tabla = np.insert(tabla,np.size(tabla,0),row,axis=0)
	print (tabla)
	global repeticiones
	repeticiones =  np.zeros((np.size(opciones,0),np.size(opciones,1)), dtype=int)
	global candidatos
	candidatos = tabla[1:np.size(tabla,0),0:np.size(tabla,1)]
	global estado
	estado = repeticiones
	for i in range (0,np.size(opciones,0)):
	    for j in range (0,np.size(opciones,1)):
	        a = (opciones[i,j]==tabla)
	        repeticiones[i,j] = sum(sum(a))

	estado = repeticiones
	candidatos = tabla[1:np.size(tabla,0),0:np.size(tabla,1)]
	request.session['candidatos'] = candidatos.tolist()
	request.session['estado'] = estado.tolist()




# Create your views here.
def home(request):
	return render(request,'akinator/index.html')



def answer(request):
	return render(request,'akinator/answer.html')

def pregunta_seleccionada(request):
	candidatos = np.asarray(request.session.get('candidatos', 0))
	estado = np.asarray(request.session.get('estado', 0))
	if np.size(candidatos,0) > 1:
		n = np.size(candidatos,0)

		dif_min = math.inf
		min_pos = np.array([0,0])
		for i in range(0,np.size(estado,0)):
			for j in range(0,np.size(estado,1)):
				if(abs(estado[i,j] - n/2) < dif_min and estado[i,j] !=0):
					dif_min = abs(estado[i,j] - n/2)
					min_pos = [i,j]

		pos_caract = min_pos
		caracteristica = opciones[pos_caract[0],pos_caract[1]]
		request.session['pos_caract'] = pos_caract
		if pos_caract[1] == 4:
			mensaje = p_Interior
			request.session['mensaje'] = mensaje
			request.session['caracteristica'] = caracteristica
		else:
			mensaje = preguntas[pos_caract[0]] + ' ' + caracteristica + '?'
			request.session['mensaje'] = mensaje
			request.session['caracteristica'] = caracteristica

def prototipo_akinator(request):
	resp = request.POST.get("yes")

	candidatos = np.asarray(request.session.get('candidatos', 0))
	estado = np.asarray(request.session.get('estado', 0))
	caracteristica = request.session.get('caracteristica',0)
	pos_caract = request.session.get('pos_caract',0)
	eliminar = np.asarray(request.session.get('eliminar',0))

	if np.size(candidatos,0) > 1:
		if resp == 'Si':

			indexes = np.argwhere(candidatos==caracteristica)
			filas = np.zeros(len(indexes), dtype=int)
			contador = 0
			for j in indexes:
				filas[contador] = j[0]
				contador = contador + 1
			contador = 0
			eliminar = np.setdiff1d(np.arange(0,np.size(candidatos,0),1),filas)
			request.session['eliminar'] = eliminar.tolist()
		# eliminar = np.subtract(np.arange(0,np.size(candidatos,0),1),filas)
		else:
			indexes = np.argwhere(candidatos==caracteristica)
			print('caracteristica')
			print(caracteristica)
			print(candidatos)
			filas = np.zeros(len(indexes), dtype=int)
			contador = 0
			for j in indexes:
				filas[contador] = j[0]
				contador = contador + 1
			contador = 0
			eliminar = filas
			request.session['eliminar'] = eliminar.tolist()
		
		for i in range(0,np.size(eliminar,0)):
			indx = eliminar[i] - i
			candidatos = np.delete(candidatos,indx,0)
			request.session['candidatos'] = candidatos.tolist()
		
		repeticiones = np.zeros((np.size(opciones,0),np.size(opciones,1)), dtype=int)
		print(eliminar)
		print('candidatos')
		print(candidatos)
		for j in range(0,np.size(opciones,0)-1):
			for k in range(0,np.size(opciones,1)):
				a = np.argwhere(opciones[j,k] == candidatos)
				if len(a) is not 0:
					repeticiones[j,k] = sum(sum(a))

		request.session['estado'] = repeticiones.tolist()
		estado[pos_caract] = 0 
	if np.size(candidatos,0) == 1 :
		request.session['personaje'] = candidatos[0,0]

def question(request):
	if request.POST.get('yes') == None and request.POST.get('no') == None:
		for key in list(request.session.keys()):
			del request.session[key]
		init(request)
		pregunta_seleccionada(request)
		print(request.session.get('mensaje',0))

	else:
		prototipo_akinator(request)
		pregunta_seleccionada(request)
		print(request.session.get('mensaje',0))

	#MODIFICAR LA PREGUNTA

	context = {'question' : request.session.get('mensaje',0) }
	#print(request.session.get('candidatos',0))

	if request.session.get('personaje') != None:
		context = {'personaje' : request.session.get('personaje',0) }

		return render(request, 'akinator/answer.html',context=context)
	return render(request,'akinator/question.html',context = context)
