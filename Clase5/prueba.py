arreglo = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
for i in range(len(arreglo)):
    menorValor = arreglo[i]
    indiceDeCambio = 0
    encontramosMenor = False
    for j in range(i+1, len(arreglo)):
        if menorValor > arreglo[j]:
            menorValor = arreglo[j]
            indiceDeCambio = j
            encontramosMenor = True
    if encontramosMenor:
        auxiliar = arreglo[i]
        arreglo[i] = menorValor
        arreglo[indiceDeCambio] = auxiliar
print(arreglo)