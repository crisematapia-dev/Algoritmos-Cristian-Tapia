# 4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran sus nombres y puntajes promedio obtenidos (de 1 a 10). Cargar sus datos en vectores paralelos, mostrar docente con calificación más alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la calificación y mostrar en pantalla la cantidad de docentes que aprobaron y desaprobaron (tomando como base que se aprueba con una nota mayor o igual a 6)

nombres = []
puntajes = []

for i in range (6):
    nombre = input("Ingrese el nombre del docente: ")
    puntaje = float(input("Ingrese el puntaje (del 1 al 10): "))
    
    nombres.append(nombre)
    puntajes.append(puntaje)

for i in range (6):
    for j in range(0, 5 - i):
        if puntajes[j] < puntajes[j + 1]:
            aux = puntajes[j]
            puntajes[j] = puntajes[j + 1]
            puntajes[j + 1] = aux
            aux = nombres[j]
            nombres[j] = nombres[j + 1]
            nombres[j + 1] = aux
print("El docente con la calificación más alta es:", nombres[0], "con", puntajes[0])
print("El docente con la calificación más baja es:", nombres[5], "con", puntajes[5])
aprobados = 0
desaprobados = 0

for i in range(6):
    if puntajes[i] > 5:
        aprobados += 1
    else:
        desaprobados += 1

print("Cantidad de docentes aprobados:", aprobados)
print("Cantidad de docentes desaprobados:", desaprobados)