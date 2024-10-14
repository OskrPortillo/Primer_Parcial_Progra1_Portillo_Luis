
def validar_opcion(minimo: int, maximo: int)-> int:
    """
    Funcion que solicita al usuario que ingrese una opcion dentro de un 
    rango determinado y valida esa opcion.
    Args:
        minimo (int): valor minimo para la opcion
        maximo (int): valor maximo para la opcion

    Returns:
        int: el valor valido que el usuario ingreso
    """

    opcion = input(f"Ingrese una opcion [{minimo} - {maximo}]: ")

    if not opcion or not opcion.isdigit() or not (minimo <= int(opcion) <= maximo):
        return validar_opcion(minimo, maximo)
    
    return int(opcion)


if __name__ == '__main__':
    op = validar_opcion(1,9)
    print (op)