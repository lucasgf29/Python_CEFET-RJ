#faca um programa que leia um numero, e se ele for maior que 20 entao imprima metade
#do numero, caso contrario imprima o dobro do valor

'''n=int(input("Digite o Número: \t"))

if(n>20):
    print(f'Como {n} é maior que 20, sua metade = {n/2:.0f}')
    
else:
    print(f'Como {n} é menor ou igual a 20, seu dobro = {n*2:.0f}')'''


#faca um programa que leia um numero e diga se esse numero é positivo, negativo ou nulo
'''n=int(input('Digite um Número: \t'))

if(n>0):
    print(f'{n} é positivo')
    
elif(n<0):
    print(f'{n} é negativo')

else:
    print(f'{n} é nulo')'''


#faca um programa que imprima a raiz quadrada de um numero caso ele seja positivo 
#e o quadrado do numero caso ele seja negativo
'''n=int(input('Digite um Número: \t'))

if(n>0):
    print(f'Como {n} é positivo, sua raiz quadrada = {n**0.5:.1f}')
    
elif:    
    print(f'Como {n} é negativo, seu quadrado = {n*n} ')

else:
    print(f'{n} é nulo')'''

#faca um pograma que leia um peso no planea terra e o numero de um planeta e 
#imprima o valor do seu peso neste planeta

'''peso=int(input('Digite seu peso em Kg: \t'))
pl=int(input('Digite a ID do planeta: \t'))

if(pl==1 or pl==2 or pl==3 or pl==4 or pl==5 or pl==6):
    if(pl==1):
        print(f'Seu peso em Mercúrio = {peso*0.37}Kg')
    elif(pl==2):
        print(f'Seu peso em Vênus = {peso*0.88}Kg')
    elif(pl==3):
        print(f'Seu peso em Marte = {peso*0.38}Kg')
    elif(pl==4):
        print(f'Seu peso em Júpiter = {peso*2.64}Kg')
    elif(pl==5):
        print(f'Seu peso em Saturno = {peso*1.15}Kg')
    else:
        print(f'Seu peso em Urano = {peso*1.17}Kg')    
else:
    print('ID de Planeta Inválido')'''
    
#faca um programa que leia um caractere alfanumerico e dia se ele e uma vogal

'''car=input('Digite um Caracter Alfanumérico: \t')
if(len(car)!=1):
    print('Nao foi digitado um caracter!')
else:
    car=car.upper()
if(car=='A' or car=='E' or car=='I' or car=='O' or car=='U'):
    print(f'O Caracter "{car}" é uma vogal')

else:
    print(f'O Caracter {car} nâo é uma vogal')'''

#faca um programa que leia um caractere alfanumerico e diga se ele é consoane, numero ou vogal

'''car=input('Digite um Caracter Alfanumérico: \t')
if(len(car)!=1):
    print('Nao foi digitado um caracter!')
else:
    car=car.upper()
    if(car=='A' or car=='E' or car=='I' or car=='O' or car=='U'):
        print(f'{car} é Vogal')
    elif(car=='0' or car=='1' or car=='2' or car=='3' or car=='4' or car=='5' or car=='6' or car=='7' or car=='8' or car=='9'):
        print(f'{car} é um Número')
    else:
        print(f'{car} é Consoante')'''


#faca um programa que peca para o usuario entrar com uma senha (definida como 
#constante a um programador) e diga se a senha esta coreta

'''senha=input('Digite a senha: \t')

if(senha=='admin'):
    print('Senha Correta')
    
else:
    print('Senha Incorreta, Digite Novamente')'''

#faca um programa que leia um numero e diga se ele é ou nao é multiplo de 3

'''n=int(input('Digite o Número: \t'))
if(n%3==0):
    print(f'o Numero {n} é multiplo de 3')
else:
    print(f'o Numero {n} nao é multiplo de 3')'''
    
#faca um programa que leia um numero e diga se ele é ou nao é divisivel por 5

