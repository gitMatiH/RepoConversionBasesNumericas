def octal_entero_a_decimal(numero=None):
    if numero is None:
        numOct = input("ingrese numero octal con coma en formato 'xxx.yyy' a pasar a binario:\n")
    else:
        numOct = numero
    numIngresado = numOct
    numOct = str(numOct)

    #divide entre parte entera y parte decimal
    splitteado = numOct.split('.',)
    numOctE = int(splitteado[0])
    numOctD = int(splitteado[1])

    #procesa parte entera
    totalEnt = 0
    exponente = 0
    i=1

    while numOctE != 0:
        resto = numOctE % 10
        totalEnt = totalEnt + resto * (8**(exponente))
        exponente = exponente + 1
        numOctE = numOctE // 10

    #procesa parte decimal
    #pasaje a decimal de la parte de la coma octal
    totalDec = 0
    exponente = -1
    numOctD = int(str(numOctD)[::-1])

    i=1

    while numOctD != 0:
        resto = numOctD % 10
        totalDec = totalDec + resto * (8**(exponente))
        exponente = exponente -1
        numOctD = numOctD // 10

    total = totalEnt+totalDec
 
    return numIngresado, total

if __name__ == "__main__":
    
    (numIngresado, total) = octal_entero_a_decimal()
    print("{} es {} en decimal".format(numIngresado, total))
