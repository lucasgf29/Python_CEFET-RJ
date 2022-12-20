#questao 7

# faca um programa para criar um arquivo de funcionario que contenha os campos:   
# nome, departamento e salario. 

# O programa termina quando nome=='fim'. 'fim' nao deve ser escrito no arquivo

'''def criaArq(nomeArq):       
    arq=open(nomeArq + '.txt', 'w')
    nome=input('entre com nome: ')
    while(nome.lower()!='fim'): 
        departamento=input('entre com departamento: ')
        salario=input('entre com salario: ')
        arq.write(f'{nome}, {departamento}, {salario} \n')
        nome=input('entre com nome: ') 
    arq.close()

nomeArq=input('entre com o nome do arquivo: ')
criaArq(nomeArq)'''


#faca um programa que leia o arquivo gerado na questao anterior, e em seguida calcule o
#aumento salarial de 70% para cada funcionario e crie o arquivo 'reajuste.txt'
#com 'nome, departamento, salario e salario reajustado' dos funcionarios dos funcionarios
#que tiveram aumento maior que 1000 (mil) reais

'''def criaArq(nomeArq):       
    arq=open(nomeArq + '.txt', 'w')
    nome=input('entre com nome: ')
    while(nome.lower()!='fim'): 
        departamento=input('entre com departamento: ')
        salario=input('entre com salario: ')
        arq.write(f'{nome}, {departamento}, {salario} \n')
        nome=input('entre com nome: ') 
    arq.close()

nomeArq=input('entre com o nome do arquivo: ')
criaArq(nomeArq)'''



'''def reajuste(nomeArq):
    arq=open(nomeArq, 'r')
    reajuste=open('reajuste.txt','w')
    
    for linha in arq:
        inicio=0
        fim=linha.find(',')
        
        nome=''
        nome+=linha[inicio:fim]
        inicio=fim+1
        fim=linha.find(',', inicio)
        
        departamento=''
        departamento+=linha[inicio:fim]
        inicio=fim+1
        fim=linha.find(',', inicio)
        
        salario=''
        salario+=linha[inicio:fim]
        salario=float(salario)
    
        aumento=salario*0.7
        salarionovo=salario+aumento
       
        salarionovo=str(salarionovo)
        salario=str(salario)
        
        if aumento>1000:
            reajuste.write(f'{nome}, {departamento}, {salario}, {salarionovo} \n')
    
    arq.close()
    reajuste.close()

    
nomeArq=input('entre com o nome do arquivo ja existente dos funcionarios: ')

reajuste(nomeArq)'''


#faca um programa que gere 1000 enderecos ip aleatorios, validos e invalidos

#num1 . num . num
#num 1 = 1-255
#num = 0-255


'''from random import randint

def ip(nomeArq):
    arq=open(nomeArq,'w')
    i=0
    while i<1000:
        arq.write(f'{randint(0,999)}.{randint(0,999)}.{randint(0,999)}.{randint(0,999)} \n')
        i+=1
    


nomeArq=input('entre com o nome do arquivo + .txt: ')
ip(nomeArq)'''

#separar em 2 arquivos, ip valido e invalido

def validacao(nomeArq):
    arq=open(nomeArq,'r')
    valido=open('ips_validos.txt','w')
    invalido=open('ips_invalidos.txt','w')
    
    for linha in arq:
        inicio=0
        fim=linha.find('.')
        
        num1=''
        num1+=linha[inicio:fim]
        num1=int(num1)
        inicio=fim+1
        fim=linha.find('.', inicio)
        
        num2=''
        num2+=linha[inicio:fim]
        num2=int(num2)
        inicio=fim+1
        fim=linha.find('.', inicio)
        
        num3=''
        num3+=linha[inicio:fim]
        num3=int(num3)
        inicio=fim+1
        fim=linha.find('.', inicio)
        
        num4=''
        num4+=linha[inicio:fim]
        num4=int(num3)

    
        if num1>=1 and num1<=255 and num2>=0 and num2<=255 and num3>=0 and num3<=255 and num4>=0 and num4<=255:
            num1=str(num1)
            num2=str(num2)
            num3=str(num3)
            num4=str(num4)
            valido.write(f'{num1}.{num2}.{num3}.{num4} \n')
        
        else:
            num1=str(num1)
            num2=str(num2)
            num3=str(num3)
            num4=str(num4)
            invalido.write(f'{num1}.{num2}.{num3}.{num4} \n')
        
    arq.close()
    valido.close()
    invalido.close
    
    
nomeArq=input('entre com o nome do arquivo que possui os ips +.txt: ')
validacao(nomeArq)