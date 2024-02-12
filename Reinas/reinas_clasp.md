# Problema de las n reinas.

[Pulsa aquí para volver al readme del repositorio](../README.md)

## Descripción del problema.

Deseamos implementar un programa en Python o C que reciba un parámetro n y codifique las restricciones SAT para resolver el problema de las N reinas, siendo N la n que ingrese el usuario.

## OBJETIVOS

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

 ## Proposiciones

 Las filas y columnas las denomtamos como "i" y "j". Estos dos símbolos van a estar presentes en todas nuestras proposicones

 Proposición P<sub>ij</sub> representa una casilla del tablero donde se encuentra una reina. A partir de ella podremos definir las retricciones.

 ### Restricciones

 * Filas
 * Columnas
 * Diagonales
   * 3.1 Principal
   * 3.2 Inversa


### Restricción de fila
Podemos expresarla como proposición F<sub>i</sub>, que asegura que no hay más de una reina en la fila

Fi = (P<sub>i1</sub> \ / P<sub>i2</sub>.... \ / P<sub>in</sub>) /\ -(P<sub>i1</sub> /\ P<sub>i2</sub>) /\ -(P<sub>i1</sub> /\ P<sub>i3</sub>) /\ ... /\ -(P<sub>i(n-1)</sub> /\ P<sub>in</sub>)

#### Primera parte:

(P<sub>i1</sub> \/ P<sub>i2</sub>.... \/ P<sub>in</sub>)

que representa todas las disyuniones P<sub>ij</sub> para la fila i. Es decir que al menos una de las variables para la fila i. Es decir, que al menos una de las variables P<sub>ij</sub> debe ser verdadera para que la fila i tenga una reina.

#### Segunda parte

-(P<sub>ij</sub> /\ P<sub>i2</sub>) /\ -(P<sub>i(n-1)</sub> /\ P<sub>in</sub>)

Cada bloque de negación asegura que dos variables P<sub>ij</sub> puedan ser ambas verdaeras, lo que implica que no pueda haber dos reinas en la misma fila.

### Restricción de columna

La proposición C<sub>j</sub> sirve ara establecer que no habrá más de una reina por columna

C<sub>j</sub> = (P<sub>ij</sub> \ / P<sub>2j</sub>.... \ / P<sub>nj</sub>) /\ -(P<sub>1j</sub> /\ P<sub>2j</sub>) /\ (P<sub>1j</sub> /\ P<sub>3j</sub>) ... /\ (P<sub>(n-1)</sub> /\ P</sub>nj</sub>)

#### Primera parte 

Establece el conjunto de disyunciones P<sub>ij</sub> para la columna j. Eso impllica que al menos una P<sub>ij</sub> debe ser verdadera para que exista una reina en esa columna

#### Segunda parte 
Es un conjunto de conjunciones negadas, es decir, que no pueder ser ambas verdadera para la comlumna j. De esta forma, no habrá más de una reina por columna.

## Diferencia entre diagonales 
### Principales

* Izquierda a derecha en el tablero
* La fila y la columna de las celdas en diagonal principal tienen la misma diferencia.
* En un tablero N*N existen N-1 diagonales principales

### Secundarias

* De derecha a izquierda en el tablero
* La suma de la fila y la columna de las celdas en la diagonal secundaria es constante
* Existen N-1 diagonales secundarias en un tablero N*N

#### Restricción de diagonales principales
Las diagonales principales que van de izquierda a drecha se puden expresar como la proposición Di

D<sub>i</sub> = (P<sub>11</sub> \ / P<sub>22</sub> ... \ / P<sub>ij</sub>) /\ -(P<sub>11</sub> /\ P<sub>22</sub>) /\ -(P<sub>11</sub> /\ P<sub>33</sub>) /\-(P<sub>(i-1)</sub> /\ P<sub>ij</sub>)

Esto nos indica que no habrá más de una reina en la diagonal principal que comienza en (i,j)
#### Restricción de diagonales secundarias

En este caso, de derecha a izquierda, asegura que no hay más de una reina en la diagonal secundaria, representada por Si

Si = (Pn1 \ / P(n-1)2 ... \ / Pij) -(Pni /\ P(n-1)2) /\ -(Pn1 /\ P(n-1)3) /\ ... /\ -(Pij /\ P2(i-1))

La primera parte, formada pro disyunciones, indica que al menos una reina debe estar presente en la diagonal secundaria i.
En la segunda parte de negaciones de conjunciones, se indica que no hay más de una reina en la diagonal secundaria i.

### Paso a FNC
Para expresar todas las variables o restricciones en la forma normal conjuntiva, debemos hacer la conjuncioón de todas ellas y negar la conclución.
La conclusión:

>[!IMPORTANT]
>
> &exist;P<sub>11</sub> /\ P<sub>22</sub> /\ &exist;P<sub>nn</sub> 

Al negar esta conclusion expresamos qué configuraciones no deberían ser válidas de acuerdo a las restricciones. Por tanto, la FNC para n = 4 sería:

(F1 /\ F2 /\ F3 /\ F4) /\ (C1 /\ C2 /\ C3 /\ C4) /\ (D1 /\ D2 /\ D3 /\ D4) /\ (S1 /\ S2 /\ S3 /\ S4) /\ -(P11 /\ P22)

Como se puede ver, hemos usado las variables **F,C,D y S** para abreviar una fórmula en la FNC