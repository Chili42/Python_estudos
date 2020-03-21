valor = float(input('Qual o valor da casa que deseja ? '))
salario = float(input('Quanto tu ganha ? '))
tempo = float(input('prente pagar em quantos anos ? '))

anos = tempo * 12
prestação = valor / anos

if prestação > salario:
    print('sem chance, nego véio!')
else:
    print('bora fazer negócio ? ')
