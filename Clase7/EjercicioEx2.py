import math as m

def chicharronera(a,b,c):
    print((-b + m.sqrt(b*b-4*a*c))/(2*a))
    print((-b - m.sqrt(b*b-4*a*c))/(2*a))

chicharronera(1,2,0)