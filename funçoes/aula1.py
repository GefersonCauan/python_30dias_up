# Analisador de Palavras
# Funções:
# contar_vogais(palavra)
# contar_consoantes(palavra)
# eh_palindromo(palavra) → retorna True se for igual ao inverso.
# analisar_palavra() → junta tudo e mostra relatório.
# ⚙️ Treina loops, len(), for, e manipulação de strings.

def contar_vogais(palavras):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavras:
        if letra in vogais:
            contador = contador + 1
    return contador

def contar_consoantes(palavras):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for letra in palavras:
        if letra in consoantes:
            contador =  contador + 1
    return contador

def eh_palindromo(palavras):
    palavra_invertida = ""
    for letra in palavras:
        palavra_invertida = letra + palavra_invertida
        if palavra_invertida == palavras:
            return True
    return False

def analisar_palavra():
    palavras = input("Digite uma palavra: ")
    num_vogais = contar_vogais(palavras)
    num_consoantes = contar_consoantes(palavras)
    poliodromo = eh_palindromo(palavras)

    print(f"Analise da palavra: '{palavras}'")
    print(f"Numero de voagais: {num_vogais}")
    print(f"Numero de consoantes: {num_consoantes}")

    if poliodromo:
        print("A palavra é um polindromo.")
    else:
        print("A palavra não é um pólindromo.")

analisar_palavra()
    