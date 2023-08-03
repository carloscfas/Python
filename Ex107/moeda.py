def aumentar(preço, taxa):
    resp = preço + (preço * taxa/100)
    return resp


def diminuir(preço, taxa):
    resp = preço - (preço * taxa/100)
    return resp


def dobro(preço):
    resp = preço + preço
    return resp


def metade(preço):
    resp = preço / 2
    return resp
