rgb = input("Introduzca el color en rgb, separando con una coma cada numero: ")

rgb_splt = list(rgb.split(','))

r = int(rgb_splt[0])
g = int(rgb_splt[1])
b = int(rgb_splt[2])

def rgb2hex(r,g,b):
    print("#%02x%02x%02x" % (r,g,b))

rgb2hex(r, g, b)
