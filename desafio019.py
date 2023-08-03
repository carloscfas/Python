from random import choice
um = str(input('Primeiro aluno: '))
dois = str(input('Segundo aluno: '))
tres = str(input('Terceiro aluno: '))
quatro = str(input('Quarto aluno: '))
lista = [um, dois, tres, quatro]
resultado = choice(lista)
print(f'O aluno escolhido foi {resultado}')
