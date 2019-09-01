ent = input("Introduzca una cadena: ")

res = [ent[i:j] for i in range(len(ent))
        for j in range(i + 1, len(ent) + 1)]

num = len(res)

pref = []
suf = []

for a in range(len(ent)-1):
    pref.append(res[a])



pos = len(ent)-1
for car in range(len(ent)-1, 0, -1):
    pos = pos  + car
    suf.append(res[pos])


print("\nAll substrings of original string are: ")
print(str(res)+"\n")
print("El numero de subcadenas es: "+str(num)+"\n")
print("Prefijos propios: ")
print(str(pref)+"\n")
print("Sufijos propios: ")
print(suf)

