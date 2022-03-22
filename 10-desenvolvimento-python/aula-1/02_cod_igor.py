product_list = {
    'sonho': 5,
    'croissant': 4,
    'coxinha': 4,
    'pastel': 4.5,
    'refrigerante': 5
}

# print(product_list)

print('-'*10)
print('Produtos')
print('-'*10)

for key, value in product_list.items():
    print(key.ljust(15).capitalize(), ': R${: .2f}'.format(value))

print('-'*10)

id_product_list = []

count = 1
while count <= 2:
    id_product = input('Entre com ID do produto {}: '.format(count)).lower()
    if (id_product in product_list):
        count += 1
        id_product_list.append(product_list[id_product])
    else:
        print('Produto inválido {}'.format(id))

total = sum(id_product_list)
print('Valor total R${: .2f}'.format(total))
