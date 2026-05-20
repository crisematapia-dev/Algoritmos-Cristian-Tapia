# 1. Se desea desarrollar un programa que permita registrar los nombres y las calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el nombre del estudiante con la nota más alta, junto con su nota. Al igual que el estudiante con la nota más baja. Informar si hay estudiantes con la misma nota máxima o mínima.

nombres = []
notas = []

for i in range(6):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    
    nombres.append(nombre)
    notas.append(nota)
for k in range (5):
    for i in range (6-1):
        if notas[i] > notas[i+1]:
            aux = notas[i]
            notas[i] = notas[i+1]
            notas[i+1] = aux
print("El estudiante con la nota más alta es:", nombres[5], "con una nota de", notas[5])
print("El estudiante con la nota más baja es:", nombres[0], "con una nota de", notas[0])
if notas[5] == notas[4]:
    print("Hay estudiantes con la misma nota máxima.")
if notas[0] == notas[1]:
    print("Hay estudiantes con la misma nota mínima.")