#def contador(i, f, p):
#    """
#    -> Faz uma contagem e mostra na tela.
#    :param i: início da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    """
#    c = i
#    while c <= f:
#        print(f'{c} ', end='')
#        c += p
#    print('FIM!')
#
#
#help(contador)


#def somar(a=0, b=0, c=0):
#    """
#
#    :param a: o primeiro valor
#    :param b: o segundo valor
#    :param c: o terceiro valor
#    :return:
#    """
#    s = a + b + c
#    print(f'A soma vale {s}')
#
#
#
#somar(3, 2, 5)


""" def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}') """


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 4)
r3 = somar(2)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
