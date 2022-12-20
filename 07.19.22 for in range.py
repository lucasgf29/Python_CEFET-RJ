# 1 até 100
# for i in range(1,101):
#     print(i, end=" ")

# 100 até 1
# for i in range(100,0,-1):
#     print(i, end=" ")

# 1 até 100, pares
# for i in range(2,101,2):
#     print(i, end=" ")

#tabuada de 1 a 10 de um numero inteiro lido
# n=int(input('entre com um valor: '))
# for i in range(1,11):
#     print(f'{n}x{i} =',n*i)
#     print()

# multiplos de 5 no intervalo de 1 a 500
# for i in range (5,501,5):
#     print(i, end = " ")

# quadrado dos numeros de 1 a 20
# for i in range(1,21):
#     print(i*i, end=' ')

#numeros pares de 1 a 600
# for i in range(2,601,2):
#     print(i, end = " ")

#leia 10 numeros e imprima a raiz quadrada de cada numero
# for i in range(1,11):
#     n = int(input('Digite um número:'))
#     print(n**0.5)

#leia 100 numeros diga qual o menor
# for i in range(1,101):
#     n=int(input('entre com um valor: '))
#     if i==1:
#         menor=n
#     if n<menor:
#         menor=n
# print('o menor número é',menor)

#leia 100 numeros inteiro se diga quantos sao impares
# cont = 0
# for i in range(1,101):
#     n = int(input('digite um número:'))
#     if n % 2 != 0:
#         cont += 1
# print(cont)

#leia 100 numeros e diga quantos estao acima de 1000, abaixo de 1000 e igual a 1000
# menor = 0
# acima = 0
# igual = 0
# for i in range(1,101):
#     n = int(input('digite um número:'))
#     if n < 1000:
#         menor += 1
#     elif n > 1000:
#         acima += 1
#     else:
#         igual += 1
# print(f"{menor} menores do que 1000, {acima} maiores que 1000, {igual} iguais a 1000")

#leia inteiro e calcule fatorial
# n = int(input('digite um número:'))
# fat=1
# for i in range(1,n+1):
#     fat *= i
# print('fatorial de', n,'=', fat)

#leia inteiro e calcle e mostre os n primeiros termos de fibonacci
# n=int(input('entre com um valor: '))
# a=0
# b=1
# for i in range(1,n+1):
#     c=a+b
#     print(b, end=' ')
#     a=b
#     b=c

#leia um numero e diga se é primo
# n=int(input('entre com um valor: '))
# cont = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         cont += 1

# if cont == 2:
#     print(n,'é um numero primo')
# else:
#     print(n,'não é um numero primo')

#leia um numero e diga se é perfeito
# n = int(input('digite um número:'))
# soma = 0
# for i in range(1,n):
#     if n % i == 0:
#         soma += i
# if soma == n:
#     print('número perfeito')
# else:
#     print('número não perfeito')

#escadinha
# n=int(input('entre com um valor:'))
# for i in range(1,n+1):
#     for j in range(1,+1):
#         print('*', end=' ')
#     print()



# quadrado NAAAAAAAAAAAO
# n=int(input('entre com um valor: '))
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if j==i:
#             print(':)', end=' ')
#         else:
#             print('*', end=' ')

#     print()

#reescreva utilizando while

# j=1
# while j<11:
#     l=1
#     while l<=j:
#         S

# cont=0
# for j in range (1,11):
#     for l in range(1,j+1):
#         cont+=1
#     print(cont)