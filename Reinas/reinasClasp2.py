from math import sqrt

import subprocess

try:
    # Replace 'command' with your actual command
    command = ["ls", "-l"]
    result = subprocess.run(command, capture_output=True, text=True)
    result.check_returncode()  # Raises CalledProcessError if the exit code is non-zero
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
except FileNotFoundError as e:
    print(f"Command not found: {e}")

import sys

from typing import List




def reinas(n: int) -> None:

    """

    Genera un archivo en formato DIMACS para el problema de las N reinas de ajedrez.



    :param n: Número de reinas.

    """

    casilla = []



    # Por optimización, guardar `range(n)` en una variable, en lugar de calcularlo cada vez

    range_n = range(n)



    # Al menos una reina en cada fila

    for i in range_n:

        casilla.append([n * i + j + 1 for j in range_n])



    # Una reina por fila

    for i in range_n:

        for j in range_n:

            for k in range(j + 1, n):

                casilla.append([-((n * i + j) + 1), -((n * i + k) + 1)])



    # Una reina por columna

    for j in range_n:

        for i in range_n:

            for k in range(i + 1, n):

                casilla.append([-((n * i + j) + 1), -((n * k + j) + 1)])



    # Una reina por diagonal

    for i in range_n:

        for j in range_n:

            for k in range(i + 1, n):

                for l in range_n:

                    if abs(i - k) == abs(j - l):

                        casilla.append([-((n * i + j) + 1), -((n * k + l) + 1)])



    # En lugar de imprimir las cláusulas, se podrían guardar en un archivo

    clausulas = f"p cnf {n**2} {len(casilla)}\n"

    for clausula in casilla:

        clausulas += f"{' '.join(map(str, clausula))} 0\n"

    with open(f"reinas_{n}.cnf", "w") as f:

        f.write(clausulas)



    # Se podría invocar directamente Clasp para que procese el archivo con las claúsulas, y

    # guardar el resultado a un nuevo archivo

    subprocess.run(

        ["clasp", f"reinas_{n}.cnf"],

        stdout=open(f"reinas_{n}_solucion.txt", "w"),

        text=True,

    )



    # Por último, se podría leer el archivo con la solución y mostrarla en pantalla en forma de tablero

    with open(f"reinas_{n}_solucion.txt") as f:

        sol_clasp = f.readlines()

    try:

        procesa_salida_clasp(sol_clasp)

    except:

        print(

            "La salida de Clasp no se pudo procesar. Es posible que no haya solución. Revise los archivos intermedios."

        )

        sys.exit(1)





def procesa_salida_clasp(salida: List[str]) -> None:

    """

    Procesa la salida de Clasp e imprime el tablero con la solución.



    :param salida: Salida de Clasp.

    """

    # Filtra sólo las líneas que comienzan con `v`

    salida = list(filter(lambda x: x.startswith("v"), salida))

    # Elimina el `v` del inicio de cada línea y el `0` del final

    salida = [x.replace("v ", "").replace(" 0", "").strip() for x in salida]

    # Aplana la lista, separando los números y convirtiéndolos a enteros

    salida = list(map(int, " ".join(salida).split()))



    # Determina el tamaño del tablero

    n = int(sqrt(max([abs(x) for x in salida])))



    # Imprime el tablero

    print(f"Solución para un tablero de {n}x{n}:")

    for i in range(0, len(salida) - 1, n):

        print(" ".join("Q" if x > 0 else "." for x in salida[i : i + n]))





# Acepta un argumento `n`, que es el número de reinas, cuyo valor por defecto sería 8

if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == "-h":

        print("Uso: reinasClasp.py [n]")

        print("Genera un archivo en formato DIMACS para el problema de las n reinas")

        print("Argumentos:")

        print("  n: número de reinas (por defecto 8)")

        sys.exit(0)



    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8



    reinas(n)

