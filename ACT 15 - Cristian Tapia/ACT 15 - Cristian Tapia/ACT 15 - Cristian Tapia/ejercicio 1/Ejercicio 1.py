# 1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente: a. Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas) b. Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar &quot;Muy Bueno&quot; si la nota es mayor o igual a 8, &quot;Bueno&quot; si la nota está entre 4 y 7, y colocar &quot;Insuficiente&quot; si la nota es inferior a 4. c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.
alumnos = []
notas = []

for i in range(4):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nota = int(input("Cargue la nota del alumno: "))
    alumnos.append(nombre)
    notas.append(nota)

muyBueno = 0

print("Listado de alumnos:")
for nombre, nota in zip(alumnos, notas):
    if nota >= 8:
        condicion = "Muy Bueno"
        muyBueno += 1
    elif nota >= 4:
        condicion = "Bueno"
    else:
        condicion = "Insuficiente"
    print(nombre, nota, condicion)

print("Cantidad de alumnos Muy Bueno:", muyBueno)
