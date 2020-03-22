sexo = str(input('informe seu sexo ?: [M/F]  ' )).strip().upper()[0]
while sexo not in 'MmFf':
   sexo = str(input('É M ou F...porra! ')).strip().upper()[0]
print('valew!')
