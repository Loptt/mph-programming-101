def multiplicarString(str, num):
    vacio = ""
    for i in range(0,num):
        vacio+=str
    #return str*num
    return vacio

print(multiplicarString("Adios",10))