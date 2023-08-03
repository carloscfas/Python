from random import randint
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
    print('Ops , Você Perdeu!')
