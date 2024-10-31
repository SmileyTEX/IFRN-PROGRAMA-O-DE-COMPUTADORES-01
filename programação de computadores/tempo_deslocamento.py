D=int(input())
V=int(input())
horas=D//V
minutos=((D/V)-(D//V))*60
print("{:02d}".format(horas),int(minutos),sep=":")