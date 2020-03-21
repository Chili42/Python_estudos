nome = str(input('qual é o seu nome ? '))
if nome == 'Rafael':
    print('que nome bonito!')
elif nome == 'Pedro' or nome =='Maria' or nome == 'Zé' or nome == 'João' or nome == 'Paulo':
    print('nome comum da porra, heim ?')
elif nome in 'Patricia Aline Claudia Angela Isabela':
    print('que nome lindo')
else:
    print('seu nome é de boas! ')
print ('tenha um bom dia {}'. format(nome))