entrada = input("Escriba una cadena:")

new_str = list(entrada)

fc = new_str[0]
lc = entrada[-1:]

new_str[0] = lc
new_str[(len(entrada) - 1)] = fc

print("".join(new_str))
