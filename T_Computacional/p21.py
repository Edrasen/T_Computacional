entrada = input("Introduzca una cadena con multiples palabras: ")
concat = input("Introduzca la cadena a concatenar en cada palabra: ")

entrada_spl = list(entrada.split())
count = 0
for palabra in entrada_spl:
    entrada_spl[count] = concat + palabra
    count = count + 1

print(entrada_spl)
