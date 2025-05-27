opcao = 1

while opcao !=0:#é parecido com o if a diferença é que ela vai ser executada indefinidamente até a condição ser atendida
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao ==1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, tenha um bom dia!")