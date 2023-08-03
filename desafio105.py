def notas(sit=False):
    """
    -> Função para analisar a situação de notas da turma.
    :nt[]: Lista que receberá a nota de cada aluno
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Divionário com várias informações sobre a situação da turma
    """
    nt = []
    while True:
        nota = float(input('Digite a nota do aluno: '))
        nt.append(nota)
        esc = str(input('Deseja adicionar mais notas? [S/N]')).strip().lower()
        if esc == 'n':
            break

    media = sum(nt) / len(nt)
    turma = {
        'total': len(nt),
        'maior': max(nt),
        'menor': min(nt),
        'média': media
    }
    if sit:
        if media < 4:
            turma['situação'] = 'Ruim'
        elif 4 <= media <= 7:
            turma['situação'] = 'Razoável'
        elif 7 <= media <= 9:
            turma['situação'] = 'Boa'
        elif media > 9:
            turma['situação'] = 'Excelente'
    return turma

# Programa Principal
resp = notas(sit=True)
print(resp)
