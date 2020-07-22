lado = float(input())
diagonal = float(input())
eps = 0.0001

resta = diagonal - ( 2 * lado * lado ) ** ( 0.5 )

if resta <= eps and resta >= -eps:
    print("es cuadrado")
else:
    print("es rectangulo")