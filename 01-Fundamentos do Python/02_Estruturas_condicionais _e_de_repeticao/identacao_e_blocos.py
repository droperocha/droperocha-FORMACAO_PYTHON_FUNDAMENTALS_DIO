def sacar(valor):
    saldo = 500

    if saldo >=valor:
        print("valor sacado!")
        print("retire seu dinheiro do local indicado!")

    if saldo < valor:
            print("Saldo Insuficiente")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

sacar(100)