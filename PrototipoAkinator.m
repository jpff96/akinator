clear; close all; clc;
%Cargado de base de datos
PPelo = "¿Su color de Pelo es ";
PDeporte = "¿Su Deporte favorito es ";
PSexo = "¿Su sexo es ";
PInterior = "¿Vive en el Interior?";

Opciones = {"Rubio", "Marron", "Morocho"; ...
            "Futbol", "Rugby", "Tennis"; ...
            "Masculino", "Femenino", "Invalid"; ...
            "Si", "No", "Invalid"};

Preguntas = {PPelo, PDeporte, PSexo,PInterior};

Tabla = ['Nombre', 'Pelo', 'Deporte', 'Sexo', 'Interior'; ...
         'Juan', Opciones(1,1), Opciones(2,1), Opciones(3,1), Opciones(4,2); ...
         'Pablo', Opciones(1,2), Opciones(2,2), Opciones(3,1), Opciones(4,1); ...
         'Maria', Opciones(1,3), Opciones(2,3), Opciones(3,2), Opciones(4,2); ...
         'Guillermina', Opciones(1,1), Opciones(2,3), Opciones(3,2), Opciones(4,1); ...
         'Ricardo', Opciones(1,2), Opciones(2,1), Opciones(3,1), Opciones(4,1)];

Repeticiones = zeros(size(Opciones));
for i=1:size(Opciones,1)
  for j=1:size(Opciones,2)
    a = strcmp(Opciones(i,j),Tabla);
    Repeticiones(i,j) = sum(sum(a));
  endfor
endfor

estado = Repeticiones;
candidatos = Tabla(2:6, 1:5);

while size(candidatos,1) > 1
  n = size(candidatos,1);
  posCaract = elegirCaracteristica(estado, n);
  caracteristica = Opciones(posCaract(1), posCaract(2));
  
  if(posCaract(2)==4)
    mensaje = strcat(PInterior, " (Si/No): ");
    disp(mensaje);
    resp = input("", "s");
  else
    mensaje = strcat(Preguntas(1,posCaract(1)), caracteristica(1), "? (Si/No): ");
    disp(mensaje);
    resp = input("", "s");
  end
  
  if(resp == 'Si')
    [x, y] = find(strcmp(candidatos, caracteristica));
    filas = x;
    eliminar = (setdiff([1:size(candidatos,1)],filas))';
  endif

  if(resp == 'No')
    [x,y] = find(strcmp(candidatos, caracteristica));
    eliminar = x;
  endif
  
  [estado, candidatos] = calcularEstado(candidatos, Opciones, eliminar);
  estado(posCaract)=0;
  
endwhile
msj = strcat("Estas pensando en: ", candidatos(1,1));
disp(msj);