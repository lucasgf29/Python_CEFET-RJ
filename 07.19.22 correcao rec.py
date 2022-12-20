# n=int(input('entre com um valor: '))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j, end=' ')
#     print()

# OS DOIS SAO IGUAIS, SÓ QUE USA FOR E OUTRO WHILE

# n=int(input('entre com um valor: '))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(i*j, end=' ')
#         j+=1
#     i+=1
#     print()

n1=int(input('ente com um valor: '))
n2=int(input('ente com um valor: '))
cont1=0
cont2=0

for i in range(1,n1+1):
    if n1%i==0:
        cont1+=1
        
for i in range(1,n2+1):
    if n2%i==0:
        cont2+=1

if cont1==2 and cont2==2:
    if n1-n2==2 or n2-n1==2:
        print('sao numeros gemeos')
    else:
        print('nao sao gemeos')
else:
    print('nao sao gemeos')