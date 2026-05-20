# 4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer: a. La cantidad de valores ingresados negativos. b. La cantidad de valores ingresados positivos. c. La cantidad de múltiplos de 15. d. El valor acumulado de los números ingresados que son pares.
positivos=0
negativos=0
multiplos15=0
sumaPares=0

for i in range(11):
    n=int(input("Ingrese un valor entero"))
    if n < 0:
        negativos += 1
    elif n > 0:
        positivos += 1
    if n % 15 == 0:
        multiplos15 += 1
    if n % 2 == 0:
        sumaPares += n
print(f"Cantidad de valores positivos: {positivos}")
print(f"Cantidad de valores negativos: {negativos}")
print(f"Cantidad de múltiplos de 15: {multiplos15}")
print(f"Valor acumulado de los números ingresados que son pares: {sumaPares}")