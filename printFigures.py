import math
print("Program para dibujar figuras geometricas con asteriscos (*)")
print("Se imprimira un cuadraro, un triangulo, un trapecio y un paralelogramo\n¿Cual es la dimension en la que quieres imprimir las figuras?")
number = int(input())


def printSquare(num):
    print("Cuadrado\n\n")
    for a in range(num):
        for b in range(num):
            print("*", end='')
        print()
    print("\n")

def printTriangle(num):
    print("Triangulo\n\n")
    space = 0
    noPrint = 1
    try:
        space = math.ceil(num/2)
    except:
        pass

    while True:
        for a in range(space):
            print("-", end='')
        for a in range(noPrint):
            print("*", end='')
        for b in range(space):
            print("-", end='')
        print("\n")
        #
        #
        space = space-1
        if noPrint+2 > num:
            noPrint = num
        else:
            noPrint+2
        if space < 0:
            break
    print("\n")



printSquare(number)
printTriangle(number)

# printSquare(number)


# print("Program para dibujar figuras geometricas con asteriscos (*)")
# print("Se imprimira un cuadraro, un triangulo, un trapecio y un paralelogramo")
# number = int(
#     input("Cual es la dimension en la que quieres imprimir las figuras"))


# def printSquare(num):
#     for b in range(num):
#         for a in range(num):
#             print("*" end="")
#         print("")


# printSquare(number)
