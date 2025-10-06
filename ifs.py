# Programa que lê um número e informa se é positivo, negativo ou igual a zero.

num = int(input("Informe um número:"))

if num < 0:
    print ("Número negativo")
elif num == 0: 
    print ("Número igual a 0")
else: 
    print ("Número positivo")


# Programa que lê um número inteiro e informa se é par ou ímpar.


N= int (input ("Informe um número inteiro: "))
if N % 2 == 0:
    print("O número é par")
else: 
    print ("Número Impar ")


# Dizendo idade 

idade= int (input (" Digite idade: ") )

if idade <=12 and idade >=0:
    print ("Criança")       #Criança: de 0 a 12 anos
elif idade >=13 and idade <=17: 
    print ("Adolescente") #Adolescente: de 13 a 17 anos
else:
   print ("Adulto") #Adulto: 18 anos ou mais


#  Verificar se um número é múltiplo de 3 ou 5

mul= int (input (" Digite um número: "))

if mul % 3 ==0 :
    print ("Número multiplo de 3")
    
elif mul % 5 ==0:
    print ("Número multiplo de 5")

elif mul % 3 ==0 and mult % 5 ==0:
    print ("Número multiplo de 3 e 5")
else:
   print ("Número não é multiplo de 3 ou 5")

