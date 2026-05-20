# 2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas realizadas por cada uno en un mes. Cargar los nombres y ventas en dos vectores paralelos, ordenar los datos de mayor a menor según las ventas, imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue el que menos vendió de los 5 empleados.

nombres = []
ventas = []
for i in range (5):
    nombre = input("Ingrese el nombre del vendedor: ")
    venta = float(input("Ingrese el total de ventas del vendedor: "))
    
    nombres.append(nombre)
    ventas.append(venta)
for k in range (4):
    for i in range (5-1):
        if ventas[i] > ventas[i+1]:
            aux = ventas[i]
            ventas[i] = ventas[i+1]
            ventas[i+1] = aux
            aux2 = nombres[i]
            nombres[i] = nombres[i+1] 
            nombres[i+1] = aux2
print("Lista de vendedores ordenada por ventas (de mayor a menor):")
for i in range(5):
    print(nombres[i], ventas[i])
print("El vendedor que menos vendió es:", nombres[0], "con un total de ventas de", ventas[0])