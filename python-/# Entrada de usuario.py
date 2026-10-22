# Entrada de usuario 

prompt = 'Dizer-me seu nome. '
prompt += 'Qual é seu nome? '

name = input(prompt)

print(f'\nOlá, {name}!')

print ('\n')

#para informar que o valor e número utilizamos int()

num= int (input('Digite um número '))

total= num + 5 

print (total)

print ('\n')
# Exemplo 2.2

idade= int (input('informe sua idade: '))

if idade >=18:
    print ('Voce pode dirigir')
else:
    print ("Vc não tem idade suficiente")
   
print ('\n ====================') 

#FAÇA VOCE MESMO 

'''7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário qual
tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse carro, por
exemplo, “Deixe-me ver se consigo um Subaru para você.”'''

car= input('Qual carro vc quer utilizar?? ')
print(f'Deixe-me ver se consigo um  {car} para você')

print ('\n')

'''7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta.'''

con=int (input('Informe a quantidade de convidados: ')) 

if con >8: 
    print ('Aguarde uma mesa maior')
else: 
    print ('Sua mesa está pronto ')
    
print ('\n')
     
'''7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não'''

ten=int (input('Informe um número: ')) 

if ten % 10 == 0:
    print ('Multiplo de 10 ') 
else: 
    print ('Número não é multiplo de 10 ')