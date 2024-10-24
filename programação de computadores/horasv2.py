inicio=int(input())
final =int(input())
tempo_corrido = final - inicio
h= tempo_corrido// 60
m= tempo_corrido % 60
print(h,m,sep=":")