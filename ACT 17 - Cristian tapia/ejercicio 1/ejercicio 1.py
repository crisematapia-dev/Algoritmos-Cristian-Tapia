# 1. Se tiene la siguiente lista: lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]] Imprimir la lista. Luego cambiar de elemento todos los enteros mayores a 50 del primer elemento de &quot;lista&quot;. El resto de enteros menores a 50 deben encontrarse en una nueva posición dentro de la lista. Volver a imprimir la lista.

lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print("Lista original:")
print(lista)

for i in range(len(lista[0])):
    if lista[0][i] > 50:
        lista[0][i] = "Mayor a 50"

nueva_posicion = []
for i in range(len(lista[0])):
    if lista[0][i] != "Mayor a 50":
        nueva_posicion.append(lista[0][i])
        lista[0][i] = "Menor a 50"
lista.append(nueva_posicion)

print("Lista modificada:")
print(lista)
