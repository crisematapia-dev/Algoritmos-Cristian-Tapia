# 3. Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes &quot;Lista 1 mayor&quot;, &quot;Lista 2 mayor&quot;, &quot;Listas iguales&quot;) Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo."""

suma1 = 0

for i in range(15):
    num = int(input("Ingrese un numero para la lista 1: "))
    suma1 = suma1 + num


suma2 = 0

for i in range(15):
    num = int(input("Ingrese un numero para la lista 2: "))
    suma2 = suma2 + num

if suma1 > suma2:
    print("Lista 1 mayor")

if suma2 > suma1:
    print("Lista 2 mayor")

if suma1 == suma2:
    print("Listas iguales")