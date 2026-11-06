# Imos a implementar o xogo do tres en raia. Para iso imos a ir por partes.

# Lembra que o tablero é de 3 x 3. Fara representalo quizais sexa o mellor representalo cunha lista de listas,
# pero pode haber moitas outras representacións válidas e coas que te sintas máis cómodo.

#     Inicializa a estrutura a baleiro.
#     Imprime o taboleiro.
#     Podes facer que X represente unha ficha do xogador 1 e O a do xogador 2
#     Fai unha función que nos indique se temos un gañador ou non.
#     Utiliza test para comprobar os casos posibles, non teñen que ser todos, pero algúns si.
#     Implementa agora o proceso de xogo:
#         Primeiro un xogador, comproba se hai gañador, logo outro.
#         Paras cando un gaña ou xa non hai máis movementos.

def comprobar(taboleiro):

    liñas = list(taboleiro)
    liñas.extend(
        [[taboleiro[fila][columna] for fila in range(3)] for columna in range(3)]
    )
    liñas.append([taboleiro[i][i] for i in range(3)])
    liñas.append([taboleiro[i][2 - i] for i in range(3)])

    for liña in liñas:
        if liña == ["0", "0", "0"]:
            print("Gañou xogador 1")
            return True
        if liña == ["1", "1", "1"]:
            print("Gañou xogador 2")
            return True

    return False

def pedir_posicion(taboleiro, xogador):
    while True:
        try:
            fila = int(input(f"Xogador {xogador} introduza fila (1-{len(taboleiro)})\n")) - 1
            columna = int(input(f"Xogador {xogador} introduza columna (1-{len(taboleiro)})\n")) - 1
        except ValueError:
            print("Introduce números enteiros.")
            continue

        if not (0 <= fila < len(taboleiro) and 0 <= columna < len(taboleiro[fila])):
            print(f"Fila e columna deben estar entre 1 e {len(taboleiro)}.")
        elif taboleiro[fila][columna] != "":
            print("Esa posición xa está ocupada.")
        else:
            return fila, columna

def escribir(taboleiro):
    continuar = False
    ganador = False
    for filas in taboleiro:
        for celda in filas:
            if celda == "":
                continuar = True

    while continuar and not ganador:
        mostrar(taboleiro)
        bandera = True
        while bandera:
            fila, colum = pedir_posicion(taboleiro, 1)
            taboleiro[fila][colum] = "0"
            bandera = False
        mostrar(taboleiro)
        
        while not bandera and not ganador:
            fila, colum = pedir_posicion(taboleiro, 2)
            taboleiro[fila][colum] = "1"
            bandera = True
        if comprobar(taboleiro):
            ganador = True
        

def mostrar(taboleiro):
    for fila in taboleiro:
        print(fila)

if __name__ == '__main__':
    tamaño = 3
    i = 0
    taboleiro = list()
    while i != tamaño:
        taboleiro.append([""] * tamaño)
        i += 1

    
    escribir(taboleiro)
