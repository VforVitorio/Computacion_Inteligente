### Problema de las n reinas.

[Pulsa aquí para volver al readme del repositorio](../README.md)

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
