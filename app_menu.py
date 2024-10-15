from UTN_Heroes_Dataset.utn_pp import (clear_console, mostrar_matriz_texto_tabla)
from salida_consola import mostrar_menu
from validacion import validar_opcion
from funciones import obtener_existencias

matriz_actual = []

def concesionaria_app (matriz_concesionaria: list[list]):
    
    while True:

        mostrar_menu()
        opcion = validar_opcion (1,9)

        match opcion:
            case 1:
                obtener_existencias(matriz_concesionaria)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break
             
        clear_console()
