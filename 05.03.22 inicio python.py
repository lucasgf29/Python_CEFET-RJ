#03.05.22

#faca um programa que imprima a media aritmetica dos numeros 8.1, 9.3 e 7.7

'''a=8.1
b=9.3
c=7.7
media=((a+b+c)/3)

print(f'\n a media aritmetica dos numeros{a}, {b} e {c} = {media:.1f}')''' 
      
      
#faca um programa que imprima a media entre 5 e 2

'''a=float((5+2)/2)

print(f'\n a media entre 5 e 2 = {a}')'''

#faca um pograma que leia um numero inteiro do teclado e o imprima

'''no=int(input('\n Digite um número:\t'))

print(f'o numero digitado foi = {no}')'''

#faca um programa que leia um numero inteiro e imprima o seu sucessor e o seu antecessor

'''no=int(input('\n Digite um Número:\t'))

print(f'O antecessor do seu numero é {no -1} e seu sucessor é {no +1}')'''

#faca um programa que leia seu nome e o escreva na tela

'''name=str(input('\n Digite seu nome:\t'))

print(f'Seu nome é {name}')'''


#faca um programa que leia seu nome e sua idade e escreva na tela

'''name=str(input('\n Digite seu nome:\t'))
age=int(input('\n Digite sua idade:\t'))
h=float(input('\n Digite sua altura em metros:\t'))

print(f'Seu nome é {name}, você possui {age} anos e {h} metros de altura')'''

#faca um programa que leia dois numeros inteiros e imprima a soma 

'''no1=int(input('\n digite o primeiro numero: \t'))
no2=int(input('\n digite o segundo numero: \t'))

print(f'A soma dos dois numeros digitados = {no1+no2}')'''


#2x faca um programa que leia duas notas e imprima a media aritmetica

'''no1=float(input('\n digite a primeira nota:\t'))
no2=float(input('\n digite a segunda nota: \t'))

print(f'a media entre {no1} e {no2} = {((no1+no2)/2):.1f}')'''

#faca um prgrama que leia duas notas e imprima a media aritmetica truncada

'''no1=float(input('\n Digite a primeira nota: \t'))
no2=float(input('\n Digite a segunda nota: \t'))

print(f'a media truncada de {no1} e {no2} = {(no1+ no2)//2}')'''

#faca um programa que leia dois numeros inteiros e imprima o dividendo, o divisor, o resto e o quociente

'''no1=int(input('\n Digite o dividendo: \t'))
no2=int(input('\n Digite o divisor: \t'))
        
print(f'\n o dividendo dos numeros {no1} e {no2} = {no1}, o divisor é {no2}, o resto da divisâo é {no1%no2} e o resultado é {no1/no2}')'''

#faca um programa que leia dois lados de um triangulo retangulo e leia a hipotenusa

'''l1=int(input('\n Digite o primeiro angulo em cm:\t'))
l2=int(input('\n Digite o segundo angulo em cm:\t'))
l3=int
hip=((l1**2)+(l2**2))**0.5
print(f'\n A Hipotenusa do triando retangulo = {hip:.0f}')'''
      

#faca um programa que leia o ano atual e quantos anos uma pessoa fez ou fara nesse ano,
#em seguida, calcule o ano em que a pessoa nasceu

'''ano=int(input('\n Ano atual:\t'))
idade=int(input('\n Quantos anos fará, ou fez, nesse ano?:\t'))

print(f'Você nasceu em: {ano-idade}')'''

#faca um programa que entre com um numero de 3 digitos(em apenas uma variavel)
#e o escreva na ordem invesa que foi digitado

'''no1=int(input('\n digite um numero de 3 digitos:\t'))

primeiro=int(no1%10)
str(primeiro)

segundotruncado=int(no1//10)

segundo=int(segundotruncado%10)
str(segundo)

terceirotruncado=int(no1//100)

terceiro=int(terceirotruncado%10)
str(terceiro)

print(f'\n O numero {no1} reverso é {primeiro}{segundo}{terceiro}')'''



