
# alunos = [
#     {'nome': 'ana', 'nota': 9},
#     {'nome': 'victor', 'nota': 6},
#     {'nome': 'joao', 'nota': 7},
#     {'nome': 'cauan', 'nota': 9.5}
# ]

# notas = [aluno['nota'] for aluno in alunos]
# media = sum(notas) / len(notas)
# print(f"Média da turma: {media:.2f}")

# vendas = [
#   {'produto': 'caneta', 'valor': 3.5},
#   {'produto': 'caderno', 'valor': 15},
#   {'produto': 'caneta', 'valor': 3.5},
#   {'produto': 'mochila', 'valor': 80}
# ]
# # calcular o produto mais vendido (mais vezes na lista)
# from collections import Counter
# produtos = [venda['produto'] for venda in vendas]
# contador = Counter(produtos)
# mais_vendido = contador.most_common(1)[0]
# print(f"Produto mais vendido: {mais_vendido[0]} (vendas: {mais_vendido[1]})")

# from sklearn.tree import DecisionTreeClassifier

# # Dados de treino
# X = [[5], [7], [9], [3]]  # notas
# y = ['Reprovado', 'Aprovado', 'Aprovado', 'Reprovado']

# modelo = DecisionTreeClassifier()
# modelo.fit(X, y)

# # Teste
# print(modelo.predict([[6]]))  # → ['Aprovado'] ou ['Reprovado'] dependendo da árvore
