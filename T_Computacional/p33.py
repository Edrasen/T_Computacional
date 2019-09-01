entrada =  input("Introduzca la cadena a modificar: ")

lentrada = list(entrada)
alfabeto = "aeiou"
counter = 0
for letra in entrada:
    if letra in alfabeto:
        lentrada[counter]=''
        counter+=1
    else:
        counter+=1

print("".join(lentrada))
    
