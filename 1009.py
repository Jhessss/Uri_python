nome = input()
salario = float(input())
vendasmes = float(input())

bonus = vendasmes*0.15

total = salario+bonus

print("TOTAL = R$", format(total, '.2f'))

