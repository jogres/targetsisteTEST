#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def is_fibonacci(n):
    if n < 0:
        return False
    
    # Função para verificar se um número é um quadrado perfeito
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x

    # Um número é Fibonacci se e somente se 5*n^2 + 4 ou 5*n^2 - 4 é um quadrado perfeito
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Teste
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