'''n=int(input('Digite o Número: \t'))
if(n%5==0):
    print(f'o Numero {n} é divisivel por 5')
else:
    print(f'o Numero {n} nao é divisivel por 5')'''

#faca um pograma que leia um numero e diga se ele é divisivel por 3 e por 7

'''n=int(input('Digite o Número: \t'))
if(n%3==0 and n%7==0):
    print(f'o Numero {n} é divisivel por 3 e por 7')
else:
    print(f'o Numero {n} nao é divisivel por 3 e por 7')'''
    
#faca um programa que leia um numero e diga se ele é divisivel por 21

'''n=int(input('Digite o Número: \t'))
if(n%21==0):
    print(f'o Numero {n} é divisivel por 21')
else:
    print(f'o Numero {n} nao é divisivel 21')'''
    
#faca um pograma que leia um numero e diga se ele esta compreendido entre 20 e 90 ou nao

'''n=int(input('Digite o Número: \t'))
if(n>=20 and n<=90):
    print(f'o Numero {n} esta compreendido entre 20 e 90')
else:
    print(f'o Numero {n} nao esta compreendido entre 20 e 90')'''
    
#faca um programa que lea a sigla do estado em que uma pessoa nasceu e imprima sua naturalidade
'''est=input('Digite a Sigla do Estado: \t')
if(len(est)!=2):
    print('Sigla Incorreta!')
else:
    est=est.upper()
    if(est=='RJ'):
        print('Você é Carioca!')
        
    elif(est=='SP'):
        print('Você é Paulista')
        
    elif(est=='BA'):
        print('Você è Bahiano')
        
    elif(est=='MG'):
        print('Você é Mineiro')
        
    else:
        print('Outros Casos')'''
        
#faca um programa que leia um numero inteiro de 3 digitos e informe se o algarismo
#da casa das centenas é par ou impar

'''n=int(input('Digite o Numero de 3 digitos: \t'))
x=n
c=n//100
x=n/100

if(x<1):
    print(f'o Numero {n} é inválido')
    
elif(c%2==0):
    print(f'a centena do numero {n} é par')
                
else:
    print(f'a centena do numero {n} é impar')'''
    
#faca um programa que leia 2 palavas e diga se elas sao iguais ou diferentes

'''p1=input('Digite a primeira palavra: \t')
p2=input('Digite a segunda palavra: \t')

if(p1==p2):
    print(f'As palavras |{p1}| e |{p2}| sâo iguais')
else:
    print(f'As palavras |{p1}| e |{p2}| são diferentes')'''
    
#faca um programa que leia 3 numeros diferentes e os imprima em ordem crescente e decrescente
#se houver numeros iguais exibir mensagem de erro

'''n1=int(input('Digite o 1o numero: \t'))
n2=int(input('Digite o 2o numero: \t'))
n3=int(input('Digite o 3o numero: \t'))

if(n1==n2 or n1==n3 or n2==n3):
    print('Numeros iguais não sâo Aceitos')
else:
    if(n1>n2 and n2>n3):
        print(f'ordem crescente {n3}<{n2}<{n1}')
        print(f'ordem decrescente {n1}>{n2}>{n3}')
        
    elif(n1>n3 and n3>n2):
        print(f'ordem crescente {n2}<{n3}<{n1}')
        print(f'ordem decrescente {n1}>{n3}>{n2}')
        
    elif(n2>n1 and n1>n3):
        print(f'ordem crescente {n3}<{n1}<{n2}')
        print(f'ordem decrescente {n2}>{n1}>{n3}')
        
    elif(n2>n3 and n3>n1):
        print(f'ordem crescente {n1}<{n3}<{n2}')
        print(f'ordem decrescente {n2}>{n3}>{n1}')
    
    elif(n3>n1 and n1>n2):
        print(f'ordem crescente {n2}<{n1}<{n3}')
        print(f'ordem decrescente {n3}>{n1}>{n2}')   
        
    elif(n3>n2 and n2>n1):
        print(f'ordem crescente {n1}<{n2}<{n3}')
        print(f'ordem decrescente {n3}>{n2}>{n1}')'''
        
        
