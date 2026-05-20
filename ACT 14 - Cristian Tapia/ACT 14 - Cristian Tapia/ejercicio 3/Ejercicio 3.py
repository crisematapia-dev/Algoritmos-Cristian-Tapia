# 3. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

numeros =[]

for i in range (5):
    valores = int(input("Ingrese un valor"))
    numeros.append(valores)
mayor = numeros[0]
for x in numeros:
    if x > mayor:
        mayor = x
print("El mayor valor es: ")    
print(mayor)

contador = 0
for n in numeros :
    if n == mayor:
        contador += 1

if contador > 1:
    print("El valor se repite en la lista")
    print("Se repite", contador, "veces")
else:
    print("El valor mayor no se repite en la lista")
