'''
curso ="pYtHon"

print(curso.upper())
# Converte todos os caracteres para maiusculo

print(curso.lower())
# Converte todos os caracteres para minusculo

print(curso.title())
# Converte todos os caracteres para minusculo com excessão do primeiro caracter

curso = "     Python   "

print(curso.strip())
# Remove os espaços do inicio e do fim da variavel

print(curso.lstrip())
# Remove os espaços só do lado esquerdo da variavel

print(curso.title())
# Remove os espaços só do lado direito da variavel

curso = "Python"

print(curso.center(20, "="))#Primeiro argumento diz quantos caracters vai ter na variavel
# Centraliza a string e adiciona o segundo argumento aos lados 

print(".".join(curso))
#Parecido com o for ele junta a instrução a cada letra da variavel string

'''
#interpolação de variaveis

# metodo oldstyle NÃO RECOMENDADO

'''
nome = "Pedro"
idade = 27
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome,idade,profissao,linguagem))
# %s string 
# %d inteiro
# %f ponto flutuante 

'''

# metodo format
'''
nome = "Pedro"
idade = 27
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome,idade,profissao,linguagem))#Manteve o mesmo dilema e problema apresentado no jeito old style em códigos ou frases grandes esse estilo fica dificil de compreender

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {0} e estou matriculado no curso de {1}." .format(nome,idade,profissao,linguagem))#errado de propósito

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(nome=nome,idade=idade,profissao=profissao,linguagem=linguagem))#Olha como ficou muito mais fácil

# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))#Olha como ficou muito mais fácil

'''

# metodo f-string
nome = "Pedro"
idade = 27
profissao = "Programador"
linguagem = "Python"

print(F"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")#melhor que o format mais fácil não precisa passar a sequencia de variaveis no final.

PI = 3.14159265358979323846

print(f"Valor de PI: {PI: .2f}")#2f numero de casas que voce quer da variavel
print(f"Valor de PI: {PI: 10.2f}") #10 é o numero de casas para adicionar antes do resultado

