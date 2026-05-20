# 1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
mayorA7 = 0
menorA7 = 0
for i in range(10):
    nota = int(input("ingrese la nota del alumno:"))
    if nota >= 7:
        mayorA7 += 1
    else:
        menorA7 += 1
print(f"Cantidad de alumnos con notas mayores o iguales a 7: {mayorA7}")
print(f"Cantidad de alumnos con notas menores a 7: {menorA7}")