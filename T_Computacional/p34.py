entrada =  input("Introduzca una cadena: ")
lentrada =list(entrada)
letras_rep = []

for letra in entrada:
    if letra not in letras_rep:
        letras_rep.append(letra)
        if letra in letras_rep and entrada.count(letra) > 1:
            print(letra +" "+str(entrada.count(letra)))

