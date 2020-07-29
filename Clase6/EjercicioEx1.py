def div243(num):
    booleano = (num % 243 == 0)
    if booleano:
        return True
    else: 
        return False
    #return num % 243 == 0

print( div243(243 * 3) )