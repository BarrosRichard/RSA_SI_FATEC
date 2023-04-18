import random

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

def generate_prime_number() -> int:
    prime = False
    while not prime:
        p = random.randint(100, 1000)
        if is_prime(p):
            prime = True
    return p

def gcd(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, z) -> int:
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_z = z

    while e > 0:
        temp1 = temp_z // e
        temp2 = temp_z - temp1 * e
        temp_z = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_z == 1:
        return d + z

def generate_key_pair() -> tuple:
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    z = (p - 1) * (q - 1)

    e = random.randint(1, z)
    g = gcd(e, z)
    while g != 1:
        e = random.randint(1, z)
        g = gcd(e, z)

    d = multiplicative_inverse(e, z)

    return ((n, e), (n, d))

def encrypt(public_key, plaintext) -> list[int]:
    n, e = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext) -> str:
    n, d = private_key
    plaintext = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plaintext)

def main() -> None:
    print(
        '###########################################################',
        '################# RSA ENCRYPTOR/DECRYPTOR #################',
        '###########################################################',
        '(Use: CTRL + C para [SAIR])',
        sep='\n'
    )

    plaintext = input('\nDigite uma mensagem: ')

    print('Gerando par de chaves...')
    public_key, private_key = generate_key_pair()
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