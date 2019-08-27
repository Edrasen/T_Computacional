entrada = input("Introduzca una cadena: ")

if(len(entrada) > 3):
    newstr = entrada[:3]
else:
    newstr = entrada
print(newstr)
