entrada = input("Introduzca una cadena: ")
pos = int(input("Introduzca la posicion del caracter a eliminar: "))

new_str = list(entrada)

if len(entrada) > 0 :
    new_str.pop(pos)
    print("".join(new_str))
else:
    print("Cadena vacia")


