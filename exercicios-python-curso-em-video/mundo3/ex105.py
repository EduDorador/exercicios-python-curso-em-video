def notas(*num, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicado se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r["total"] = len(num)
    r["maior"] = max(num)
    r["menor"] = min(num)
    r["media"] = sum(num) / len(num)
    if sit:
        if r["media"] >= 7:
            r["situação"] = 'BOA'
        elif r["media"] >= 5:
            r["situação"] = 'RAZOÁVEL'
        else:
            r["situação"] = 'RUIM'
    return r


#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
