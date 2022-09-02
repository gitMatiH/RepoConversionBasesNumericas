def octal_a_decimal(numero=None):
    if numero is None:
        numOct = input("ingrese numero octal con coma en formato 'xxx.yyy' a pasar a binario:\n")
    else:
        numOct = numero
    numIngresado = numOct
    numOct = str(numOct)

    print()

    #divide entre parte entera y parte decimal
    print("Cuentas:")
    splitteado = numOct.split('.',)
    numOctE = int(splitteado[0])
    print("Parte entera", numOctE)
    numOctD = int(splitteado[1])
    print("Parte decimal", numOctD)
    print()

    #procesa parte entera
    #pasaje a decimal; Cuando lo hago en papel pienso en caracteres, no digitos
    print("Número en base ocho", numOctE)
    print()
    print("Cuentas:")
    print("----------------")
    totalEnt = 0
    #exponente = len(str(numOct))
    exponente = 0
    i=1

    while numOctE != 0:
        print("paso", i)
        resto = numOctE % 10
        print("resto de", numOctE, "% 10 =", resto)
        totalEnt = totalEnt + resto * (8**(exponente))
        print("{}*(8**({}))".format(resto, exponente), "=", totalEnt)
        print("total acumulado:", totalEnt)
        exponente = exponente + 1
        print("{}//10".format(numOctE), "=", numOctE//10)
        numOctE = numOctE // 10
        print("----------------")
        i=i+1

    print("\nParte entera en base diez:", totalEnt)


    #procesa parte decimal
    print("procesa parte decimal")

    #pasaje a decimal de la parte de la coma octal
    print(numOctD, "a binario")
    print()
    print("Cuentas:")
    print("----------------")
    totalDec = 0
    exponente = -1 # len(str(numOctD))
    numOctD = int(str(numOctD)[::-1])

    i=1

    while numOctD != 0:
        print("paso", i)
        resto = numOctD % 10
        print("resto de", numOctD, "% 10 =", resto)
        totalDec = totalDec + resto * (8**(exponente))
        print("{}*(8**({}))".format(resto, exponente), "=", totalDec)
        print("total acumulado:", totalDec)
        exponente = exponente -1
        print("{}//10".format(numOctD), "=", numOctD//10)
        numOctD = numOctD // 10
        print("----------------")
        i=i+1

    print("\nParte decimal en base diez:", totalDec)

    total = totalEnt+totalDec
    print("{} es {} en decimal".format(numIngresado, total))

    return total

if __name__ == "__main__":
    octal_a_decimal()
