entrada = input("Introduzca una cadena: ")

contador = {}

palabras = entrada.split()
for palabra in palabras:
    if palabra not in contador:
        contador[palabra] = 1
    else:
        contador[palabra] += 1


print(contador)
