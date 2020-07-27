def aBinario(num):
    lista = []
    while num != 0:
        nuevoBit = num % 2
        lista.append(nuevoBit)
        num = int(num / 2)
    lista.reverse()
    return lista

print(aBinario(45))
