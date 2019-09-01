entrada = input("Introduzca una cadena: ")

newstr = list(entrada)
count = 0
for car in entrada:
    if car == ',':
        newstr[count] = '.'
    elif car == '.':
        newstr[count] = ','
    else:
        newstr[count] = car
    count += 1

print("".join(newstr))
