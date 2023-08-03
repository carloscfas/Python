numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    usuario = int(input('Digite um número entre 0 e 20:  '))
    if 0 <= usuario <= 20:
        break
    print('Tente Novamente. Digite um número entre 0 e 20! ')
print(f'Vocẽ digitou o número {numeros[usuario]} ')
