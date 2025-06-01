conta_normal = False
conta_universitaria = True


saldo = 2000.0
saque = float(input("Valor do saque: "))
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque<= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else:
        print("Saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Não é possivel sacar dinheiro sem antes acessar uma conta!")