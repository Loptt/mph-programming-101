peso = float(input())
altura = float(input())

imc = peso / (altura * altura)

if imc <= 18.5:
    print("peso inferior al normal")
elif imc <= 24.9:
    print("peso normal")
elif imc <= 29.9:
    print("perso superior al normal")
else:
    print("obesidad")