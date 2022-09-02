#binario entero a decimal

def binario_entero_a_decimal(num=None):
    if num == None:
        num = input("ingresar número binario entero a pasar a decimal: ")
    else:
        pass
    exponenteMax = len(num)-1
    exponente = -1
    total = 0
    aux = int(num)
    while exponente < exponenteMax:
        resto = aux % 10
        exponente = exponente +1
        total = total + resto * (2**(exponente))
        aux = aux//10


    return (num, str(total))

if __name__ == "__main__":

##    (num, resultado) = binario_entero_a_decimal()
    #import sys
    #(num, resultado) = binario_entero_a_decimal(sys.argv[1])
    (num, resultado) = binario_entero_a_decimal()
    print("El número {} en binario es: {}".format(num, resultado))
