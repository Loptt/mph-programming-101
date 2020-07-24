n = int(input("dame n: "))

lista = []

for i in range(n):
    lista.append(int(input("dame un numero ")))

print(lista)

auxList = []

for i in range(n):
    if lista[i]%2 == 0:
        auxList.append(lista[i])

lista = auxList.copy()

print(lista)