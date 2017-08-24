hi, hf = input().split()
hi = int(hi)
hf = int(hf)

ht = hf - hi

if(ht<0):
    ht = 24+ht
    print("O JOGO DUROU %i HORA(S)" %(ht))

elif(ht==0):
    print("O JOGO DUROU 24 HORA(S)")

else:
    print("O JOGO DUROU %i HORA(S)" %(ht))
