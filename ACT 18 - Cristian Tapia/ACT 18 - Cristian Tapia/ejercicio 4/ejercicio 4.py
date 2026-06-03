# 4. Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras a o A

def cagardatos():
    texto = input("Ingrese un texto en mayúsculas o minúsculas: ")
    return texto

def contarletras(cadena):
    contador = 0
    for letra in cadena:
        if letra == 'a' or letra == 'A':
            contador += 1
    return contador

def resultados():
    texto = cagardatos()
    cantidada = contarletras(texto)
    print(f"La cantidad de letras 'a' o 'A' en el texto es: {cantidada}")

resultados()