'''no1=int(input('\n digite um numero de 3 digitos:\t'))
inv=(no1%10)*100

no1=no1//10

inv+=(no1%10)*10

no1=no1//10

inv+=no1%10

print(f'resultado {inv}')'''


#10.05.22
#faca um programa que leia o raio e de o perimetro

'''r=int(input('Digite o raio da circunferencia: \t'))

p=2*3.14*r

print(f'O perimetro da circunferencia é: {p:.1f}')'''


# faca um programa que leia o valor de 3 massas e 3 distancias e calcule a forca coesao

'''m1=int(input('Digite a 1a massa: \t'))
m2=int(input('Digite a 2a massa: \t'))
m3=int(input('Digite a 3a massa: \t'))
d1=int(input('Digite a 1a distancia: \t'))
d2=int(input('Digite a 2a distancia: \t'))
d3=int(input('Digite a 3a distancia: \t'))

g=6.67*(10**-11)
f=g*(((m1*m2)/(d1**2))+((m1*m3)/(d2**2))+((m2*m3)/(d3**2))) 

print(f'a Forca coesao = {f}')'''

#faca um program que leia a temperatura em C e transforme para F

'''c=int(input('Digite a temperatura em C: \t'))

f=(9*c+160)/5

print(f'A temperatura {c} em F = {f:.0f}')'''

#faca um programa para calcular o volume de uma lata lendo o valor de raio e altura

'''r=float(input('Digite o raio da lata: \t'))

h=int(input('Digite a altura da lata: \t'))

v=3.14*(r**2)*h

print(f'O volume da lata é = {v:.1f}')'''


#faca um programa que leia um valor e diga o numero maximo de notas de 2 e moedas de 1 
#que o valor possa ser representados


'''v=float(input('Digite o valor: \t'))

notas=v//2

moedas=v%1

print(f'O valor {v} pode ser representado por {notas:.0f} de 2 reais ou {moedas:.0f} moedas de 1 real')'''


#faca um programa que leia as despesas e imprima o valor com uma gorjeta de 10%

'''d=float(input('Digite o valor gasto: \t'))

gorjeta=d+(d/10)

print(f'O valor gasto com gorjeta de 10% = {gorjeta:.1f}')'''

#faca um programa que leia hora, minuto e segundo e transforme para segundos

'''h=int(input('Digite a(s) horas: \t'))
m=int(input('Digite o(s) minutos: \t')) 
s=int(input('Digite o(s) segundos: \t'))

h=h*60
m=h+m
m=m*60
s=s+m

print(f'O horario indicado em Segundos = {s}')'''


#faca um programa que transforme segundos para hora, minutos e segundos

'''segundos=int(input('Digite os Segundos: \t'))

h=segundos//3600
m=segundos//60
s=segundos-m*60
m=m-h*60

print(f'os segundos em horas = {h}, em minutos = {m} e segundos = {s}')'''


#faca um programa que leia um numero binario de 4 digitos e mostre o decimal correspondente


b=int(input('Digite o código binário de 4 digitos: \t'))

primeiro=b//1000
primeiro=primeiro*8

segundo=b//100
segundo=(segundo%10)*4

terceiro=b//10
terceiro=(terceiro%10)*2

quarto=b%10
quarto=quarto*1

decimal=primeiro+segundo+terceiro+quarto

print(f'O numero binario {b} em decimal = {decimal}')

#faca um programa que leia um numero decimal de 0 a 15 e transforme para binario

'''dec=int(input('Entre com um numero decimal de 0 a 15: \t'))
aux=dec
bin=(dec%2)*1(10**0)
dec//=2
bin+=(dec%2)*(10**1)
dec//=2
bin+=(dec%2)*(10**2)
dec//=2
bin+=(dec%2)*(10**3)
dec=aux

print(f'{dec} na base 10 é equivalente à {bin} na base 2')'''