lado = float(input())
diagonal = float(input())
eps = 0.0001

#print( (2 * lado * lado)  ** 0.5)
resta = diagonal - ( 2 * lado * lado ) ** ( 0.5 )
#print(resta)
if resta <= eps and resta >= -eps:
    print("es cuadrado")
else:
    print("es rectangulo")