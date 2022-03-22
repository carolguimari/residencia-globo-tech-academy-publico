sentence = input('Entre com a frase:')

words = sentence.split(' ')

print('-'*10)
for word in words:
    print(word[:2], end=' ')

print('\n' + '-'*10)
for word in words:
    print(word[2:], end=' ')
