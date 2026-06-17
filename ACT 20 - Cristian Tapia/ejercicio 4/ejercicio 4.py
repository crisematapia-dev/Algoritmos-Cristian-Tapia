# 4. Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def personas():
    edades=[]
    for x in range(5):
        ab=int(input("Ingrese edad"))
        edades.append(ab)
    return edades
def mayores (edades):
    contador=0
    c=0
    for x in range (len(edades)):
        if edades[x]>=18:
            contador+=1
        else:
            c+=1
    print ("personas mayores de 18: ", contador)
    print ("personas menores a 18 ", c)
asd=personas()
mayores(asd)