entrada = input("Introduzca una cadena de longitud par: ")


if(len(entrada)%2 == 0):
    lon2 = int((len(entrada))/2)
    fsthlf = entrada[:lon2]
    print(fsthlf)
else:
    print("Cadena no valida")
