lado = float(input())
diagonal = float(input())
epsilon = 0.001

resta = diagonal - ( 2 * lado * lado ) ** ( 0.5 )

if resta <= eps and resta >= -eps:
    print("es cuadrado")
else:
    print("no es un cuadrado")