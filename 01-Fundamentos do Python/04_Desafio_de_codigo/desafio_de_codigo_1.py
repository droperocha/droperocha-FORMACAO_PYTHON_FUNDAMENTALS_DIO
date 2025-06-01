#tive que tirar toda esa enfeitada que dei pois o teste só queria um string escrita "Par" ou "Ímpar"


# Solicita ao usuário um número inteiro
numero = int(input("Digite um valor e te direi se ele é par ou impar: "))
par = numero%2


if par == 0:
    print(f"O número {numero} é par")

else:
    print(f"O número {numero} é impar")
# TODO: Verifique se o número é par ou ímpar e imprima o resultado:
