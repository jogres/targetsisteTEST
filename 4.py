#4) Descubra a lógica e complete o próximo elemento:

#a) 1, 3, 5, 7, ___
# A sequência é uma progressão aritmética com diferença de 2.
proximo_elemento = 7 + 2
print(proximo_elemento)

#b) 2, 4, 8, 16, 32, 64, ____
# A sequência é uma progressão geométrica com razão 2.
proximo_elemento = 64 * 2
print(proximo_elemento)

#c) 0, 1, 4, 9, 16, 25, 36, ____
# A sequência é a série dos quadrados dos números naturais.
proximo_elemento = 7 * 7
print(proximo_elemento)

#d) 4, 16, 36, 64, ____
# A sequência é dos quadrados dos números pares.
proximo_elemento = (2 * 5) * (2 * 5)
print(proximo_elemento)

#e) 1, 1, 2, 3, 5, 8, ____
# A sequência é a sequência de Fibonacci.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

proximo_elemento = fibonacci(7)
print(proximo_elemento)

#f) 2,10, 12, 16, 17, 18, 19, ____
# A sequência parece ser números consecutivos após uma mudança.
proximo_elemento = 19 + 1
print(proximo_elemento)
