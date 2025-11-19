# Você recebe uma string em maiúsculas (exemplo: "BANANA").
# Dois jogadores vão formar substrings dessa string:
# Kevin: só palavras que começam com vogal (A, E, I, O, U).
# Stuart: só palavras que começam com consoante.
# Cada substring vale pontos = quantas vezes ela aparece dentro da string original.
# Exemplo: "ANA" aparece 2 vezes em "BANANA", então vale 2 pontos.
# No final, você precisa calcular a pontuação dos dois e imprimir quem ganhou e a pontuação.
# Se Stuart ganhar: "Stuart 12".
# Se Kevin ganhar: "Kevin 15".
# Se empatar: "Draw".
# 👉 O truque pra resolver rápido:
# Em vez de gerar todas as substrings (muito pesado), você pode calcular os pontos assim:
# Para cada posição i na string, o número de substrings possíveis começando em i é len(string) - i.
# Então, se a letra em i é vogal → ponto pra Kevin.
#  Se é consoante → ponto pra Stuart

def minion_game(string):
    vogais = 'AEIOU'
    pontos_kevin = 0
    pontos_stuart = 0
    tamanho = len(string)
    
    # Conta pontos
    for i in range(tamanho):
        if string[i] in vogais:
            pontos_kevin += tamanho - i
        else:
            pontos_stuart += tamanho - i

    # Decide vencedor
    if pontos_kevin > pontos_stuart:
        print('Kevin', pontos_kevin)
    elif pontos_stuart > pontos_kevin:
        print('Stuart', pontos_stuart)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
