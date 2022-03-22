import re
lista = []

for i in range(3):
    palavra = input('Digite uma palavra:')
    lista.append(palavra)


for index, palavra in enumerate(lista):

    match index:

        case 0:
            lista[0] = lista[0].upper()
            print(lista[0])
        case 1:
            lista[1] = lista[1].casefold()
            print(lista[1])
        case 2:
            lista[2] = re.sub("[aeiouAEIOU]", "", lista[2].upper())
            print(lista[2])
