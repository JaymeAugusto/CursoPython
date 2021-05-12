nome = input('Qual é seu nome?')
if nome == 'jayme':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no Brasil!')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}'.format(nome))