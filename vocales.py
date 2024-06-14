def contar_vocales(cadena):
    # Definir las vocales como un conjunto solo en minúsculas
    vocales = {'a', 'e', 'i', 'o', 'u'}
    # Convertir la cadena a minúsculas y luego utilizar una expresión generadora para contar las vocales
    return sum(1 for char in cadena.lower() if char in vocales)


# Solicitar al usuario que introduzca una palabra o frase
cadena = input("Introduce una palabra o frase: ")
numero_de_vocales = contar_vocales(cadena)
print("Número de vocales en la cadena:", numero_de_vocales)
