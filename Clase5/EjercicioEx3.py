cuantos = int(input("cuantos articulos quieres? "))
articulos = []
for i in range(cuantos):
    articulos.append(input("ingresa el nombre de un articulo "))

articulos.sort()

print(articulos)