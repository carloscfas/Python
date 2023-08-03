print('-'*20)
cont = 0
soma = 0
num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} Números e a soma entre eles foi {soma}')
print('Fim')

# Tive que colocar minha váriavel fora do While e no Último no While, para o Flag não contar
