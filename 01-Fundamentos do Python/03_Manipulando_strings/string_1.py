nome = "laYEnNE"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá Mundo!      "

print(texto + "." )
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")


menu = "Python"

print("####"+menu+"####")
print(menu.center(14))
print(menu.center(14,"#"))
print("P-y-t-h-o-n")
print("-".join(menu))

#Exemplo  meu
print()
print()
menu = "Python"
menu = "-".join(menu)
print(menu)
print(menu.center(30,"="))
