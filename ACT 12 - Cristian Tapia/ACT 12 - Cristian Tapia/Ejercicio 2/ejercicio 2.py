#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
n=int(input("cuantas alturas deseas ingresar?"))
for a in range (n):
    alturas=int(input("Ingrese la altura"))
    promedio=alturas/n
print("La altura promedio es:")
print (promedio)