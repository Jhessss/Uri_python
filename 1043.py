a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

perimetro = a+b+c
area = ((a+b)/2)*c

if(a<(b+c)) and (b<(a+c)) and (c<(a+b)):
    print("Perimetro = %.1f" %(perimetro))

else:
    print("Area = %.1f" %(area))
