# 1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal."""
n = int(input("Ingrese la cantidad de empleados: "))

entre_100_300 = 0
mas_300 = 0
total = 0

for i in range(n):
    sueldo = int(input("Ingrese el sueldo: "))

    if sueldo >= 100 and sueldo <= 300:
        entre_100_300 = entre_100_300 + 1
    else:
        mas_300 = mas_300 + 1

    total = total + sueldo

print("Empleados que cobran entre 100 y 300:", entre_100_300)
print("Empleados que cobran más de 300:", mas_300)
print("Total que gasta la empresa:", total)