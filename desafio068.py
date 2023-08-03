from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = '  '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('-' * 35)
    print(f'Você jogou {jogador} e o Computador {computador}.Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 35)
    if tipo == 'P' or 'p':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I' or 'i':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente.....')
    print('=-=' * 35)
print(f'GAME OVER! Você venceu {v} vezes.')
