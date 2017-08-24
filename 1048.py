salario = float(input())

if(salario>=0) and (salario<=400.00):
    novosalario = salario*0.15+salario
    reajuste = salario*0.15
    perc = 15

elif(salario>=400.01) and (salario<=800.00):
    novosalario = salario*0.12+salario
    reajuste = salario*0.12
    perc = 12

elif(salario>=800.01) and (salario<=1200.00):
    novosalario = salario*0.10+salario
    reajuste = salario*0.10
    perc = 10

elif(salario>=1200.01) and (salario<=2000.00):
    novosalario = salario*0.07+salario
    reajuste = salario*0.07
    perc = 7

else:
    novosalario = salario*0.04+salario
    reajuste = salario*0.04
    perc = 4

print("Novo salario: %.2f" %(novosalario))
print("Reajuste ganho: %.2f" %(reajuste))
print("Em percentual: %i %%" %(perc))
