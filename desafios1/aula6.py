# istema de Empréstimos
# Pede renda mensal
# Pede valor do empréstimo desejado
# Regras:
# Se empréstimo ≤ 10% da renda → “Aprovado”
# Entre 10%–50% → “Aprovado com análise”
# 50% → “Negado”
# 👉 foco: decisões matemáticas + múltiplas faixas + else final

def sistema_emprestimos(renda_mensal, valor_emprestimo):
    if valor_emprestimo <= 0.1 * renda_mensal:
        return "Aprovado"
    elif 0.1 * renda_mensal < valor_emprestimo <= 0.5 * renda_mensal:
        return "Aprovado com analise"
    else:
        return "Negado"
    
if __name__ == "__main__":
    renda = float(input("Digite sua renda mensal: R$: "))
    valor = float(input("Digite o valor do emprestimo desejado: R$"))
    resultado = sistema_emprestimos(renda, valor)
    print(f"resultado: {resultado}")
