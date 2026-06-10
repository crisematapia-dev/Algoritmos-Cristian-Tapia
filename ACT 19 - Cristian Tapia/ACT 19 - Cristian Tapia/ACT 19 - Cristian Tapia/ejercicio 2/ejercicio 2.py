# 2. En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las siguientes funciones y llamarlas desde el bloque principal: 1) Carga de los sueldos en una lista. 2) Impresión de todos los sueldos. 3) Cuántos tienen un sueldo superior a $4000. 4) Retornar el promedio de los sueldos. 5) Mostrar todos los sueldos que están por debajo del promedio.

def cargarsueldos():
    sueldos = []
    for i in range(10):
        sueldo = float(input(f"Ingrese el sueldo de la persona {i+1}: "))
        sueldos.append(sueldo)
    return sueldos

def imprimirsueldos(sueldos):
    print("Sueldos:")
    for sueldo in sueldos:
        print(sueldo)

def contarsueldossuperiores(sueldos):
    contador = 0
    for sueldo in sueldos:
        if sueldo > 4000:
            contador += 1
    return contador

def calcularpromedio(sueldos):
    total = sum(sueldos)
    promedio = total / len(sueldos)
    return promedio

def mostrarsueldospordebajodelpromedio(sueldos, promedio):
    print("Sueldos por debajo del promedio:")
    for sueldo in sueldos:
        if sueldo < promedio:
            print(sueldo)
          
sueldos = cargarsueldos()
imprimirsueldos(sueldos)
cantidad_superiores = contarsueldossuperiores(sueldos)
print(f"Cantidad de sueldos superiores a $4000: {cantidad_superiores}")
promedio = calcularpromedio(sueldos)
print(f"Promedio de los sueldos: {promedio}")
mostrarsueldospordebajodelpromedio(sueldos, promedio)
