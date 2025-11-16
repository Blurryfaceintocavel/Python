##D20

#import random

#dado= random.randint (1,20)

#print( dado ,"<-1d20 ")

import sys
import random

print("+" + "-"*30 + "+")
print("|{:^30}|".format("SELECIONE O DADO"))
print("+" + "-"*30 + "+")

dados = [
    "[1] D2",
    "[2] D4",
    "[3] D6",
    "[4] D10",
    "[5] D12",
    "[6] D20" ,
     "[7] Sair"
]

for dados in dados:
    print("|{:^30}|".format(dados))

print("+" + "-"*30 + "+")

dados = int(input("Digite a opção: "))

#Inicio dos testes condicionais

if dados == 1:
    dado = random.randint(1, 2) #d2
    print(dado ,"<-1d2 ")
elif dados == 2:
    dado = random.randint(1, 4) #d4
    print(dado ,"<-1d4 ")
elif dados == 3:
    dado = random.randint(1, 6) #d6
    print(dado ,"<-1d6 ")
elif dados == 4:
    dado = random.randint(1, 10) #d10
    print(dado ,"<-1d10 ")
elif dados == 5:
    dado = random.randint(1, 12) #d12
    print(dado ,"<-1d12 ")
elif dados == 6:
    dado = random.randint(1, 20) #d20
    print(dado ,"<-1d20 ")
elif dados == 7:
    sys.exit("Saindo...")
else:
    sys.exit("Opção inválida")
