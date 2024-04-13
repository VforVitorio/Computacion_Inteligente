% Ejercicio de las torres, parcial 01 Víctor Vega Sobral 

% Definimos el tamaño del tablero y el numero de torres. Por defecto le asignamos el valor n = 10
#const n = 10.

%Definimos que el tablero debe ser n*n con sus filas y columnas que vayan de 1 hasta n 
fila(1..n).
columna(1..n).

%Predicado para colocar en una posición determinada a la vez
1 { torre(X, Y) : fila(X) } 1 :- columna(Y).


%Restricción horizontal: solo puede haber una torre en cada fila

:- torre(X1, Y1), torre (X2,Y2), Y1 != X2.


%Restricción vertical: solo puede haber una torre en cada columna

:- torre(X1, Y1), torre (X2,Y2), Y2 != X1.

#show torre/2.