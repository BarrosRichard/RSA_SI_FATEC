import random
import os

def is_prime(n) -> bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def generate_key_pair(p, q) -> tuple:
    n = p * q
    z = (p - 1) * (q - 1)

    e = random.randint(1, z)
    g = gcd(e, z)
    while g != 1:
        e = random.randint(1, z)
        g = gcd(e, z)

    d = pow(e, -1, z)

    return ((n, e), (n, d))

def encrypt(public_key, plaintext) -> list[int]:
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext) -> str:
    n, d = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

def main() -> None:

    TITLE = '''
    ###########################################################
    ################# RSA ENCRYPTOR/DECRYPTOR #################
    ###########################################################
    (Use: CTRL + C para [SAIR])
    '''

    print(
        TITLE,
        sep='\n'
    )

    P = int(input("P: "))
    Q = int(input("Q: "))
    
    while not is_prime(P) or not is_prime(Q):
        os.system('clear')
        print(
            TITLE,
            sep='\n'
        )
        print("\nErro.: P e Q devem ser primos...")
        P = int(input("P: "))
        Q = int(input("Q: "))

    plaintext = input('\nDigite uma mensagem: ')

    print('Gerando par de chaves...')
    public_key, private_key = generate_key_pair(P, Q)
    print('Encriptando... Chave publica: {}'.format(public_key))
    ciphertext = encrypt(public_key, plaintext)
    print('Decriptando... Chave privada: {}'.format(private_key))
    plaintext = decrypt(private_key, ciphertext)

    print('\nMENSAGEM ENCRIPTADA.: {}'.format(ciphertext))
    print('MENSAGEM DECRIPTADA.: {}'.format(plaintext))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[SAIR]')