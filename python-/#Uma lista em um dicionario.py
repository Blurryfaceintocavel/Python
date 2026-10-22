#Uma lista em um dicionario

pizza= { 'Borda': 'Grossa', 
    'Ingrediente' : ['Catupiry', 'Cogumelo', 'Cebola'],   
}

#resumo

print ('Vc pediu uma ' + pizza ['Borda'] + '-Borda Pizza ' + 'Seguido dos ingredientes: ')
for cobertura in pizza['cobertura']:
    print ('\t' + cobertura)    

print ("\n ==================")
