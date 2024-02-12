

def reinas(n):
    casilla = []

    # Al menos una reina en cada fila
    for i in range(n):
        casilla.append([n*i + j + 1 for j in range(n)])

    # Una reina por fila
    for i in range(n):
        for j in range(n):
            for k in range(j+1, n):
                casilla.append([-((n*i + j) + 1), -((n*i + k) + 1)])

    # Una reina por columna
    for j in range(n):
        for i in range(n):
            for k in range(i+1, n):
                casilla.append([-((n*i + j) + 1), -((n*k + j) + 1)])

    # Una reina por diagonal
    for i in range(n):
        for j in range(n):
            for k in range(i+1, n):
                for l in range(n):
                    if (abs(i - k) == abs(j - l)):
                        casilla.append([-((n*i + j) + 1), -((n*k + l) + 1)])

    # Salida de datos
    print(f"p cnf {n**2} {len(casilla)}")
    for clausula in casilla:
        print(" ".join(map(str, clausula)) + " 0")



n = int(input("Introduce el número de reinas: "))
reinas(n)