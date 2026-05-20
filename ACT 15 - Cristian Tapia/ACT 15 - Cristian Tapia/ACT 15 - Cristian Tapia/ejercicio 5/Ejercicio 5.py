# 5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

paises = []
habitantes = []
for i in range(5):
    pais = input("Ingrese el nombre de un país: ")
    poblacion = int(input("Ingrese la cantidad de habitantes del país: "))
    paises.append(pais)
    habitantes.append(poblacion)
for k in range (4):
    for i in range (5-1):
        if paises[i] > paises[i+1]:
            aux = paises[i]
            paises[i] = paises[i+1]
            paises[i+1] = aux
            aux2 = habitantes[i]
            habitantes[i] = habitantes[i+1]
            habitantes[i+1] = aux2
print("Lista de países ordenada alfabéticamente:")
for i in range(5):
    print(paises[i])
for k in range (4):
    for i in range (5-1):
        if habitantes[i] < habitantes[i+1]:
            aux = habitantes[i]
            habitantes[i] = habitantes[i+1]
            habitantes[i+1] = aux
            aux2 = paises[i]
            paises[i] = paises[i+1]
            paises[i+1] = aux2
print("Lista de países ordenada por cantidad de habitantes (de mayor a menor):")
for i in range(5):
    print(paises[i], habitantes[i])