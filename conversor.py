## conversor prototipo por línea de comandos
print("Codificaciones de bases momentáneamente aceptadas:\n"
      "bin: binario\n"
      "oct: octal\n")
tnum = input("ingrese base del número: ")
num = input("ingrese número: ")
base = input("ingrese a qué base convertir éste número: ")
if tnum == "oct" and base == "bin":
    from octal_a_otro.octal_a_decimal import octal_a_decimal
    from decimal_a_otro.decimal_a_binario import decimal_a_binario
    res=octal_a_decimal(num)
    print(type(res))
    resStr = decimal_a_binario(res)
    print('\nNúmero octal "{}" pasado a binario: {}'.format(num, resStr))
## conversor con gui QT, adaptación de linea de comandos
