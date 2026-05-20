# 3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenamos de menor a mayor.

empleados = int(input("ingrese la cantidad de empleados que tiene la empresa: "))
sueldos=[]
for i in range(empleados):
    sueldo = int(input("ingrese el sueldo del empleado: "))
    sueldos.append(sueldo)
for k in range (4):
    for i in range (empleados-1):
        if sueldos[i] > sueldos[i+1]:
            aux = sueldos[i]
            sueldos[i] = sueldos[i+1]
            sueldos[i+1] = aux


print("Lista de sueldos ordenada de menor a mayor:")
print(sueldos)
