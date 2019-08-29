numero = int(input("Introduzca un numero: "))
ancho =  int(input("Introduzca el ancho del margen: "))
align = int(input("Escoja una alineacion izquierda(1), derecha(2), centro(3): "))
margin = ' ' * ancho

if align == 1:
    print("{}{}".format(numero, margin))
elif align == 2:
    print("{}{}".format(margin, numero))
else:
    print("{}{}".format(margin[:int(ancho/2)], numero))
