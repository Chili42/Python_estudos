numero = int(input('qual número deseja ? '))

for c in range(0, 11):
    result = numero * c
    print('{} x {} = {}'.format(numero, c, result))