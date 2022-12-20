#  Q1 - faca um programa que leia um numero e diga se é quase perfeito (quando a soma dos seus divisores [MENOS ELE] é igual a ele -1)

# n=int(input('entre com um numero positivo inteiro : '))
# while n<=0:
#     print('erro!')
#     n=int(input('entre com um numero positivo inteiro: '))

# soma=0
# i=1


# while i<n:
#     if n%i==0:
#         soma+=i            
#     i+=1
# if soma==(n-1):
#     print(f'{n} é um numero quase perfeito')
# else:
#     print(f'{n} não é um numero quase perfeito')




#  Q2 - faca um programa que leia um numero inteiro qualquer e em seguida calcule a quantidade de digitos desse numero, digue se é par ou impar e calcule o fatorial 

# n=int(input('entre com um valor inteiro positivo: '))
# while n<=0:
#     print('erro!')
#     n=int(input('entre com um valor inteiro positivo: '))

# soma=0
# i=1
# fat=1
# aux=n

# while n!=0:
#     n//=10
#     soma+=1


# while i<=soma:
#     fat*=i
#     i+=1

# if soma%2==0:
#     print(f' {soma} é par e seu fatorial={fat} ')
# else:
#     print(f' {soma} é impar e seu fatorial={fat} ')


#   Q3 - faca um programa que leia um numero inteiro positivo igual ao do trabalho em escadinha em fibonnaci

# n=int(input('entre com um numero: '))
# while n<=0:
#     print('erro!')
#     n=int(input('entre com um numero: '))

# i=1

# while(i<=n):
#     j=1
#     a=0
#     b=1 
#     while(j<=i):
#         c=a+b
#         a=b
#         b=c
#         print(a, end=' ')
#         j+=1         
#     i+=1
#     print()


# n=int(input('entre com um numero inteiro positivo: '))
# while n<=0:
#     print('erro!')
#     n=int(input('entre com um numero inteiro positivo: '))
    
# if n%2==0:
#     aux='par'
# else:
#     aux='impar'
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if j==i:
#             print('*', end=' ')
#         else:
#             print(aux, end=' ')
#         j+=1
#     i+=1
#     print()
        
        
n=int(input('entre com um numero: '))
while n<=0:
    print('erro!')
    n=int(input('entre com um numero: '))

i=1

while(i<=n):
    j=1
    while(n>=j):
        if n==j:
        a=b
        b=c
        print(a, end=' ')
        j+=1         
    i+=1
    print()