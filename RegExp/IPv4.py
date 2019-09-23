import re

ipadress = input("Introduzca una direccion IPV4\n")

x = re.search("^(2?[0-5]?[0-9]|1?[0-9]?[0-9])\.((2?[0-5]?[0-9]|1?[0-9]?[0-9])\.)(2?[0-5]?[0-5]|1?[0-9]?[0-9])\.(2?[0-5]?[0-5]|1?[0-9]?[0-9])$", ipadress)

if(x):
    print("\nIPv4 valida!")
else:
    print("\nIPv4 no valido!")
