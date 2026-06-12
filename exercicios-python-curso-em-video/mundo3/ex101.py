def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos de idade: O VOTO é NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos de idade: O VOTO é OPCIONAL!'
    else:
        return f'Com {idade} anos de idade: O VOTO é OBRIGATÓRIO!'


#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
