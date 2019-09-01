entrada =  input("Introduzca una cadena: ")
n = int(input("Introduzca el numero de caracteres a transformar: "))

if n < len(entrada):
    firstn = entrada[:n]
    newstr = firstn.lower() + entrada[n:]
    print(newstr)
else:
    print("n es mayor que la longitud de la cadena")
