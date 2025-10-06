#Operação lógica E (AND)

#and é um operador lógico que retorna True se ambas as expressões ao seu redor forem verdadeiras. 
#Caso contrário, retorna False.

# Exemplo 1: Ambas as expressões são verdadeiras

idade= 20
idade_tirar_CNH = True

print(idade >= 18 and idade_tirar_CNH == True )  # True

# Exemplo 2: Uma expressão é falsa
idade = False 
idade_tirar_CNH = True

print(idade >= 18 and idade_tirar_CNH == True )  # False

# Exemplo 3: Ambas as expressões são falsas

idade = False 
idade_tirar_CNH = False

print(idade >= 18 and idade_tirar_CNH == True )  # False

#Usuario informa a idade

idade= int (input  (f"Qual a sua idade? "))
idade_tirar_CNH= 18

if idade >= 18 and idade >= idade_tirar_CNH:
    print(f"Você pode tirar a CNH: {idade}")
else:
    print(f"Você não pode tirar a CNH idade maxima e de {idade_tirar_CNH} anos e você tem {idade} anos")

print ("------------OR-------------------")

#Operação lógica OU (OR)
#or é um operador lógico que retorna True se pelo menos uma das expressões ao seu redor for verdadeira.
#Caso ambas as expressões sejam falsas, retorna False.

acompanhamento= True
idade_sem_acompanhamento= 16
idade= 15

print (idade >= idade_sem_acompanhamento or acompanhamento == True) # True


# false

acompanhamento= False
idade_sem_acompanhamento= 16
idade= 15
print (idade >= idade_sem_acompanhamento or acompanhamento == True) # False



#Usuario informa a idade

idade= int (input  (f"Qual a sua idade? "))
idade_sem_acompanhamento= 16
acompanhamento= input (f"Você está acompanhado? S/N: ")

if acompanhamento == "S": 
   acompanhamento = True
else:
    acompanhamento == "N"
    acompanhamento = False
if idade >= idade_sem_acompanhamento or acompanhamento == True:
    print (f"Você pode entrar no cinema, sua idade é {idade} anos")
else:
    print (f"Você não pode entrar no cinema, sua idade é {idade} anos")

print ("------------NOT-------------------")

#Operação lógica NÃO (NOT)
#not é um operador lógico que inverte o valor de uma expressão.
#Se a expressão for True, not a torna False. Se a expressão for False, not a torna True.

suspeito= False
print (not suspeito) # False
