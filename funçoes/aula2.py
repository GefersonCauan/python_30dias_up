# Simulador de Produção de Fábrica
# Cada máquina produz X unidades por hora.
# Cada máquina tem custo de energia diferente.
# Funções:
# produzir(qtd_maquinas, horas)
# calcular_custo(qtd_maquinas, horas)
# relatorio_producao() → mostra total produzido, custo total e eficiência.
# ⚙️ Envolve cálculos, loops e decisões condicionais encadeadas.

def produzir(qtd_maquinas, horas, producao_por_maquina):
    total_produzido = qtd_maquinas * horas * producao_por_maquina
    return total_produzido

def calcular_custo(qtd_maquinas, horas, custo_por_maquina):
    custo_total = qtd_maquinas * horas * custo_por_maquina
    return custo_total

def relatorio_producao(qtd_maquinas, horas, producao_por_maquina, custo_por_maquina):
    total_produzido = produzir(qtd_maquinas, horas, producao_por_maquina)
    custo_total = calcular_custo(qtd_maquinas, horas, custo_por_maquina)

    eficiencia = total_produzido / custo_total if custo_total > 0 else 0

    print("Relatório de Produção:")
    print(f"Total Produzido: {total_produzido} unidades")
    print(f"Custo Total: R$ {custo_total:.2f}")
    print(f"Eficiência: {eficiencia:.2f} unidades por R$")

# Exemplo de uso
qtd_maquinas = 20
horas = 9
producao_por_maquina = 15
custo_por_maquina = 10

relatorio_producao(qtd_maquinas, horas, producao_por_maquina, custo_por_maquina)

