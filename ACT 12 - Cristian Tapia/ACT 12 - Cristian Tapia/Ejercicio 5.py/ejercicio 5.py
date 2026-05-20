# 5. Realizar un programa que lea los lados de n triángulos, e informar: a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual) b. Cantidad de triángulos de cada tipo.

n = int(input("¿Cuántos triángulos deseas ingresar? "))
equilateros = 0
isosceles = 0
escalenos = 0
for i in range(n):
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))
    
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
        equilateros += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
        isosceles += 1
    else:
        print("El triángulo es escaleno.")
        escalenos += 1
print(f"Cantidad de triángulos equiláteros: {equilateros}")
print(f"Cantidad de triángulos isósceles: {isosceles}")
print(f"Cantidad de triángulos escalenos: {escalenos}")