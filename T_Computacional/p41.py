ent = input("Introduzca una cadena: ")

car = input("Introduzca el caracter delimitador: ")

count = 0
index = 0
for letra in ent:
    if letra == car:
        index = count
        count += 1
    else:
        count += 1

print(ent[:index] + " " +ent[index:])
