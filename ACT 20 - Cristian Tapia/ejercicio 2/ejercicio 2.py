# 2. Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios. Definir las siguientes funciones: 1) Cargar los nombres de artículos y sus precios. 2) Imprimir los nombres y precios. 3) Imprimir el nombre de artículo con un precio mayor 4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.

def precio_mayor (precio, productos):
    may=precio[0]
    for x in range(1, len (precio)):
        if precio [x]>may:
            may=precio[x]
            pos=x
    print ("producto con mayor precio: ", productos[pos], "con valor de", may)

def importe(precio,productos):
    porte=int(input("ingrese el importe que tienes "))
    for x in range (len(precio)):
        if precio[x]<=porte:
            pos= x
            print(f"productos con menor o igual precio: {productos[pos]}")

productos= []
precio = []

for x in range (5):
    ha=input("ingrese el nombre del producto :")
    productos.append(ha)
    sb=int(input(f"ingrese el valor del producto {ha}"))
    precio.append(sb)
for f in range (5):
    print(f"el nombre del producto es {productos[f]} y su valor es: {precio[f]}")

precio_mayor(precio,productos)
importe(precio, productos)
