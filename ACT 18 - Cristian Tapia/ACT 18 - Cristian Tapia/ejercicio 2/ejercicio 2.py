# 2. Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ordenarenteros(a, b, c):
    enteros = [a, b, c]
    enteros.sort()
    print("Los números ordenados de menor a mayor son:", enteros)

def solicitaryordenar():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    num3 = int(input("Enter third integer: "))
    ordenarenteros(num1, num2, num3)

solicitaryordenar()