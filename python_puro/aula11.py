# “Caixa Eletrônico Simplificado” 🏦
# 🧩 Situação:
# Você está criando o sistema de um caixa eletrônico.
# 🎯 Regras:
# O usuário digita o valor a sacar.
# O caixa deve mostrar quantas notas de R$100, R$50, R$20 e R$10 serão entregues.
# Sempre usar as notas maiores primeiro.
# Exemplo:
# Valor: 280
# Resultado:
# 2 notas de 100
# 1 nota de 50
# 1 nota de 20
# 1 nota de 10
# 🧠 Treino lógico:
# Como “tirar” as notas do valor total?
# Dica: usa divisão inteira (//) e resto (%).

valor = int(input("Digite o valor a sacar: R$ "))

notas_v100 = valor // 100
valor = valor % 100

notas_v50 = valor // 50
valor = valor % 50

notas_v20 = valor // 20
valor = valor % 20

notas_v10 = valor // 10
valor = valor % 10

print(f"notas de R$100: {notas_v100}")

print(f"notas de R$50: {notas_v50}")

print(f"notas de R$20: {notas_v20}")

print(f"notas de R$10: {notas_v10}")
if valor != 0:
    print(f"Valor restante que não pode ser sacado: R$ {valor}")
# Obs: esse código não trata valores inválidos (ex: 125