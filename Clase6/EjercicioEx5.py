def esPalindromo(palabra):
    volteado = ''.join(reversed(palabra))
    return palabra == volteado

print(esPalindromo("1234"))