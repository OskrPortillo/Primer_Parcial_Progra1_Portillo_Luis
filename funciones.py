from UTN_Heroes_Dataset.utn_pp import get_original_matrix
import random


def obtener_existencias(matriz_concesionaria)-> list[list]:

    matriz = []

    cantidad_filas = len(matriz_concesionaria[1])
    print(cantidad_filas)

    for i in  range(cantidad_filas):
        for j in range(len(matriz_concesionaria[i])):
            matriz.append(matriz_concesionaria[i][j]) #modelo
        matriz.append(matriz_concesionaria[i][])

