frase = str(input('Digite alguma coisa: ')) .strip().upper() # removi espaços e tornei MAIUSCULO
palavras = frase.split() # peguei minha frase e divide ela com o split = DIVISÃO DE FRASE
junto = ''.join(palavras) # peguei minha frase e usei o join para fazer uma junção em " - " <-------
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # usei o len como inicio para contar os caracteris.
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digita não é um palíndromo')
