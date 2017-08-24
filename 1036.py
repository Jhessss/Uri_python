import math

a, b, c= input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (b**2)-(4*a*c)

if(a!=0) and (delta>=0):
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print("R1 =", format(x1, '.5f'))
    print("R2 =", format(x2, '.5f'))

elif(delta<0):
    print("Impossivel calcular")

else:
    print("Impossivel calcular")

