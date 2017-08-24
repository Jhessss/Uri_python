line = input().split()
A = float(line[0])
B = float(line[1])
C = float(line[2])

pi = 3.14159
atri = A*C/2
acir = pi*C**2
atra = (A+B)*C/2
aqua = B**2
aret = A*B

print("TRIANGULO:", format(atri, '.3f'))
print("CIRCULO:", format(acir, '.3f'))
print("TRAPEZIO:", format(atra, '.3f'))
print("QUADRADO:", format(aqua, '.3f'))
print("RETANGULO:", format(aret, '.3f'))

