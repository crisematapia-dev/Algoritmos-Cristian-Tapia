# 2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

empleadosMañana= []
empleadosTarde= []

for i in range (4):
    sueldo = float(input("Ingrese Sueldo turno mañana:"))
    empleadosMañana.append(sueldo)

for i in range (4):
    sueldo = float(input("Ingrese sueldo turno tarde"))
    empleadosTarde.append(sueldo)

print ("sueldos turno mañana:")
print (empleadosMañana)

print ("sueldos turno tarde")
print (empleadosTarde)