"""
lista.append('meu item') #ele coloca mais um item na sua lista
lista.insert(0 = posição,'meu item') #ele adiciona um item em qualquer posição da lista
del lista[3] # del deleta pelo index da lista
lista.pop(3) # pop deleta pelo index da lista
lista.pop() # pop sem numero ele elimina o ultimo index da lista
lista.remove('nome do meu item na lista') #remove delete pela string da lista
valores.sort() # ele coloca sua lista em ordem
valores.sort(reverse=True) # ele coloca sua lista em ordem decrescente
"""
"""
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
# num.pop()
if 5 in num:
    num.remove(5)
else:
    print('Não Encontramos o número 5!')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
"""

"""
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
"""

"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
"""

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
