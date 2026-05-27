# 3. Definir una lista y almacenar los nombres de 3 empleados. Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó. Imprimir los nombres de empleados y los días que faltó. Mostrar los empleados con la cantidad de inasistencias. Finalmente mostrar el nombre o los nombres de empleados que faltan menos días.

empleado = []
dias_faltados = []
for i in range(3):
    nombre = input(f"Ingrese el nombre del empleado N°{i+1}: ")
    empleado.append(nombre)
    dias = int(input(f"Ingrese la cantidad de días que faltó {nombre}: "))
    dias_faltados.append(dias)
print("Empleados y días faltados:")
for i in range(3):
    print(f"{empleado[i]}: {dias_faltados[i]} días")

print("Cantidad de inasistencias de cada empleado:")
for i in range(3):
    print(f"{empleado[i]}: {dias_faltados[i]} inasistencias")

menor = min(dias_faltados)
print("Empleados que faltan menos días:")
for i in range(3):
    if dias_faltados[i] == menor:
        print(f"{empleado[i]} con {menor} inasistencias")