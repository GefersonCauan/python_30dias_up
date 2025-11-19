import pandas as pd
import matplotlib.pyplot as plt
import os

# Lista com os nomes dos arquivos semanais
arquivos = ["vendas_semana1.csv", "vendas_semana2.csv", "vendas_semana3.csv", "vendas_semana4.csv"]

# Lista vazia para armazenar os DataFrames
todas_as_semanas = []

# Loop para ler cada arquivo e adicionar na lista
for arquivo in arquivos:
    df = pd.read_csv(arquivo)
    todas_as_semanas.append(df)

# Concatena todos os DataFrames
df_total = pd.concat(todas_as_semanas, ignore_index=True)

df_total["total"] = df_total["preco"] * df_total["quantidade"]

vendas_mensais = df_total.groupby("produto")["total"].sum()

# Gráfico
vendas_mensais.plot(kind="bar")
plt.title("💰 Vendas Totais por Produto no Mês")
plt.xlabel("Produto")
plt.ylabel("Valor R$")
plt.tight_layout()
plt.show()

df_total.to_csv("relatorio_vendas_mensal.csv", index=False)
print("📁 Arquivo consolidado salvo como 'relatorio_vendas_mensal.csv'")
