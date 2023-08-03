'''for c in range(1, 10):
    print(c)
print('FIM')'''

# quando eu sei o Limite posso usar tanto for quanto o While
# quando eu não sei o limite tenho que usar o While

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer Continuar? [S/N]')).upper()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números par e {impar} números ímpares! ')
