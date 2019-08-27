entrada=input("Introduce una palabra: ")

def concat2v2(entrada):
    if(len(entrada) < 2):
        print("")
    else:
        print(entrada[:2]+entrada[-2:])

concat2v2(entrada)
