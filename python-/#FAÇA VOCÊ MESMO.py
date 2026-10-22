

'''7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete.'''

resposta= {}
ativo= True 
nome= input ('Informe o seu nome: ')
resposta= input ('Se pudesse visitar um lugar do mundo, para onde você iria?')

respostas=[nome] =resposta

repetir =("Gostaria de inserir outra informação?? ")



if repetir == 'n':
    ativo= False

for nome, resposta in respostas.items():
    print( nome + " Voce gostaria de Visitar " + resposta + ".")