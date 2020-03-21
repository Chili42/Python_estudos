cont = 0
for c in range(6):
    numero = int(input('Digite 6 números  '))
    if numero % 2 == 0:
        cont = numero + cont
print('a soma dos numeros pares é {}'.format(cont))