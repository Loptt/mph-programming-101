lado = float(input())
diagonal = float(input())
epsilon = 0.001

#print( (2 * lado * lado)  ** 0.5)
resta = diagonal - ( 2 * lado * lado ) ** ( 0.5 )
#print(resta)
if resta <= epsilon and resta >= -epsilon:
    print("es cuadrado")
else:
    print("no es un cuadrado")