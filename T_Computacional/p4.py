entrada=input("Introduce una cadena ")

def rplc (entrada):
	new_str = list(entrada)
	first_l = entrada[0]
	count = 0
	for letra in entrada:
		if count != 0 and letra == first_l:
			new_str[count] = '$'
		else:
		    new_str[count] = letra
		count=count+1
	print("".join(new_str))

rplc(entrada)