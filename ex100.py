from random import randint
lista = list()


def sortear():
    print('Sorteando 5 valores da lista:', end=' ')
    for r in range(0, 5):
        lista.append((randint(1, 9)))
    for n in lista:
        print(f'{n}', end=' ')
    print('PRONTO!')


def somapar():
    sp = 0
    for n in lista:
        if n % 2 == 0:
            sp += n
    print('Somando os valores pares de:', end=' ')
    for n in lista:
        print(f'{n}', end=' ')
    print(f'\nO resultado da soma foi de {sp}')


sortear()
somapar()
