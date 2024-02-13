# Foro 03

## Enunciado

Una empresa de desarrollo software desea asignar tareas a un pequeño equipo de desarrollo de una IA como parte de un proyecto de la empresa. Cada tarea requiere de unos conocimientos y habilidades específicas y cada miembro posee especialización en una de estas habilidades. Dada la complejidad del desarrollo, cada miembro del equipo solo puede trabajar en una tarea a la vez. El objetivo es maximizar la eficiencia del equipo asignando las tareas de la forma adecuada.

### Tareas

Las tareas del proyecto son las siguientes, con su correspondiente habilidad requerida para la ejecución de la tarea:
• Desarrollo del modelo de IA: lenguaje Python.

• Entrenamiento: Machine Learning.

• Pruebas de validación: Testing.

• Optimización de hiperparámetros: Algoritmos de optimización.

• Despliegue en el proyecto: Docker.

### Miembros del equipo

Los miembros del equipo son los siguientes, con sus habilidades correspondientes.

• Juan: Python.

• María: Machine Learning.

• Carlos: Python.

• Laura: Testing.

• Mateo: Machine Learning.

• Pedro: Docker.

• Pablo: Docker.

• Antía: Docker.

• Lucía: Testing.

• Carmen: optimización.

• Pedro: optimización.

## Código de Clingo

El código al que hemos llegado consta de varias partes, entre las que podemos destacar:

1. La definición de habilidades:

```prolog
habilidad(python).
habilidad(machine_learning).
habilidad(testing).
habilidad(optimizacion).
habilidad(docker).
```

Empezamos el codigo definiendo cada una de las habilidades necesarias para la realización del proyecto

2. Definición de las tareas y habilidades necesarias para cada una:

```prolog
tarea(desarrollo_modelo_ia, python).
tarea(entrenamiento, machine_learning).
tarea(pruebas_validacion, testing).
tarea(optimizacion_hiperparametros, optimizacion).
tarea(despliegue_proyecto, docker).
```

Aquí se define el hecho tarea(NombreTarea, HabilidadRequerida) que dispone el nombre y habilidad necesaria para resolver la tarea.

3. Definición de los miembros del equipo y sus habilidades:

```prolog
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
```

Cada linea define el miembro(Nombre, Habilidad), que establece que un nombre del equipo tiene determinada habilidad

4. Las restricciones en si, entre las que encontramos dos.

   1. Para cada Tarea se requiere una habilidad, por lo que se debe asignar exactamente un miembro que tenga dicha habilidad a la tarea determinada.

   ```prolog
   1 { asignacion(Miembro, Tarea) : miembro(Miembro, Habilidad) } 1 :- tarea(Tarea, Habilidad).
   ```

   La primera parte de la linea:

   ```prolog
   1 { asignacion(Miembro, Tarea) : miembro(Miembro, Habilidad) } 1
   ```

   Es una construcción de cardinalidad que dice que exactamente un miembro debe ser asignado a una tarea. El miembro además debe poseer la habilidad requerida para la tarea.

   La segunda parte:

   ```prolog
   :- tarea(Tarea, Habilidad).
   ```

   Se trata del cuerpo de la regla, al activarse para cada tarea que requiere una habiliad.

   2. La segunda restricción hace que no se permita asignar a una persona a más de una tarea.

   La primera parte:

   ```prolog
   miembro(Miembro, _)
   ```

   Selecciona a cada miembro independientemente de su habilidad

   La segunda parte:

   ```prolog´
   #count { Tarea : asignacion(Miembro, Tarea) } > 1
   ```

   Cuenta el número de tareas a las que un miembro ha sido asignado. Si este número es mayor que 1, la regla se activa.
   El operador ":-" nos sirve para activar la regla. Si la parte de la izquierda es verdadera, la de la derecha debe serlo, activando esta restricción.

## Solución arrojada por Clingo

Lo primero que debemos hacer es activar nuestro entorno de Anaconda.

> [!CAUTION]
> Para activar el entorno, debemos primero realizar la instalación de Anaconda o Miniconda, creando un virtual de Python 3.10. Si no, nos saltará un error de que no existe dicho entorno.

En nuestro caso:

```powershell
conda activate clingo_env
```

> [!WARNING]
> Antes de usar conda, debemos de movernos al directorio donde tenemos nuestro archivo

Una vez activado, procedemos a usar el software Clingo, poniendo nuestro nombre de archivo:

```
clingo trabajos.lp
```

La salida arrojada por el programa es la siguiente:

```powershell
Reading from trabajos.lp
Solving...
Answer: 1
asignacion(carlos,desarrollo_modelo_ia) asignacion(maria,entrenamiento) asignacion(lucia,pruebas_validacion) asignacion(carmen,optimizacion_hiperparametros) asignacion(pedro,despliegue_proyecto)
SATISFIABLE

Models       : 1+
Calls        : 1
Time         : 0.004s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.000s
```

Por tanto, nuestro problema es satisfacible, es decir, se pueden asignar cada tarea a una persona con una determinadada habilidad.

Si ponemos un 0 despues del comando mostrado anteriormente, clingo nos dará todas las combinaciones posibles.

```powershell
SATISFIABLE

Models       : 24
Calls        : 1
Time         : 0.024s (Solving: 0.02s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.000s
```

En este caso se observa que hay 24 posibles soluciones, o lo que es lo mismo, 24 formas diferentes de asignar las tareas.

Clingo también ofrece todos los casos específicos, pero para que no sobrecarguemos de texto pondremos el numero 5 después del comando para ver 5 posibles soluciones de tareas.

```powershell
Reading from trabajos.lp
Solving...
Answer: 1
asignacion(carlos,desarrollo_modelo_ia) asignacion(maria,entrenamiento) asignacion(lucia,pruebas_validacion) asignacion(carmen,optimizacion_hiperparametros) asignacion(pedro,despliegue_proyecto)
Answer: 2
asignacion(carlos,desarrollo_modelo_ia) asignacion(maria,entrenamiento) asignacion(lucia,pruebas_validacion) asignacion(carmen,optimizacion_hiperparametros) asignacion(pablo,despliegue_proyecto)
Answer: 3
asignacion(carlos,desarrollo_modelo_ia) asignacion(maria,entrenamiento) asignacion(lucia,pruebas_validacion) asignacion(carmen,optimizacion_hiperparametros) asignacion(antia,despliegue_proyecto)
Answer: 4
asignacion(carlos,desarrollo_modelo_ia) asignacion(maria,entrenamiento) asignacion(laura,pruebas_validacion) asignacion(carmen,optimizacion_hiperparametros) asignacion(pablo,despliegue_proyecto)
Answer: 5
asignacion(carlos,desarrollo_modelo_ia) asignacion(maria,entrenamiento) asignacion(laura,pruebas_validacion) asignacion(carmen,optimizacion_hiperparametros) asignacion(antia,despliegue_proyecto)
SATISFIABLE

Models       : 5+
Calls        : 1
Time         : 0.007s (Solving: 0.01s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.000s
```

Por ejemplo, la respuesta 1 sugiere asignar a carlos el desarrollo del modelo de IA, María su entrenamiento, Lucía las pruebas de validación, Carmen las optimizaciones de los algoritmos y Pedro el despliegue del proyecto.
