line1 = input().split()
cod1 = int(line1[0])
nump1 = int(line1[1])
valor1 = float(line1[2])

tot1 = nump1*valor1

line2 = input().split()
cod2 = int(line2[0])
nump2 = int(line2[1])
valor2 = float(line2[2])

tot2 = nump2*valor2

total = tot1+tot2

print("VALOR A PAGAR: R$", format(total, '.2f'))

