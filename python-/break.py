adm = "123"

print("Insira X para sair do programa \n")

while True:
    user = input('Insira sua senha: ')

    if user == 'X':
        break

    elif user != adm:
        print("Senha incorreta \n")

    else:
        print("Acesso permitido \n")

'''============ FAÇã vc memo============='''

'''7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.'''

#Ingrediente

print("Insira quiet para sair do programa \n")

while True:
    ingredient = input('Informe os ingredientes: ')

    if ingredient == 'quiet':
        break
    else:
        print('Acrescentando item ' + ingredient.title() + '.')
        
print ('\n')

'''7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.
Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
o preço do ingresso do cinema.'''

idade = int(input("Informe a idade: "))

if idade < 3:
    print("Ingresso Gratuito")

elif idade <= 12:
    print("10 Reais")

else:
    print("15 Reais")


7.6

# Break

mensagem = '\nInsira a sua idade: '
mensagem += '\nInsira (quiet) para sair do programa: '

while True:
    idade = input(mensagem)

    if idade == 'quiet':
        break

    else:
        idade = int(idade)

        if idade < 3:
            print("Ingresso Gratuito")

        elif idade <= 12:
            print("10 Reais")

        else:
            print("15 Reais")
      
    print ('\n')      
# ative
prompt= 'Insira a sua idade pt2: '
prompt += 'Entre com quiet para encerrar o programa'
ativo= True
while ativo:
    mensagem= input(prompt)
if mensagem == 'quiet':
   ativo= False
else:
        idade = int(idade)

        if idade < 3:
            print("Ingresso Gratuito")

        elif idade <= 12:
            print("10 Reais")

        else:
            print("15 Reais")