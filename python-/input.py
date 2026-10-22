mensagem =input ('Diga algo que eu repetirei: ') 
print (mensagem)

('\n')

prompt= 'testando as mensagem com prompt'
prompt+='\n qual e seu primeiro nome? '
name= input (prompt)

print("\nHello, " + name + "!")

('\n')

#Usando numero 

num=int (input("Informe um número: "))

if num  %2 ==0: 
    print("Número e par" )
else: 
    ('impar')

('\n')
'''===================================='''

#Entrada Usuario

'''7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário qual
tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse carro, por
exemplo, “Deixe-me ver se consigo um Subaru para você.”'''

car=input ("Qual carro voce gostaria de alugar: ")
print ("verei se consigo " + str(car) +  ' para voce')


'''7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
exiba uma mensagem dizendo que eles '''

pe=input("quantas pessoas irão ao restaurante?? ")
pe =int(pe)

if pe >= 8:
    print ("Terá que esperar a mesa")
else: 
    ("mesa pronta")
    
'''7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não'''

num = int(input("Digite um número: "))

if num % 10 == 0:
    print ('Numero e multiplo de dez')
else: 
    print ('Número não e multiplo de dez')



'''======================================================='''

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = " "

while message != 'quit':
    message = input(prompt)
    print(message)
    
print('\n')

ativo= True
while ativo: 
    mensagem= input( prompt)
    
    if mensagem == 'Quit':
       ativo = False
    else:
        print(mensagem )