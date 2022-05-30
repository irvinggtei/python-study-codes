def voto(a):
    from datetime import date
    hoje = date.today().year - a

    print(f'Com {hoje} anos: ', end='')
    if hoje >= 18 and hoje <= 65:
        print('Voto OBRIGATÓRIO.')
    if hoje >= 16 and hoje < 18:
        print('Voto OPCIONAL.')
    if hoje > 65:
        print('Voto OPCIONAL.')
    if hoje < 16:
        print('NÃO pode votar.')


print('-' * 30)
ano = int(input('Ano de nascimento (AAAA): '))
voto(ano)