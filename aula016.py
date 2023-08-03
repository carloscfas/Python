""" lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #uma TUPLA
# Tuplas são imutáveis
print(sorted(lanche)) #sorted coloca em ordem """

"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) #o index mostra qual posição está o meu 8 na Tupla
#print(c.count(5)) # o Count vai contar quantos 5 tem dentro da Tupla
#print(len(c)) #o Len vai contar quantos elementos tem dentro da Tupla """


""" for comida in lanche: #maneira mais simples
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)): #maneira utilizando o Range
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):# Maneira utilizando o Enumerate e utilizando 2 variáveis no for
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!') """

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # o del apaga minha Tupla pessoa da memória
print(pessoa)

