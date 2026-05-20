#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

num1=int(input("ingrese un valor entero"))

if num1>0:
    print("su numero es positivo")
else:
    if num1<0:
        print("su numero es negativo")
    else:
        if num1==0:
            print("su numero es nulo")
