arreglo = []

arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))


sumaIndicesPares = arreglo[0] + arreglo[2] + arreglo[4]
sumaIndicesImpares = arreglo[1] + arreglo[3] + arreglo[5]

resta = sumaIndicesPares - sumaIndicesImpares

print(resta)