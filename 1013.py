line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])

MaiorAB = (a+b+abs(a-b))/2
Maiortodos=(MaiorAB+c+abs(MaiorAB-c))/2

print("%i eh o maior" %(Maiortodos))
