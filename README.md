# RSA - Segurança da Informação
Implementa um algoritmo de criptografia RSA que pode ser utilizado para criptografar e descriptografar mensagens.

## Explicação das funções

 ### **1. is_prime:**
 É usada para determinar se um número inteiro é um número primo ou não. Em outras palavras, a função retorna "True" se o número passado como argumento for primo e "False" caso contrário.
Primeiro, a função verifica se o número é menor ou igual a 1. Se for, a função retorna "False", porque os números primos são sempre maiores do que 1.
Em seguida, a função verifica se o número é menor ou igual a 3. Se for, a função retorna "True", porque os números 2 e 3 são primos.
Se o número não for menor ou igual a 3, a função verifica se ele é divisível por 2 ou 3. Se for, a função retorna "False", porque os números primos não são divisíveis por nenhum número além de 1 e eles próprios.
Se o número não for divisível por 2 ou 3, a função entra em um loop "while". O loop começa com a variável "i" sendo definida como 5.
Dentro do loop, a função verifica se o número é divisível por "i" ou "i+2". Se for, a função retorna "False", porque o número não é primo.
Depois disso, a função adiciona 6 à variável "i" e continua verificando até que "i*i" seja maior que o número passado como argumento. Essa verificação é feita porque, se um número é divisível por um número maior do que a sua raiz quadrada, então ele também deve ser divisível por um número menor do que a sua raiz quadrada. Portanto, não é necessário verificar se um número é divisível por todos os números até o próprio número.
Finalmente, se o número passado como argumento passar por todos esses testes, a função retorna "True", indicando que o número é primo.
Em resumo, essa função usa uma série de verificações para determinar se um número é primo ou não. Ele verifica se o número é menor ou igual a 1, se é menor ou igual a 3, se é divisível por 2 ou 3 e, finalmente, verifica se é divisível por qualquer número de 5 em diante, até que a raiz quadrada do número seja atingida.

 ### **2.  generate_prime_number:**
É usada para gerar um número primo aleatório no intervalo entre 100 e 1000 (inclusive). Em outras palavras, a função retorna um número inteiro que é primo e está entre 100 e 1000.
Primeiro, a função define uma variável booleana chamada "prime" como "False". Essa variável é usada para controlar o loop "while" que vem em seguida.
Dentro do loop "while", a função gera um número aleatório "p" usando a função "randint" do módulo "random". O número gerado deve estar entre 100 e 1000, inclusive.
A função, em seguida, chama outra função chamada "is_prime" para verificar se o número gerado é primo ou não. Se o número for primo, a variável "prime" é definida como "True" e o loop "while" é interrompido.
Finalmente, a função retorna o número primo gerado.
Em resumo, essa função gera um número primo aleatório no intervalo entre 100 e 1000 (inclusive) usando um loop "while" e a função "is_prime".

### **3.  gcd:**
É usada para encontrar o máximo divisor comum entre dois números inteiros positivos "a" e "b". Em outras palavras, a função retorna o maior número inteiro que divide ambos "a" e "b".
A função usa um loop "while" que continua enquanto "b" for diferente de zero. Dentro do loop, a função atualiza o valor de "a" para ser igual a "b" e atualiza o valor de "b" para ser o resto da divisão de "a" por "b". Isso é feito usando uma atribuição múltipla, onde "a" recebe o valor atual de "b" e "b" recebe o valor atual de "a % b".
O loop "while" continua até que "b" seja zero. Nesse ponto, a função retorna o valor atual de "a", que é o máximo divisor comum entre "a" e "b".
Em resumo, essa função usa o algoritmo de Euclides para encontrar o máximo divisor comum entre dois números inteiros positivos "a" e "b". O algoritmo repete o processo de divisão sucessivamente até que o resto da divisão seja igual a zero, indicando que o último divisor usado é o máximo divisor comum entre os dois números.

**O que é algoritmo de Euclides?**
O algoritmo de Euclides é um algoritmo utilizado para encontrar o máximo divisor comum (MDC) entre dois números inteiros positivos "a" e "b". Ele é nomeado em homenagem a Euclides, um matemático grego que descreveu o algoritmo em sua obra "Os Elementos".
A ideia básica do algoritmo é usar a propriedade de que o máximo divisor comum de dois números é o mesmo que o máximo divisor comum do menor número e o resto da divisão do maior número pelo menor número. Em outras palavras, se "a" e "b" são dois números inteiros positivos, e "a" é maior que "b", então o máximo divisor comum entre "a" e "b" é igual ao máximo divisor comum entre "b" e "a % b".
O algoritmo de Euclides é implementado usando um loop que continua enquanto o segundo número ("b") não é zero. Em cada iteração do loop, o valor de "a" é atualizado para ser igual a "b" e o valor de "b" é atualizado para ser o resto da divisão de "a" por "b". Esse processo é repetido até que "b" seja zero. Nesse ponto, o valor atual de "a" é o máximo divisor comum entre os dois números originais.
O algoritmo de Euclides é um dos algoritmos mais simples e eficientes para encontrar o máximo divisor comum entre dois números inteiros positivos. Ele tem muitas aplicações em matemática e ciência da computação, incluindo criptografia, teoria dos números e algoritmos de busca de caminho mais curto em grafos.

