import random


'''

    Verifica se um determinado número 'n' é primo

    PARAMS

    - n: int

'''
def is_prime(n):
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


'''

    Gera um número primo utilizando is_prime() para efetuar a verificação    

'''
def generate_prime_number():
    prime = False
    while not prime:
        p = random.randint(100, 1000)
        if is_prime(p):
            prime = True
    return p

'''

    Retorna o mínimo divisor comum entre dois números 'a' e 'b'

    PARAMS

    - a: int
    - b: int

'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''

    Retorna o multiplicativo inverso de 'e' e 'phi'

    PARAMS

    - e: int
    - phi: int

'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


'''

    Gera um par de chaves (pública e privada)

'''
def generate_key_pair():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((n, e), (n, d))

'''

    Encripta e retorna um texto utilizando a chave pública 

'''
def encrypt(public_key, plaintext):
    n, e = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext


'''

    Decripta e retorna um texto utilizando a chave privada 

'''
def decrypt(private_key, ciphertext):
    n, d = private_key
    plaintext = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plaintext)


'''

    EXECUÇÃO

'''
public_key, private_key = generate_key_pair()
plaintext = input("Digite a mensagem a ser criptografada: ")
ciphertext = encrypt(public_key, plaintext)
print(ciphertext)
plaintext = decrypt(private_key, ciphertext)
print(plaintext)
