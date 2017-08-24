a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

lista = [a,b,c]

lista.sort(reverse=True)

if(lista[0]>=(lista[1]+lista[2])):
    print("NAO FORMA TRIANGULO")
elif((lista[0])**2==((lista[1]**2)+(lista[2])**2)):
    print("TRIANGULO RETANGULO")
elif((lista[0])**2>((lista[1]**2)+(lista[2])**2)):
    print("TRIANGULO OBTUSANGULO")
elif((lista[0])**2<((lista[1]**2)+(lista[2])**2)):
    print("TRIANGULO ACUTANGULO")

if(lista[0]==lista[1]==lista[2]):
    print("TRIANGULO EQUILATERO")
elif(lista[0]==lista[1]) or (lista[1]==lista[2]) or (lista[0]==lista[2]):
    print("TRIANGULO ISOSCELES")
