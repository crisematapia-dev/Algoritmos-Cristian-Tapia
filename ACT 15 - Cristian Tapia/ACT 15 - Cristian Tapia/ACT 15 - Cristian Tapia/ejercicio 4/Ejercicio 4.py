# 4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

numeros = []

for i in range(5):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

for m in range (4):
    for n in range (4):
        if numeros[n] < numeros[n+1]:
            aux = numeros[n]
            numeros[n] = numeros[n+1]
            numeros[n+1] = aux

print("Lista de números ordenada de mayor a menor:")
print(numeros)

for f in range (4):
    for k in range (1,5):
        if numeros[k] < numeros[k+1]:
            aux = numeros[k]
            numeros[k] = numeros[k+1]
            numeros[k+1] = aux
    
print("Lista de números ordenada de menor a mayor:")
print(numeros)