### **4.  multiplicative_inverse:**
É usada para encontrar o inverso multiplicativo de um número inteiro "e" módulo um segundo número inteiro "z". O inverso multiplicativo de "e" módulo "z" é outro número inteiro "d" tal que (e * d) % z = 1.
A função inicializa várias variáveis, incluindo "d", "x1", "x2" e "y1". Em seguida, a função inicia um loop "while" que continua enquanto "e" é maior que zero.
Dentro do loop, a função usa o algoritmo estendido de Euclides para calcular o máximo divisor comum entre "e" e "z", bem como os coeficientes de Bezout "x" e "y", que satisfazem a equação "ex + zy = gcd(e, z)". Em outras palavras, a função encontra um par de inteiros "x" e "y" tal que (e * x) + (z * y) = gcd(e, z).
O loop atualiza várias variáveis, incluindo "x1", "x2", "y1" e "d", antes de verificar se o máximo divisor comum entre "e" e "z" é igual a 1. Se for o caso, a função retorna o valor atual de "d" mais "z". Isso é necessário porque o valor atual de "d" pode ser negativo, e adicionar "z" a "d" garante que o resultado seja positivo.
Em resumo, a função "multiplicative_inverse" usa o algoritmo estendido de Euclides para encontrar o inverso multiplicativo de "e" módulo "z". O algoritmo encontra um par de inteiros "x" e "y" que satisfazem a equação "ex + zy = gcd(e, z)", e o valor de "d" é o coeficiente "y" da equação. Se o máximo divisor comum entre "e" e "z" for igual a 1, a função retorna o valor de "d" mais "z".

### **5.  generate_key_pair:**
É usada para gerar um par de chaves criptográficas para um algoritmo de criptografia  RSA.
A função começa gerando dois números primos aleatórios "p" e "q" usando a função "generate_prime_number". Em seguida, ela calcula o produto desses dois números para obter "n" e o valor "z" da função Euler totient (ou função totiente de Euler), que é igual a (p-1)*(q-1).
Em seguida, a função seleciona aleatoriamente um número "e" que é menor que "z" e calcula o máximo divisor comum entre "e" e "z" usando a função "gcd". Se o resultado não for igual a 1, a função seleciona outro número aleatório "e" e tenta novamente até que o resultado do máximo divisor comum seja igual a 1.
Depois que a função encontrar um valor adequado para "e", ela calcula o inverso multiplicativo de "e" módulo "z" usando a função "multiplicative_inverse" e atribui o resultado a "d". Esses valores "e" e "d" são os exponentes de criptografia e descriptografia, respectivamente.
Por fim, a função retorna um par de chaves criptográficas, onde a chave pública é (n, e) e a chave privada é (n, d).
Em resumo, a função "generate_key_pair" usa a geração de números primos aleatórios e o cálculo da função totiente de Euler para gerar um par de chaves criptográficas para um algoritmo de criptografia assimétrica. A chave pública é composta pelo produto "n" dos dois números primos e o expoente "e", enquanto a chave privada é composta por "n" e o expoente "d".

### **6.  encrypt:**
É usada para criptografar uma mensagem de texto usando uma chave pública em um algoritmo de criptografia RSA.
A função recebe como entrada a chave pública "public_key" que é composta pelo produto "n" dos dois números primos e o expoente "e", e a mensagem de texto "plaintext" que será criptografada.
A função extrai os valores de "n" e "e" da chave pública e, em seguida, itera por cada caractere na mensagem de texto "plaintext". Para cada caractere, a função primeiro converte o caractere em seu valor numérico ASCII correspondente usando a função "ord". Em seguida, a função eleva esse valor numérico à potência "e" e calcula o resultado módulo "n" usando o operador "%". Esse valor é adicionado à lista "ciphertext".
Depois que todos os caracteres na mensagem de texto forem criptografados, a função retorna a lista "ciphertext" que contém a mensagem criptografada.
Em resumo, a função "encrypt" usa a chave pública "public_key" para criptografar uma mensagem de texto "plaintext" usando um algoritmo de criptografia assimétrica. A mensagem criptografada é retornada como uma lista de valores inteiros.

### **7.  decrypt:**
É usada para descriptografar uma mensagem de texto criptografada usando uma chave privada em um algoritmo de criptografia RSA.
A função recebe como entrada a chave privada "private_key" que é composta pelo produto "n" dos dois números primos e o expoente "d", e a mensagem criptografada "ciphertext" que será descriptografada.
A função extrai os valores de "n" e "d" da chave privada e, em seguida, itera por cada valor inteiro na lista "ciphertext". Para cada valor inteiro, a função primeiro eleva o valor à potência "d" e calcula o resultado módulo "n" usando o operador "%". Em seguida, a função converte o valor numérico resultante em seu caractere correspondente usando a função "chr". Esse caractere é adicionado à lista "plaintext".
Depois que todos os valores inteiros na mensagem criptografada forem descriptografados, a função retorna a lista "plaintext" como uma única string concatenando todos os caracteres.
Em resumo, a função "decrypt" usa a chave privada "private_key" para descriptografar uma mensagem de texto criptografada "ciphertext" usando um algoritmo de criptografia assimétrica. A mensagem original é retornada como uma string.
