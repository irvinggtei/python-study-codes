def sheet(n='', g=0):
    if n == '':
        n = '<ANON>'
    print(f'The player {n}', end='')
    if g > 1:
        print(f' scored {g} goals.')
    elif g == 1:
        print(f' scored {g} goal.')
    else:
        print(' didnt scored.')


name = str(input('Type the player name: '))
goals = str(input(f'{name} score: '))
if goals.isnumeric():
    goals = int(goals)
sheet(name, goals)