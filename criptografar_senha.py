from bcrypt import hashpw, gensalt

def criptografar(senha):
    vetor_binario = ''.join(map(bin, bytearray(senha, 'utf-8')))
    resultado = hashpw(vetor_binario.encode('utf8'), gensalt(13))
    return resultado.decode('utf-8')

def main():
    senha = input('Digite a senha que deseja criptografar: ')
    resultado = criptografar(senha)
    print(f'Sua senha foi criptografada como: {resultado}')

if __name__ == '__main__':
    main()
