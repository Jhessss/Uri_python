hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

ht = hf - hi
mt = mf - mi

if(ht<0):
    ht = 24+ht
    if(mt<0):
        mt = 60+mt
        ht = ht - 1
        print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(ht,mt))
    elif(mt>=0):
        print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(ht,mt))


elif(ht==0 and mt==0):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif(ht>0):
        if(ht==1 and mt<0):
            mt = 60+mt
            print("O JOGO DUROU 0 HORA(S) E %i MINUTO(S)" %(mt))
        elif(ht!=1 and mt>=0):
            print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(ht,mt))
        elif(ht!=1 and mt<0):
            ht = ht - 1
            mt = 60+mt
            print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(ht,mt))
        else:
            print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(ht,mt))
