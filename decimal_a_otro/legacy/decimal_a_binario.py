import math
##>>> import math
##>>> frac, whole = math.modf(2.5)
##>>> frac
##0.5
##>>> whole
##2.0

##>>> from decimal import Decimal
##>>> Decimal('4.20') % 1
##Decimal('0.20')

from decimal import Decimal


def decimal_a_binario(numero=None):
    if numero is None:
        numDec = input("ingrese numero decimal con coma en formato 'xxx.yyy' a pasar a binario:\n")
    else:
        numDec = numero
    numIngresado = numDec
    numDec = str(numDec)
    print()

    #divide entre parte entera y parte decimal
    print("Cuentas:")
    splitteado = numDec.split('.',)
    numDecE = int(splitteado[0])
    print("Parte entera", numDecE)
    numDecD = int(splitteado[1])
    print("Parte decimal", numDecD)
    print()

    ##pasaje a binario
    print("\nParte entera a pasar a binario:", numDecE)
    print()
##    numDecE = total
    posicion = 0
    resulBin = ""
    while numDecE >= 1:
        if posicion == 0:
            posicion = 1
        else:
            posicion = posicion * 10 
        print("posicion", posicion)
        resto = numDecE % 2
        resulBin = str(resto) + str(resulBin)
        print(resulBin)
        numDecE = numDecE // 2

    print("\nParte entera en binario: ", int(resulBin),"\n")

    
    ##procesa parte decimal
    print("procesa parte decimal")

    #pasaje a decimal de la parte de la coma octal
    print(numDecD, "a binario")
    print()
    print("Cuentas:")
    print("----------------")
    print("\nNúmero en base diez:", "0."+str(numDecD))
    binario = bin(numDecD)
    print("print(binario)[0:]")
    print(binario)
    print("print(binario)[1:]")
    print(binario[1:])
    print("print(binario)[2:]")
    print(binario[2:])
    binario = binario[2:]
    print("binario ahora corta la cadena", binario)

    print("Resultado decimal en binario:", binario,"\n")

    print('El número decimal ingresado "{}" es {} en binario'.format(numIngresado, str(resulBin)+"."+str(binario)))
    return str(resulBin)+"."+str(binario)

if __name__ == "__main__":
    decimal_a_binario()
