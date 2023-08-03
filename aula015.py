""" cont = 1
while True: # while True = sloop infinito
    print(cont, '-> ', end='')
    cont += 1
print('Acabou') """

""" n = cont = 0
while n != 999: # O 999 é meu Flag
    n = int(input('Digite um número: '))
    cont += 1 """

""" n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    s += n
s -= 999
print(f'A soma vale {s}') """

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
