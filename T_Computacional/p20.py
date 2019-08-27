key_long = 26

def getkey():
    key = 0
    print("Ingresa la llave, debe ser menor o  igual que 26")
    key = int(input())
    if (key > 1 and key <= key_long):
        return key

def getMsg():
    entrada = input("Introduzca el mensaje a encriptar: ")
    return entrada

def traduct(mensaje, llave):
    traduction = ""
    for caracter in mensaje:
        if caracter.isalpha():
            num = ord(caracter)
            num += llave
            if caracter.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif caracter.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            
            traduction += chr(num)
        else:
            traduction += caracter
    return traduction

llave = getkey()
mensaje = getMsg()

print("El mensaje encriptado es: ")
print(traduct(mensaje, llave))
