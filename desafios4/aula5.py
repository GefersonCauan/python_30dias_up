import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv("vendas.csv")

# Mostra as 5 primeiras linhas
print(df.head())

# Informações básicas do DataFrame
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Criando nova coluna de valor total por linha
df["total"] = df["preco"] * df["quantidade"]

# Agrupando vendas por produto
vendas_por_produto = df.groupby("produto")["total"].sum()
print(vendas_por_produto)
print(vendas_por_produto)

# Cria gráfico de barras
vendas_por_produto.plot(kind="bar")
plt.title("Total de Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Valor R$")
plt.tight_layout()
plt.show()
