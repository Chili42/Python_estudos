result = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        result = result + c
print('A soma dos {} números divisiveis por 3 - entre 0 e 500 é: {}'.format(cont, result))
