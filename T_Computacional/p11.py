entrada =input("Introduzaca una cadena: ")
print("Desea solo mayusculas(1) o minusculas(2)?: ")
selec = int(input())

if(selec == 1):
    print(entrada.upper())
elif(selec == 2):
    print(entrada.lower())
else:
    print("Opcion no valida")
