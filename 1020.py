dias = int(input())

anos = dias//365
diasrest = dias%365
meses = diasrest//30
diasrest = diasrest%30
d = diasrest//1
diasrest = diasrest%1

print("%i ano(s)" %(anos))
print("%i mes(es)" %(meses))
print("%i dia(s)" %(d))

