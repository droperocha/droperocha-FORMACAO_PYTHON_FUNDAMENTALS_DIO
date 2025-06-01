'''while True:#criando um while infinito
    opcao = int(input("Informe um número: "))
        
    if opcao == 10:
        break

    print(opcao)
'''


for numero in range(10):
    if numero == 5:#pulando o numero 5, o continue pula a condição e retorna
       continue
    print(numero, end=" ")

#break para o laço, corta a repetição, parar no momento em que a condição for atendida
#continue pula a execução

'''Programa criado pra exibir os números 
digitados E SÓ PARAR SE A CONDIÇÃO DO IF FOR ATENDIDA
break é muito utilizado par estruturas de repetições infinitas '''