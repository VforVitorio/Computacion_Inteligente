% reinas.lp 

% Define el tamaño del tablero y el numero de reinas. Por defecto, 8
#const n = 8.

%Define el dominio del tablero por filas y por columnas
fila(1..n).
columna(1..n).

%Define un predicado para colocar en una posición determinada a la vez
1 { reina(X, Y) : fila(X) } 1 :- columna(Y).


%Restricciones para evitar que una reina se ataque con otra
%Restricción horizontal 
%...
:- reina(X, Y1), reaina (X,Y2), Y1 != X2.



%Restricción vertical
%...
:- reina(X, Y1), reaina (X,Y2), X1 != X2.

%Restricciones diagonales
%...
:- reina(X1, Y1), reina(X2, Y2), X1 + Y1 = X2 + Y2.
:- reina(X1, Y1), reina(X2, Y2), X1 - Y1 = X2 - Y2.

#show reina/2.