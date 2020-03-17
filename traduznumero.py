cont = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
'Dezessete', 'Dezoito', 'Dezenove', 'Vinte', 'Vinte e um', 'Vinte e dois',
'Vinte e três', 'Vinte e quatro', 'Vinte e cinco', 'Vinte e seis', 'Vinte e sete', 'Vinte e oito',
'Vinte e nove', 'Trinta', 'Trinta e um', 'Trinta e dois', 'Trinta e três', 'Trinta e quatro',
'Trinta e cinco', 'Trinta e seis', 'Trinta e sete', 'Trinta e oito', 'Trinta e nove', 'Quarenta',
'Quarenta e um', 'QUARENTA E DOIS :)')

while True:
    num = int(input('digite um número entre 0 e 42: '))
    if 0<= num <= 42:
        break
    print('tente novamente.', end='')
print(f'Você digitou o número {cont[num]}')