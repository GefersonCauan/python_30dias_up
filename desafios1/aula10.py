# Sistema de Investimentos
# Pede:
# tipo de investimento (“poupança”, “CDB”, “açoes”, “cripto”)
# valor investido
# tempo em meses
# Regras:
# poupança → rendimento 0.5% ao mês
# CDB → 1.2% ao mês
# ações → 3% ao mês
# cripto → rendimento aleatório entre -5% e +8%
# Lógica:
# calcula o valor final com base no tipo
# mostra se teve lucro, prejuízo ou estabilidade
# 👉 Treina: simulação real + matemática + lógica condicional de múltiplos tipos

import random
tipo_investimento = input(" qual investimento voçe deseja (poupança, CDB, ações, cripto): ").lower()
valor = int(input("Quanto deseja investir: "))
meses = int(input("quanto meses: "))

if tipo_investimento == "poupança":
    rendimento = 0.05
elif tipo_investimento == "CDB":
    rendimento =1.2
elif tipo_investimento == "acoes":
    rendimento = 3
elif tipo_investimento == "cripto":
    rendimento = -5 or +8
    rendimento = random.uniform(-5, 8) / 100
else:
    print("tipo de investimento invalido")
    rendimento = 0
valor_final = valor * (1 + rendimento) ** meses
print(f"valor final do investimento: {valor_final:.2f}")
if valor_final > valor:
    print("voçe teve lucro")
elif valor_final < valor:
    print("voçe teve prejuizo")
else:
    print("voçe ficou estavel")
    