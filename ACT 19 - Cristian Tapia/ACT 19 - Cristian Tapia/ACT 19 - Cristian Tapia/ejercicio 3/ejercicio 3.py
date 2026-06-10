# 3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.

def suma(n1,n2,n3=0,n4=0,n5=0):
    suma = n1 + n2 + n3 + n4 + n5
    return suma

def mostra(resultado):
    print("la suma de los valores es:")
    print(resultado)

print("ingrese datos:")
valor1 = int(input("ingrese valor del primer numero:"))
valor2 = int(input("ingrese valor del tercer numero:"))
valor3 = int(input("ingrese valor del segundo numero:"))

total = suma(valor1,valor2,valor3)

mostra(total)