#decimal entero a binario

def decimal_entero_a_binario(num=None):
    if num == None:
        num = input("ingresar numero decimal a pasar a binario: ")
    else:
        pass
    dividendo = int(num)
    resultado = ""
    while (dividendo / 2) >= 1:
        resto = dividendo % 2
        resultado = str(resto) + resultado
        dividendo = dividendo // 2

    resto = dividendo % 2
    resultado = str(resto) + resultado
    return (num, resultado)

if __name__ == "__main__":

    import sys
    (num, resultado) = decimal_entero_a_binario(sys.argv[1])    #como hago una lista de argumentos
    print("numero {} en binario es: {}\n".format(num, resultado))
