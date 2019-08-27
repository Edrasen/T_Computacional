entrada = input("Escriba una cadena: ")

def borrar(entrada):
    count = 1
    new_str = list(entrada)

    for letra in entrada:
        if (count%2 == 0):
            count = count + 1
        else:
            (new_str).remove(letra)
            count = count+1  
    
    print("".join(new_str))

borrar(entrada)
