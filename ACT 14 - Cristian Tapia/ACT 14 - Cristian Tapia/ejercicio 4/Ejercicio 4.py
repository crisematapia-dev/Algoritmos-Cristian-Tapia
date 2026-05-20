# 4. Cargar por teclado y almacenar en una lista las alturas de 5 personas(valores float) Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

personas = []
suma = 0

for i in range (5):
    alturas= float(input("Ingrese la altura de la persona"))
    personas.append(alturas)
for i in range(5):
    suma=suma + personas[i]
promedio = suma/5

altos=0
bajos=0

for alturas in personas:
    if alturas > promedio:
        altos += 1
    elif alturas < promedio: 
        bajos +=1

print (f"Promedio de alturas: {promedio}" )
print (f"personas mas altas que el promedio: {altos}")
print (f"personas mas bajas que el promedio: {bajos}")