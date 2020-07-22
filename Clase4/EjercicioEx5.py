arreglo = []

arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))

arregloInvertido = arreglo.copy()
arregloInvertido.reverse()

print(arreglo)
print(arregloInvertido)

if arreglo == arregloInvertido:
    print("Es palíndromo")
else:
    print("No palíndromo")