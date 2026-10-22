# FUNÇÃO SIMPLES

def saudacao():
    print('Hello world this is function')


saudacao()


# FUNÇÃO COM INFORMAÇÃO

def hihi(username):
    print('Hello ' + username.title() + '!')


hihi('mundinho')


# FUNÇÃO COM VÁRIAS INFORMAÇÕES

def petsdesc(tipo, nome):
    print('Eu tenho um animal ' + tipo + '.')
    print('O nome dele é ' + nome + '.')


petsdesc('Gato', 'Kitty')
petsdesc('Hamster', 'Bolinha')


# FUNÇÃO COM PARÂMETRO DEFAULT

def job(name, empresa='Refrio'):
    print('Nome do funcionário: ' + name)
    print('Trabalha na empresa: ' + empresa)


job(name='Bruno')
job(name='Jose')


print('\n')


# ==================================================
# 8.3 – CAMISETA
# ==================================================

def make_shirt(tam, estam):
    print('Tamanho da camiseta é: ' + tam)
    print('A estampa dela é: ' + estam)


# Argumentos posicionais
make_shirt('GG', 'Good Vibes')


# Argumentos nomeados
make_shirt(tam='M', estam='Eu amo Python')


print('\n')


# ==================================================
# 8.4 – CAMISETAS GRANDES
# ==================================================

def make_shirt2(tam2='Grande', estam2='Eu amo Python'):
    print('Tamanho da camiseta é: ' + tam2)
    print('A estampa dela é: ' + estam2)


# Camiseta grande com mensagem default
make_shirt2()

# Camiseta média com mensagem default
make_shirt2('Média')

# Camiseta de qualquer tamanho com mensagem diferente
make_shirt2('P', 'Good Vibes')


print('\n')


# ==================================================
# 8.5 – CIDADES
# ==================================================

def describe_city(cidade, pais='Japão'):
    print(cidade + ' está localizada no ' + pais)


describe_city('Tokyo')
describe_city('Osaka')
describe_city('São Paulo', 'Brasil')


print('\n')


# ==================================================
# FUNÇÃO COM RETURN
# ==================================================

def complname(nome, sobrenome):
    complete = nome + ' ' + sobrenome
    return complete.title()


nomee = complname('mariah', 'iasmyn')
print(nomee)


print('\n')


# ==================================================
# FUNÇÃO COM DICIONÁRIO
# ==================================================

def construcao_pessoa(nome, sobrenome):
    pessoa = {
        'First': nome,
        'sobrenome': sobrenome
    }

    return pessoa


person = construcao_pessoa('jaqueline', 'silva')
print(person)


print('\n')


# ==================================================
# FUNÇÃO COM LAÇO WHILE
# ==================================================

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""

    full_name = first_name + ' ' + last_name

    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")

    if f_name == 'q':
        break

    l_name = input("Last name: ")

    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)

    print("\nHello, " + formatted_name + "!")


print('\n')


# ==================================================
# 8.6 – NOMES DE CIDADE
# ==================================================

def city_country(cidade, pais):
    CyCon= cidade + ',  ,'+ pais
 
cidade_pais= city_country('new york', 'eua')
cidade_pais= city_country('RJ', 'Brasil')
print (cidade_pais)

# ==================================================
# 8.7 – Álbum
# ==================================================
    
