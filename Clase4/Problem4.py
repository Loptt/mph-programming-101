names = []

while True:
    name = input("Ingrese un nombre: ")
    if name == '':
        break
    names.append(name)

names.sort()
print("Lista de nombres en orden:")

for name in names:
    print(name)