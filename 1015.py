line1 = input().split()
x1 = float(line1[0])
y1 = float(line1[1])

line2 = input().split()
x2 = float(line2[0])
y2 = float(line2[1])

d = ((x2-x1)**2+(y2-y1)**2)**(1/2)

print(format(d, '.4f'))
