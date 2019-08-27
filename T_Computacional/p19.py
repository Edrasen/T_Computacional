entrada = input("Introduzca una cadena: ")
ref = input("Introduzca el caracter a buscar: ")

ref_lon = len(ref)

if((entrada[:ref_lon]) == ref):
    print("Cadena valida")
else:
    print("Cadena NO valida")
