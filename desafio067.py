valor = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{valor} x {c} = {valor*c}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')