""" num = 0
continuar = 0
cont = 1
media = 0
maior = 0
menor = 0
while num >= 0:
    num = int(input('Digite um número: '))
    continuar = str(input('Quer Continuar? [S/N]')).strip()
    cont += 1
    media = num * 4
    maior = 0
    menor = 0
print(f'Você Digitou {cont}Números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print('Fim') """

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você Digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
