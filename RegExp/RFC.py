import re

#Check if the RFC given it is valid or not

rfc = input("Introduzca su RFC\n")
x = re.search("^([A-ZÑ\x26]{4,5}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))((-)?([A-Z\d]{3}))?$", rfc)

if (x):
    print("\nRFC valido!")
else:
    print("\nRFC RFC invalido!!")                                      
