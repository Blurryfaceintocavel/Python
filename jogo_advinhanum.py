import random

numeros = random.randint(1, 4)

palpite= int(input("Imagina o número que estou pensando: "))

if numeros == palpite:
  print ("ACERTOU!!! ")
 
elif numeros > palpite:
  print("Palpite alto", " \n Numero era: ", numeros)

elif numeros < palpite:
  print("Palpite baixo", " \n Numero era: ", numeros)

else:
  print("Errou :("," \n Numero era: ", numeros )
  
