#3 3. Confeccionar un programa que permita: 1) Cargar una lista de 10 elementos enteros. 2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos. 3) Imprimir las dos listas generadas.

def cargarElementos():
    lista=[]
    for x in range(10):
        q=int(input("ingresa numeros positivos o negativos"))
        lista.append(q)
    return lista

def separar(lista):
    ng=[]
    ps=[]
    for x in range(len(lista)):
        if lista[x]>=0:
            ps.append(lista[x]) 
        else:
            ng.append(lista[x])
    return [ng,ps]

def mostrar(ng, ps):
    print ("numeros negativos: ")
    print (ng)
    print ("numeros positivos")
    print (ps)
    
cargarLista=cargarElementos()
Lista1,Lista2=separar(cargarLista)
mostrar(Lista1,Lista2)