#faca um programa que leia 3 numeros e diga se eles podem ou nao formar um triangulo e informe o triangulo

'''n1, n2, n3=input("Entre com os 3 lados do Triângulo:").split()
n1=float(n1)
n2=float(n2)
n3=float(n3)

if(n1+n2>n3 and n2+n3>n1 and n1+n3>n2):
    if(n1==n2 and n2==n3):
        print('O Triângulo é Equilátero!')

    elif(n1==n2 and n2!=n3):
        print('O Triângulo é Isósceles')
    
    else:
        print('O Triângulo é Escaleno')
    
else: 
    print('O Triângulo é inválido')'''
    

#faca um programa que leia os coeficientes de uma equacao do segundo grau e calcule suas raizes
#o programa deve mostrar quando possivel o valor das raizes calculadas e a classificacao das mesmas
#(raizes imaginarias, raiz unica o raizes reais distintas)

'''a,b,c=input('Entre com a,b e c:').split()
a=float(a)
b=float(b)
c=float(c)
delta=b**2-4*a*c
if delta<0:
    print('Raizes Imaginárias!')
elif delta==0:
    x=-b/(2*a)
    print(f'Raiz única = {x:.2f}')
else:
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print(f'Raizes distintas x1={x1:.2f} e x2={x2:.2f}')'''


#vender o produto com lucro de 45% caso seja maior que 20BRL, se menor, lucro 30%

'''p=float(input('Digite o Valor inicial do produto: \t'))
qc=p*(45/100)+p
t=p*(30/100)+p
if(p<20 and p>0):
    print(f'O produto comprado por {p:.2f} BRL poderá ser vendido, visando um lucro de 30%, por {t:.2f} BRL ')
else:
    print(f'O produto comprado por {p:.2f} BRL poderá ser vendido, visando um lucro de 45%, por {qc:.2f} BRL')'''
    
    
    
#faca um programa que leia 2 notas do aluno e diga se esta aprovado, reprovado ou pf (>=7 aprovado, <3 reprovado, resto pf)

'''nome=input('Entre com seu nome: \t)
n1,n2=input('Digite as 2 notas: \t').split()
n1=int(n1)
n2=int(n2)

md=(n1+n2)/2

if(md>=7):
    print(f'O Aluno {nome} ficou com média {md} e está Aprovado!')
    
elif(md<3):
    print(f'O Aluno {nome} ficou com média {md} e está Reprovado')

else:
    print(f'O Aluno {nome} ficou com média {md} e está em Prova Final!')'''
    
    

#faca um programa que leia um numero binario de 4 digitos e diga quantos digitos zero existem nesse numero

bi=str(input('Digite um Numero Binário de 4 Digitos:\t'))
if(len(bi)!=4):
    bi=int(bi)
    print(f'O binário {bi} é inválido!')

else:
  bi=int(bi)

  primeiro=bi//1000
  primeiro=primeiro*8

  segundo=bi//100
  segundo=(segundo%10)*4

  terceiro=bi//10
  terceiro=(terceiro%10)*2

  quarto=bi%10
  quarto=quarto*1

  decimal=primeiro+segundo+terceiro+quarto


  if(decimal==8):
      print(f'O binário {bi} possui 3 zeros')
  elif(decimal==9):
      print(f'O binário {bi} possui 2 zeros')
  elif(decimal==10):
      print(f'O binário {bi} possui 2 zeros')
  elif(decimal==11):
      print(f'O binário {bi} possui 1 zeros')
  elif(decimal==12):
      print(f'O binário {bi} possui 2 zeros')
  elif(decimal==13):
      print(f'O binário {bi} possui 1 zeros')
  elif(decimal==14):
      print(f'O binário {bi} possui 1 zeros')
  elif(decimal==15):
      print(f'O binário {bi} não possui zeros')
  else:
      print(f'O binário {bi} é inválido!')
       
