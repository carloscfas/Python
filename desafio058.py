""" from random import randint
from time import sleep
print('-=-' * 20)
print('VOu pensar em um número entre 0 e 5. Tente adivinhar......')
print('-=-' * 20)
p = int(input('Digite o número que o Computador escolheu entre 1,5: '))
n = randint(1,5)
print('PROCESSANDO....')
sleep(2)
print(f'O Computador escolheu o número {n}')
if p == n:
    print('Parabéns você Ganhou')
else:
    print('Ops , Você Perdeu!') """
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos....Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
