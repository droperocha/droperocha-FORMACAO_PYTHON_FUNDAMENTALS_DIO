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
