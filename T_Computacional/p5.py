en1=input("Escriba la primera palabra: ")
en2=input("Escriba la segunda palabra: ")

def intercat(entrada1, entrada2):
        newstr1 = entrada1[:2]
        newstr2 = entrada2[:2]
        mensaje1= newstr2 + entrada1[2:] + ' ' + newstr1 + entrada2[2:]
        print(mensaje1)

intercat(en1,en2)
