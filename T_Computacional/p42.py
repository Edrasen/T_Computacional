entrada = input("Introduzca una cadena: ")
car = input("Introduzca el caracter de referencia: ")


count = 0
for letra in entrada:
    count = count + 1
    if(letra == car):
        print(entrada[count:])
        
    


