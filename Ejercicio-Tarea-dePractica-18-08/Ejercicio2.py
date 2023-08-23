palabra = (input("Ingresa una frase: ") )
palabra = palabra.lower()
vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    print (vocal, palabra.count(vocal))