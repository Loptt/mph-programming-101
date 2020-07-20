lado = float(input())
diagonal = float(input())
eps = 0.00001


print( (2 * lado * lado)  ** 0.5)
if diagonal - ( 2 * lado * lado ) ** ( 0.5 ) <= eps:
    print("es cuadrado")
else:
    print("es rectangulo")