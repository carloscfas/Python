print('-' * 40)
print('Loja Do Carlão')
print('-' * 40)

preço = float(input('Preço das Compras: R$'))
print(('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão '''))
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua Compra será parcelada em 2x de R${parcela} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparç = int(input('Quantas parcelas? '))
    parcela = total / totparç
    print(f'Sua compra será parcelada em {totparç}x de {parcela} COM JUROS')
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
print(f'Sua compra de R${preço} vai custar R${total} no final')
