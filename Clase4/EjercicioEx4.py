arreglo = []

arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
arreglo.append(int(input()))
# 0 1 2 3 4 5 - indices
# 1 2 3 4 5 6 - elementos
#1 + 3 + 5 = 9 
#2 + 4 + 6 = 12
# respuesta = 9 - 12 = -3
sumaIndicesPares = arreglo[0] + arreglo[2] + arreglo[4]
sumaIndicesImpares = arreglo[1] + arreglo[3] + arreglo[5]

resta = sumaIndicesPares - sumaIndicesImpares

print(resta)