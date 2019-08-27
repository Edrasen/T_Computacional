numero = int(input("Cuantas palabras va a introducir? "))

if numero < 1:
    print("Imposible!")

else:
    lista = []
    morelepal = ""
    index = 0
    lenpal = 0
    for i in range(numero):
        print("Escriba la palabra ", str(i+1) + ": ", end="")
        palabra = input()
        lista += [palabra]
        if(len(palabra) >= lenpal):
            lenpal = len(palabra)
            morelepal = palabra
            indx = i
        else:
            morelpal = morelepal
            indx = indx
    #print("La lista es: ", lista)
    print("La palabra mas larga es: ", lista[indx])
