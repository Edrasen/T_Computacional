numero = int(input("Introduzca un numero entre 0 y 100: "))
porcent = '%'

if(numero >0 and numero < 100):
    print("{}{}".format(numero, porcent))
else:
    print("El numero introducido no es valido")

