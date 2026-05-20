# 4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num1=int(input("ingrese un valor numerico de 1 o 2 digitos"))

if num1>99:
    print("Numero invalido, debe ser de 2 digitos, intente de nuevo")
else:
    if num1>10:
        print("Su numero tiene 2 digitos")
    else:
        if num1>1:
            print("su numero tiene 1 digito")
