total = total_produtos = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço do Produto:R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        total_produtos += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total gasto nas compras foi {total} Reais')
print(f'Temos {total_produtos} produtos custando mais de 1000 reais')
print(f'O produto mais barato foi {barato} que custa R$ {menor}')
