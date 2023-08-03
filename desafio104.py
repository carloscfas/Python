def leiaInt(msg):
    while True:
        num = input(msg).strip()
        if num.isnumeric():
            return int(num)
        print('\033[31mERRO! Digite um número inteiro válido. \033[m')



# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
