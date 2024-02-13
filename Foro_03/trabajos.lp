% Definir las habilidades
habilidad(python).
habilidad(machine_learning).
habilidad(testing).
habilidad(optimizacion).
habilidad(docker).


% Definir las tareas y las habilidades necesarias para cada una
%Aquí se define el hecho tarea(NombreTarea, HabilidadRequerida)

tarea(desarrollo_modelo_ia, python).
tarea(entrenamiento, machine_learning).
tarea(pruebas_validacion, testing).
tarea(optimizacion_hiperparametros, optimizacion).
tarea(despliegue_proyecto, docker).

% Definir los miembros del equipo y sus habilidades
%Cada linea define el miembro(Nombre, Habilidad)





miembro(juan, python).
miembro(maria, machine_learning).
miembro(carlos, python).
miembro(laura, testing).
miembro(mateo, machine_learning).
miembro(pedro, docker).
miembro(pablo, docker).
miembro(antia, docker).
miembro(lucia, testing).
miembro(carmen, optimizacion).  

% Un miembro que tiene una habilidad para cada tarea
%Primera palabra antes de flecha
%Es una construcción de cardinalidad que dice que exactamente un miembro 
%debe ser asignado a una tarea. 
%El miembro además debe poseer la habilidad requerida para la tarea.


1 { asignacion(Miembro, Tarea) : miembro(Miembro, Habilidad) } 1 :- tarea(Tarea, Habilidad).

% Cada miembro del equipo solo puede trabajar en una tarea a la vez
%Primera parte selecciona a cada miembro independientemente de su habilidad

%Segunda parte count cuenta el numero de tareas a las que un miembro del equipo
ha sido asignado. Si es mayor que uno se activa la flecha que activa la restricción.

:- miembro(Miembro, _), #count { Tarea : asignacion(Miembro, Tarea) } > 1.


% Mostrar las asignaciones
#show asignacion/2.