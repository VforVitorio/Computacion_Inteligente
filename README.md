# Repositorio de Computación Inteligente.

## Descripción.

Este es el archivo readme donde se irán añadiendo todos los programas realizados en la asignatura de computación inteligente.

> [!WARNING]
> Este es un repositorio en constante desarrollo. El archivor readme se irá actualizando conforme vayan surgiendo nuevos proyectos a realizar.

### Problema de las n reinas.

#### Descripción del problema.

Deseamos implementar un programa en Python o C que reciba un parámetro n y codifique las restricciones SAT para resolver el problema de las N reinas, siendo N la n que ingrese el usuario.

##### OBJETIVOS

1. Establecer las restricciones en lógica proposicional.

   1. Pasar a la Forma Normal Conjuntiva.

2. Implementar las restricciones en Pyhton usando la forma normal conjuntiva.

3. Poner las restricciones en formato DIMACS, para poder ser interpretado por Clasp

4. Mediante Clasp, obtener el numero de soluciones posibles.

> [!IMPORTANT]
> Es necesario recordar la sintaxis del formato DIMACS, por lo que se proporciona un ejemplo a continuación:
>
> ```
> c (-p\/-r\/t) /\ (-p \/-r \/-u) /\ (-q \/s \/t) /\ (-q \/s \/-u)
> c p = 1, q = 2, r = 3, s = 4, t =5, u = 6
> c Cada clausula es una linea
> c 6 átomos 4 clausulas
> p cnf 6 4
> -1 -3 5 0
> -1 -3 -6 0
> -2 4 5 0
> -2 4 -6 0
> ```
>
> ## Proposiciones
>
> Las filas y columnas las denomtamos como "i" y "j". Estos dos símbolos van a estar presentes en todas nuestras proposicones
>
> ## i
>
> Proposición R<sub>ij representa una casilla del tablero donde se encuentra una reina. A partir de ella podremos definir las retricciones.
>
> ### Restricciones
>
> 1. Filas
> 2. Columnas
> 3. Diagonales
>    3.1 Principal
>    3.2 Inversa
>    Restricción de fila
>    Podemos expresarla como proposición F<sub>i , que asegura que no hay más de una reina en la fila

Fi = (Pi1 \/ Pi2.... \/ Pin) /\ -(Pi1 /\ Pi2) /\ -(Pi1 /\ Pi3) /\ ... /\ -(Pi(n-1) /\ Pin)

Se compone la primera parte:

                     (Pi1 \/ Pi2.... \/ Pin)

que represente todas las disyuniones Rij para la fila i. Es decir qe al menos una de las variables para la fila i. Es decir, que al menos una de las variables Rij debe ser verdadera para que la fila i tenga una reina.

La segunda parte

-(Pij /\ Pi2) /\

Cada bloque de negación asegura que dos variables Pij puedan ser ambas verdaeras, lo que implica que no pueda haber dos reinas en la misma fila.
