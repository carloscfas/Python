def aumentar(preço=0, taxa=0, formato=False):
    """
    --> Calcula o aumento de um determinado preço,
    retornando o resultado como ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    resp = preço + (preço * taxa/100)
    return resp if formato is False else moeda(resp)


def diminuir(preço=0, taxa=0, formato=False):
    resp = preço - (preço * taxa/100)
    return resp if formato is False else moeda(resp)


def dobro(preço=0, formato=False):
    resp = preço + preço
    return resp if not formato else moeda(resp)


def metade(preço=0, formato=False):
    resp = preço / 2
    return resp if not formato else moeda(resp)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisando: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxaa}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
