
def hexadecimal_entero_a_decimal(num=None):
    if num == None:
        num = input("ingresar numero entero hexadecimal a pasar a decimal: ")
    else:
        pass
    cifras = ['A', 'B', 'C', 'D', 'E', 'F']
    valores = [10, 11, 12, 13, 14, 15]
    tabla = zip(cifras, valores)
    print(list(tabla))
    tabla = dict(tabla)
    print(tabla)
    tabla = dict(zip(cifras, valores))
    print(tabla)
    resultado = ""
    while (num//10!=0 and ):
        pass
    return (num, resultado)

if __name__ == "__main__":

    import sys
    (num, resultado) = hexadecimal_entero_a_decimal(12)    #sys.argv[1]; como hago una lista de argumentos
    print("numero hexadecimal {} en decimal es: {}\n".format(num, resultado))
