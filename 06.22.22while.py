#faca um programa que mostre a tabuada de 1 a 10 de um numero inteiro

'''n=int(input('Entre com um numero: \t'))
i=1
while i<=10:
    print(f'{i}x{n}={i*n}')
    i+=1'''
    
#faca um programa que imprima os 100 primeiro numeros pares positivos

'''n=2
while n<=200:
    print (f'{n}',end=' ')
    n+=2'''
    
#faca um programa que imprima os multiplos de 5 no intervalo de 1 até 500

'''n=5
while n<=500:
    print(f'{n}',end=' ')
    n+=5'''

#faca um programa que imprima o quadrado dos numeros de 1 até 20

'''n=1

while n<=20:
    i=n*n
    print(f'{i}',end=' ')
    n+=1'''
    
#faca um programa que imprima os numeros pares de 1 a 600

'''n=2
while n<=600:
    print (f'{n}',end=' ')
    n+=2'''
    
#faca um programa que leia 10 numeros e imprima a raiz quadrada de cada numero

'''n1,n2,n3,n4,n5,n6,n7,n8,n9,n10=input('Entre com 10 numeros separados por espaço:\t').split()

n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
n6=int(n6)
n7=int(n7)
n8=int(n8)
n9=int(n9)
n10=int(n10)'''

'''i=1
while i<=10:
    n=int(input('Entre com um número:\t'))
    print(f'Sua raiz quadrada é {n*n}',end=' ')
    i+=1'''
    
#faca um programa que leia 100 numeros inteiros e diga qual é o menor

'''i=1
while i<=100:
    n=int(input('Entre com um valor: '))
    if i==1:
        menor=n
    elif n<menor:
        menor=n
    
    i+=1
    
print(f'{menor} é o menor valor')'''

#faca um programa que leia 100 numeros inteiros e diga quantos sao impares

'''tam=100
i=1
imp=0
while i<=tam:
    n=int(input('Entre com um valor: '))
    
    if n%2!=0:
        imp+=1
        
    i+=1  
print(f'\n {imp} números impares')'''

#faca um programa que leia 100 numeros e diga quantos estao acima, iguais e abaixo de 1000

'''tam=100
i=1
ab=0
ig=0
ac=0
while i<=tam:
    n=int(input('Entre com um valor: '))
    
    if n<1000:
        ab+=1
        
    elif n==1000:
        ig+=1
        
    else: 
        ac+=1
        
    i+=1

print(f'\n {ab} números abaixo de 1000,{ig} números iguais a 1000 e {ac} números acima de 1000')'''
    
  
#faca um programa que leia um numero inteiro e calcule o seu fatorial

# n=int(input('Entre com um valor:\t'))
# temp=n
# i=n
# n-=1
# if n<0:
#     print('Erro! Nâo existe fatorial de numero negativo!')
# else:
#     while n>0:
#         i=i*n
#         n-=1
    
# print(f'O fatorial de {temp} é {i}')

#ou

# if n<0:
#     print('Erro! Nâo existe fatorial de numero negativo!')

# else:
#     i=1
#     fat=1
#     while i<=n:
#         fat*=i
#         i+=1
#     print(f'{n}!={fat}')
    
    
#faca um programa que leia um numero inteiro e calcule e mostre os n primeiros termos da serie de fibonacci

'''n=int(input('Entre com um numero: \t'))
if n<=0:
    print('Erro!')

else:
    a=0
    b=1
    i=1
    
    while i<=n:
        c=a+b
        print(b,end=' ')
        a=b
        b=c
        
        i+=1'''
        
        
#faca um programa que leia um numero e verifique se ele é primo

'''n=int(input('Entre com um numero: \t'))
i=1
cont=0

while i<=n:
    if n%i==0:
        cont+=1
        
    i+=1
    
if cont==2:
    print(f'{n} é primo')
    
else:
    print(f'{n} não é primo')'''  
        
    
#faca um programa que leia um numero e diga se é perfeito

'''n=int(input('Entre com um numero: \t'))
i=1
cont=0

while i<n:
    if n%i==0: 
        cont+=i
    i+=1

if cont==n:
    print(f'{n} é um numero perfeito!')
    
else:
    print(f'{n} não é um numero perfeito!')'''
    
 
#faca um programa que leia um numero inteiro N e mostre na tela a figura abaixo

'''n=int(input('Entre com um numero inteiro positivo: \t'))

if n<=0:
    print('Erro!')
    
else:
    i=1
    while i<=n:
        j=1
        while j<=i:
            print('*', end='')
            j+=1
        i+=1
        print()'''
        


    
#faca um programa igual ao anterior mas finalizando com 1*


# n=int(input('Entre com um numero inteiro positivo: \t'))

# if n<=0:
#     print('Erro!')
    
# else:
#     i=1
#     while i<=n:
#         j=1
#         while j<=i:
#             print('*', end=' ')
#             j+=1
#         i+=1
#         print()
        
        
#     j=1
#     i=n-1
#     while i>=1 and j>=i:
#         print('*', end=' ')
#         j-=1
#     i-=1
#     print()
    
    #TERMINAR TERMINAR TERMINAR

# n=int(input('entre com o total de pessoas:'))
# somaalt=0
# somaalth=0
# toth=0
# somaaltm=0
# totm=0
# i=1
# while i<=n:
#     sexo=int(input('entre com 1-masc ou 2-fem: '))
#     while sexo!=1 or sexo!=2:
#         print('erro! entre com 1-masc ou 2-fem: ')
#     alt=float(input('entre com a altura: '))
#     if sexo==1:
#         somaalth+=alt
#         toth+=1
#     else:
#         somaaltm+=alt
#         toth+=1
#     if i==1:
#         maior=alt
#         menor=alt
#     else:
#         if alt<menor:
#             menor=alt
#         if alt>maior:
#             maior=alt
#     i+=1
# print(f'media alt grupo={(somaalth+somaaltm)/n}')
# if toth==0`:`
#     print(f'media de alt dos homens=0')
# else:
#     malth=somaalh/toth
#     print(f'media da alt dos homens={malth}')
# if totm==0:
#     print('media de alt das mulheres=0')
# else:
#     maltm=somaaltm/totm
#     print(f'media de alt das mulheres={maltm}')


# n=int(input('entre com um numero inteiro positivo: '))
# while n<=0:
#     print('erro!')
#     n=int(input('entre com um numero inteiro positivo: '))
    
# i=1
# while i<=n:
#     j=1
#     while n>=j:
#         print('*', end=' ')
#         j+=1
#     n-=1
#     print()

