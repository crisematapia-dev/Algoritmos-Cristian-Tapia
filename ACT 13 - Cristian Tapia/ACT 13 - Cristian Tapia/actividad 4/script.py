#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

primerCuadrante = 0
segundoCuadrante = 0
tercerCuadrante = 0
cuartoCuadrante = 0

n = int(input("Ingrese la cantidad de puntos: "))

for i in range(n):
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        primerCuadrante = primerCuadrante + 1

    elif x < 0 and y > 0:
        segundoCuadrante = segundoCuadrante + 1

    elif x < 0 and y < 0:
        tercerCuadrante = tercerCuadrante + 1

    elif x > 0 and y < 0:
        cuartoCuadrante = cuartoCuadrante + 1

print("\nCantidad de puntos en el primer cuadrante:", primerCuadrante)
print("Cantidad de puntos en el segundo cuadrante:", segundoCuadrante)
print("Cantidad de puntos en el tercer cuadrante:", tercerCuadrante)
print("Cantidad de puntos en el cuarto cuadrante:", cuartoCuadrante)