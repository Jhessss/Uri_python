N = int(input())

horas = N//3600
seg_rest = N % 3600
minutos = seg_rest // 60
seg_rest = seg_rest % 60

output = str(horas) + ":" + str(minutos) + ":" + str(seg_rest)
print(output)
