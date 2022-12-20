# CORRECAO PROVA
# Q1 - 


# a=int(input('entre com o primeiro numero: '))
# b=int(input('entre com o segundo numero: '))
# if a<=0 or b<=0:
#     print('erro!')
# else:
#     soma1=0
#     soma2=0
#     i=1
#     while i<a:
#         if a%i==0:
#             soma1+=i
#         i+=1
#     i=1
#     while i<b:
#         if b%i==0:
#             soma2+=i
#         i+=1
#     if soma1==b and soma2==a:
#         print('sao numeros amigos')
#     else:
#         print('os numeros nao sao amigos')


# Q2 -

# n=int(input('entre com um valor:'))
# j=1
# a=0
# b=1
# aux=n
# if n<=0:
#     print('erro!')
# else:
#     while n//10>0:
#         n//=10
#     while j<=n:
#         c=a+b
#         a=b
#         b=c
#         j+=1
#     print(f'o {n}o termo de finacci é = {a}')


# Q3 -

n=int(input('entre com um valor inteiro positivo:'))
if n<=0:
    print('erro!')
else:
    if n%2==0:
        aux='par'
    else:
        aux='impar'
    i=1
    while i<=n:
        j=1
        while j<=n:
            if i==j:
                print('*', end=' ')
            else:
                print(aux,end=' ')
            j+=1
        print()
        i+=1