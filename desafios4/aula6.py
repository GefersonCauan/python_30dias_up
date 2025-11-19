# def mover_robo(comandos):
#     pos = [0, 0]
#     movimentos = {'N': (0, 1), 'S': (0, -1), 'L': (1, 0), 'O': (-1, 0)}
#     for c in comandos:
#         dx, dy = movimentos[c]
#         pos[0] += dx
#         pos[1] += dy
#     return tuple(pos)

# # Exemplo de uso
# comandos = "NNSLOO"
# posicao_final = mover_robo(comandos)
# print(f"A posição final do robô é: {posicao_final}")
# # Desafio: Movimento de um Robô em um Plano 2D
# # Escreva uma função que receba uma string de comandos representando movimentos de um robô em um plano 2D. Cada comando pode ser 'N' (norte), 'S' (sul), 'L' (leste) ou 'O' (oeste). A função deve retornar a posição final do robô após executar todos os comandos, começando na posição (0, 0).
# # Exemplo: Para a entrada "NNSLOO", a saída deve ser (0, 1).
# # Dica: Utilize coordenadas cartesianas para representar a posição do robô e atualize-as conforme os comandos são processados.sssss


from collections import Counter  # ferramenta para contar

palavra = input("Digite uma palavra: ")  # recebe a palavra do usuário

contagem = Counter(palavra)  # conta quantas vezes cada letra aparece

print(contagem)  # mostra o resultado
