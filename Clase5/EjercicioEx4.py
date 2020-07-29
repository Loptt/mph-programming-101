n = int(input("dame n: "))

lista = []

for i in range(n):
    lista.append(int(input("dame un numero ")))

auxList = []

for element in lista:
    if element % 2 == 0: 
        auxList.append(element)

lista = auxList.copy()

print(lista)