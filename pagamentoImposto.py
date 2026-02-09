
def calc ():

    #Entrada Usuario 
    
    salario= float (input ("Digite o valor do salário: "))
    beneficio= float (input ("Digite o valor do beneficio: "))

    #Calculo do imposto
    imposto = 0

    if salario >= 0 and salario <=1100:
        imposto=0.05 * salario
    elif salario > 1100 and salario <= 2500:
        imposto=0.10 * salario
    else :
        imposto= 0.15 * salario 

    pagamento= salario + beneficio - imposto 
    return pagamento

#pagamento 

pagamento = calc ()
print (f"O valor do pagamento é: {pagamento:.2f}")
