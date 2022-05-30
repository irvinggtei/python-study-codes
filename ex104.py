def a_number(num):
    while True:
        print('-' * 30)
        an = str(input(num))
        if an.isnumeric():
            an = int(an)
            break
        else:
            print('Is not a number, please type a real number')
    return an


n = a_number('Insert a number: ')
print(f'You just inserted the number {n}')