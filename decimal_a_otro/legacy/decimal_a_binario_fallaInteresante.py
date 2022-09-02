def decimal_a_binario():
    numDec = input("ingrese numero decimal con coma en formato 'xxx.yyy' a pasar a binario:\n")
    numIngresado = numDec
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
    numDecD = "0."+str(numDecD)

    #pasaje a binario de la parte pasada a decimal
    print(numDecD, "a binario")
    posicion = "0.0"
    decimalBinario = ""
    numDecD = str(numDecD)
    numDecD = float(numDecD)
    print(numDecD)
    while numDecD != 0:
        numDecD = numDecD * 2
        print("mult por 2", numDecD)
        #saca la parte entera en string
        parteEntera = str(int(numDecD))
        print("parte entera", parteEntera)
        #lo deja como 0.xxx
        numDecD = numDecD - int(numDecD)    #aca falla en num = 1.936 - int(1.936) -> print(num) da 0.9359999999999999 
        print("parte decimal", numDecD)
        if posicion == "0.0":
            posicion = "0.1"
        else:
            posicion = posicion[:2] + '0' + posicion[2:]    #el float daba problemas asi que lo pase con un hack a caracteres
        print("posicion", posicion)
        decimalBinario = decimalBinario + parteEntera
        print(decimalBinario)

    print("Resultado decimal en binario:", decimalBinario,"\n")

    print('El número octal ingresado "{}" es {} en binario'.format(numIngresado, str(resulBin)+"."+str(decimalBinario)))


if __name__ == "__main__":
    decimal_a_binario()
