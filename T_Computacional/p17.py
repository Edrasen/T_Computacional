entrada = input("Introduzca una cadena: ")

new_in= ""
if entrada[0].isupper()  and entrada[1].isupper():
    new_in = entrada.upper()
else:
    new_in = entrada.lower()

print(new_in)
