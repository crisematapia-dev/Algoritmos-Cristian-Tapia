# 3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una carrera de 100 metros. El programa debe cargar los datos en dos vectores paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el promedio.
nombres = []
tiempos = []

for i in range(5):
    nombre = input("Ingrese el nombre del atleta: ")
    tiempo = float(input("Ingrese el tiempo del atleta en segundos: "))
    
    nombres.append(nombre)
    tiempos.append(tiempo)

for i in range(5):
    for j in range(0, 4 - i):
        if tiempos [j] > tiempos [j + 1]:
            aux = tiempos [j]
            tiempos [j] = tiempos [j + 1]
            tiempos [j + 1] = aux
            aux = nombres [j]
            nombres [j] = nombres [j + 1]
            nombres [j + 1] = aux


promedio = sum(tiempos) / 5
print ("El promedio es: ", promedio)
print("el mejor tiempo es de:", nombres[0], "con", tiempos[0], "segundos")
print("el peor tiempo es de:", nombres[4], "con", tiempos[4], "segundos")
print("Los atletas que superaron el promedio son:")
for i in range(5):
    if tiempos[i] < promedio:
        print(nombres[i], "con un tiempo de", tiempos[i], "segundos")