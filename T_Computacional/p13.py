entrada = input("Introduzca una palabra: ")

last2 = entrada[-2:]

new_concat = last2 + last2 + last2 + last2
if(len(entrada)>2):
    print(new_concat)
else:
    print("Cadena invalida: ")
