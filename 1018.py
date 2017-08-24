N = int(input())

cem = N//100
dinrest = N%100
cinq = dinrest//50
dinrest = dinrest%50
vinte = dinrest//20
dinrest = dinrest%20
dez = dinrest//10
dinrest = dinrest%10
cinco = dinrest//5
dinrest = dinrest%5
dois = dinrest//2
dinrest = dinrest%2
um = dinrest//1

print(N)
print("%i nota(s) de R$ 100,00" %(cem))
print("%i nota(s) de R$ 50,00" %(cinq))
print("%i nota(s) de R$ 20,00" %(vinte))
print("%i nota(s) de R$ 10,00" %(dez))
print("%i nota(s) de R$ 5,00" %(cinco))
print("%i nota(s) de R$ 2,00" %(dois))
print("%i nota(s) de R$ 1,00" %(um))

