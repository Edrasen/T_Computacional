entrada = input("Introduzca una cadena: ")

alfabeto = "abcdefghijklmnopqrstuvwxyz"
let_count = []

for letra in entrada:
    if letra not in let_count:
        let_count.append(letra)

let_count.sort()
conteo = ("".join(let_count))
#print(conteo)
if conteo  == alfabeto:
    print("la cadena contiene todas las letras del alfabeto")
else:
    print("la cadena NO contiene todos los caracteres")
