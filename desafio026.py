frase = str(input('Digite uma Frase: ')) .strip() .upper()
um = frase.count('A')
dois = frase.find('A')+1
tres = frase.rfind('A')+1
print(f'A letra A aparece {um} vezes na frase.')
print(f'A primeira letra A apareceu na posição {dois}')
print(f'A última letra A apareceu na posição {tres}')
