import math
print("Program para dibujar figuras geometricas con asteriscos (*)")
print("Se imprimira un cuadraro, un triangulo y un paralelogramo\n¿Cual es la dimension en la que quieres imprimir las figuras?")
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
            print(" ", end='')
        for a in range(noPrint):
            print("*", end='')
        for b in range(space):
            print(" ", end='')
        print("")
        #
        #
        space = space-1
        if noPrint+2 > num:
            noPrint = num
        else:
            noPrint = noPrint+2

        if space < 0:
            break
    print("\n")


def printParallelogram(num):
    print("Paralelogramo \n\n")
    space = num-1
    for a in range(num):
        for a in range(space):
            print(" ", end='')
        for a in range(num):
            print("*", end='')
        print("")
        space = space-1
    print("\n")

def printParallelogramInverse(num):
    print("Paralelogramo inverso \n\n")
    space = 0
    for a in range(num):
        for a in range(space):
            print(" ", end='')
        for a in range(num):
            print("*", end='')
        print("")
        space = space+1
    print("\n")


printSquare(number)
printTriangle(number)
printParallelogram(number)
printParallelogramInverse(number)