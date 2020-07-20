numero = int(input())

if numero > 0:
    #positivo
    if numero % 2 == 0:
        #par
        if numero < 100:
            #menor a 100
            print("es un numero positivo, par y menor a 100")
        elif numero > 100:
            #mayor a 100
            print("es un numero positivo, par y mayor a 100")
        else: 
            print("el numero es 100")
    else:
        #impar
        if numero < 100:
            #menor a 100
            print("es un numero positivo, impar y menor a 100")
        elif numero > 100:
            #mayor a 100
            print("es un numero positivo, impar y mayor a 100")
        else: 
            print("el numero es 100")
elif numero < 0:
    #negativo
    if numero % 2 == 0:
        #par
        print("es un numero negativo, par y menor a 100")
    else:
        #impar
        print("es un numero negativo, impar y menor a 100")
else: 
    print("el numero es 0")