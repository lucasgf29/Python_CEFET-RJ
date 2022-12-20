# def S(n):
#     def fat(n):
#         if n==0:
#             return 1
#         else: 
#             return fat(n-1)*n
    
    
#     if n==0:
#         return 1
#     else:
#         return S(n-1)+1/fat(n)
    

# n=int(input('entre com n: '))
# print(f'S({n})= {S(n)}')

#funcao recursiva que calcule x^z sem usar **

# def pot (x,z):
#     if x==0 and z<=0:
#         print('erro!')
        
#     if x==0 and z>0:
#         return 0
    
#     if x!=0 and z==0:
#         return 1
    
#     if x!=0 and z>0:
#         if z==1:
#             return x
#         else:
#             return pot(x,z-1)*x
        
#     if x!=0 and z<0:
#         return 1/pot(x,-z)
        
# x,z=input('entre com X e Z: ').split()
# x=float(x)
# z=int(z)


# print(f'{x}^{z} = {pot(x,z)}')

#***************************** IMPORTANTE ******************************** 

'''def mostra(n):
    if n==1:
        print('1', end='\t')
    else:
        print(n,end='\t')
        mostra(n-1)
        print(n,end='\t')

def mostra2(n):
    if n==1:
        mostra(1)
    else:
        mostra(n)
        print()
        mostra2(n-1)
        print()
        mostra(n)
        
       
        
n=int(input('entre com um numero: '))
mostra(n)'''

    #***************************** IMPORTANTE ****************************** 

# def tab(n,y):

#     if y<=10:
#         print(f'{y} x {n} = {n*y}')
#         tab(n,y+1)
    
    
    
# n=int(input('entre com um numero: '))
# y=1
# tab(n,1)


# def fibo(n):
#     if n==1 or n==2:
#         return 1
#     else:
#          return fibo(n-1)+fibo(n-2)
    
# n=int(input('entre com n: '))
# print(fibo(n))


'''def fibo(n):
    if n==1 or n==2:
        return 1
    
    else:
        return fibo(n-1)+fibo(n-2)
    
n=int(input('entre com um numero inteiro positivo: '))
print(n**fibo(n))'''

'''def tri(n):
    if n==1:
        return 1
    
    else:
        return tri(n-1)+n
    
n=int(input('entre com um valor para n: '))
print(tri(n))'''


### fiz sozinho em casa -------> 
'''def p(ano):
    if ano<=0:
        return ('erro!')
    
    if ano==1:
        return 500.00
    
    else:
        return p(ano-1)*1.1

        
        
    
ap=500.00
ano=int(input('entre com o ano que deseja saber: '))
print(p(ano))'''




'''def pent(n):
    if n==1:
        return 1
    
    else:
        return pent(n-1)+3*n-2
    
n=int(input('entre com um valor para n: '))
print(pent(n))'''



'''def fibo(n): 
    if n==1 or n==2:
        return 1
    
    else:
        return fibo(n-1)+fibo(n-2)
    

def fat(n):
    if n==0:
        return 1

    else:
        return fat(n-1)*n
    
    
n=int(input('entre com valor para n: '))
print(n**fat(fibo(n)))'''



'''def bin_dec(n,i=1):
    if n==0:
        return 0
    else:
        return (n%10)*i+bin_dec(n//10,i*2)
    
    
binario=int(input('entre com um valor binario: '))
decimal=bin_dec(binario,1)
print(F'{binario} base 2 = {decimal} base 10')'''


#reescreva a funcao primo sem usar repeticao

def primo(n,i=1,cont=0):
    
    if i==n+1:
        if cont==2:
            print('primo')
        else:
            print('nao é primo')
    else:
        
        if n%i==0:
            cont+=1
            
        primo(n,i+1,cont)
        

        

n=int(input('entre com numero: '))

primo(n)
