ancho = int(input("Introduzca el ancho de cadena deseada: "))
numero = input("Introduzca un numero: ")
num_int = int(numero)
n = ancho - len(numero)
n_ast = '*' * n
print("{}{}".format(num_int, n_ast))

