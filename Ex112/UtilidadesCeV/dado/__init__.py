def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        num = input(msg).strip()
        if num.isnumeric():
            return int(num)
        print('\033[31mERRO! Digite um número inteiro válido. \033[m')
