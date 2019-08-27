entrada = input("Introduzca una cadena: ")

if(len(entrada)%9 == 0):
    reverse = entrada[::-1]
    print(reverse)
else:
    print("Cadena no valida")
