# 3. Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados: def retornar_superficie(lado1,lado2): En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cuál de los dos tiene una superficie mayor.

def retornarsuperficie(lado1, lado2):
    return lado1 * lado2

def cargardatos():
    lado1_rectangulo1 = float(input("Ingrese el lado 1 del primer rectángulo: "))
    lado2_rectangulo1 = float(input("Ingrese el lado 2 del primer rectángulo: "))
    superficie1 = retornarsuperficie(lado1_rectangulo1, lado2_rectangulo1)

    lado1_rectangulo2 = float(input("Ingrese el lado 1 del segundo rectángulo: "))
    lado2_rectangulo2 = float(input("Ingrese el lado 2 del segundo rectángulo: "))
    superficie2 = retornarsuperficie(lado1_rectangulo2, lado2_rectangulo2)
    return superficie1, superficie2

def resultados():
    superficie1, superficie2 = cargardatos()
    if superficie1 > superficie2:
        print("El primer rectángulo tiene una superficie mayor.")
    elif superficie2 > superficie1:
        print("El segundo rectángulo tiene una superficie mayor.")
    else:
        print("Ambos rectángulos tienen la misma superficie.")

resultados()
