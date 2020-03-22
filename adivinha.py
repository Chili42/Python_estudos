from time import sleep

print('-=-' * 10)
print('       Jogo do Chili')
print('-=-' * 10)
print('\n')
from random import randint
cont = 1
computador = randint(0, 10)
jogador = int(input('entre 0 e 10 - qual número acha que eu pensei ? '))
print('PROCESSANDO...')
sleep(1)
while jogador != computador:
    jogador = int(input('tenta de novo, mano! '))
    print('PROCESSANDO...')
    sleep(1)
    cont = cont + 1
print('você acertou em {} tentativas... o número é {}'.format(cont, computador))
    
