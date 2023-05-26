import random
import string



def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo(a) ao Gerador de Senhas Aleatórias!")
    comprimento = int(input("Digite o comprimento desejado para a senha: "))
    senha = gerar_senha(comprimento)
    print("Senha gerada:", senha)

if __name__ == '__main__':
    main()
