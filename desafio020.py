import random
um = str(input('primeiro aluno:' ))
dois = str(input('segundo aluno: '))
tres = str(input('terceiro aluno: '))
quatro = str(input('quatro aluno: '))
lista = [um , dois, tres, quatro]
resultado = random.shuffle(lista)
print(f'A ordem de apresentação será \n {lista}')
