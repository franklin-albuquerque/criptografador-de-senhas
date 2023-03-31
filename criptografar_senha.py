from bcrypt import hashpw, gensalt

senha = input('Digite sua senha: ')
bytes = senha.encode('utf-8')
vetor_binario = ''.join(f'{caractere:b}' for caractere in bytes).encode('utf8')

print('Criptografando...')

hash = hashpw(vetor_binario, gensalt(13))
print(f'A senha criptografada é: {hash}')
