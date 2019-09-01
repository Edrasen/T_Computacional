ent =  input("Introduzca un a cadena: ")

count = 0
for letra in ent:
    if letra in "aeiou":
        count += 1
    else: 
        count = count

print(count)
        
