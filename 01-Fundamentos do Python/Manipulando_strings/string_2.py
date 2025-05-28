nome = "Pedro"
idade = 28
profissao = "Programador"
linguagem = "Python"

saldo = 15.135546578

dados = {"nome": "Pedro","idade": 28}

print("Nome: %s Idade %d" %(nome,idade))

print("Nome: {} Idade {}" .format(nome,idade))

print("Nome: {0} Idade {1}" .format(nome,idade))

print("Nome: {name} Idade {age}" .format(name=nome,age=idade))

print("Nome: {nome} Idade {idade}" .format(**dados))

print(f"Nome: {nome} Idade {idade}")

print(f"Nome: {nome} Idade {idade} saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade {idade} saldo: {saldo:15.2f}")
