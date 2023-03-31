from bcrypt import hashpw, gensalt

def criptografar(senha):
    bytes = senha.encode('utf-8')
    vetor_binario = ''.join(f'{caractere:b}' for caractere in bytes).encode('utf-8')
    resultado = hashpw(vetor_binario, gensalt(13))
    return resultado

def main():
    senha = input('Digite sua senha: ')
    hash = criptografar(senha)
    print(f'A senha criptografada é: {hash}')

if __name__ == '__main__':
    main()
