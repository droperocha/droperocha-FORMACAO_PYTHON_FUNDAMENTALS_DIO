# Filtro versão 1
numeros =[1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)#adiciona valores na lista

print (pares)

# Filtro versão 2

numeros =[1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0] #parece dificil mas é um jeito de fazer em uma linha só


print (pares)


#Modificando valores versão 1
numeros =[1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)#Eleva ao quadrado

print (quadrado)

#Modificando valores versão 2
numeros =[1, 30, 21, 2, 9, 65, 34]
quadrado = [numero **2 for numero in numeros]
print (quadrado)
