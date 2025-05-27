texto = input("===== (Separador de vogais) =====\n Informe um texto: ")

VOGAIS = "AEIOU"


for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()#quebra de linha
    print("===== (Fim do Separador de Vogais) =====")

print("_____Tabuada de 5_____")
for numero in range(0, 51, 5 ):
    print(numero, end=" ")
else:
    print()
    print("_____ Fim da tabuada de 5 _____")