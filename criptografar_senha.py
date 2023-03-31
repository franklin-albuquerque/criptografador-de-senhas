from bcrypt import hashpw, gensalt

senha = input('Digite sua senha: ')
bytes = senha.encode('utf-8')

print('Criptografando...')

hash = hashpw(bytes, gensalt(13))
print(f'A senha criptografada é: {hash}')
