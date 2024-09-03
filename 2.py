#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def contar_letra_a(s):
    return s.lower().count('a')

# Teste
string = input("Digite uma string para verificar a ocorrência da letra 'a': ")
quantidade = contar_letra_a(string)
print(f"A letra 'a' ocorre {quantidade} vezes na string.")
