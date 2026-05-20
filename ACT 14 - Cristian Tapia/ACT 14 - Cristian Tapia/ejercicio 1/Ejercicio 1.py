## 1. Definir una lista que almacene por asignación los nombres de 5 personas. 33Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.


personas = []

for i in range (5):
    nombre = input("Ingrese un Nombre")
    personas.append(nombre)

contador = 0

for nombre in personas:
    if len(nombre) >= 5:
        contador += 1

print("Cantidad de nombres con 5 o más caracteres:", contador)