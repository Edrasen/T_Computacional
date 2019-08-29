entrada = input("Introduzca una cadena: ")

palabras = entrada.split()
reverse_words = []

for palabra in palabras:
    reverse_words.append(palabra[::-1])

print(" ".join(reverse_words))
