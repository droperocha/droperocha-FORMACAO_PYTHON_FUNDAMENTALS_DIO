saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Contando Cédulas, aguarde...\n")
    print("Retire as cédulas do local indicado!")
else:#senão, economiza memória
    print("Saldo insuficiente!")
'''
if saldo < saque:
    print("Saldo insuficiente!")'''

'''
elif é utilizado quando temos mais de um desvio
e temos de testar mais de uma condição porque o else somente finaliza
o elif me permite testar mais condições

if = se, faça
elif = senão, faça
else = senão, finalize

'''
