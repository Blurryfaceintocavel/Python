N_confi= ['Alice', 'Bruno', 'Denise','Roberta']
confi=[]

while N_confi:
    current_user= N_confi.pop()
    print ('usuarios verificados '+ current_user.title())
    confi.append(current_user)
    
print ("Usuario confirmado: ")
for confirmado in confi: 
     print(confirmado.title( ))
     
print ('\n ')
     
#Removendo todas as instâncias de valores específicos de uma lista

pets=['Cachorro','Gato', 'Hamster', 'Gato']
print (pets)
while 'Gato' in pets: 
    pets.remove('Gato')
print (pets)

print ('\n ')

#===

respostas= {}
ativo= True 
nome =input ('Informe seu nome: ')
resposta = input("Qual montanha você gostaria de escalar algum dia?")

respostas [nome] =resposta
repetir= input ('Você gostaria de deixar outra pessoa responder? (sim/não)')

if repetir == 'não':
    ativo= False
    
print ('==resultado==')

for nome, resposta in respostas.items():
    print( nome + " Voce gostaria de escalar " + resposta + ".")
    
print ('\n ')

