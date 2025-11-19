# O Caixa do Mercado
# 🧠 Situação:
# Você trabalha no caixa de um mercado.
# Cada cliente compra vários produtos com preços diferentes.
# Você precisa somar os valores, aplicar um desconto se o total for maior que R$ 100, e mostrar o valor final.
# 🎯 Objetivo:
# Perguntar quantos produtos o cliente comprou.
# Receber o preço de cada produto.
# Somar o total.
# Se o total > 100 → aplicar 10% de desconto.
# Mostrar o valor final.
# 💡 Dicas de lógica:
# Você vai precisar de um loop for pra somar os preços.
# Um if pra aplicar o desconto.
# Variável total pra acumular os valores.

num_produtos = int(input("Quantos produtos o cliente comprou? "))
total = 0.0
for i in range(num_produtos):
    preco = float(input(f"Digite o preço do produtos {i + 1}: R$"))
    total += preco
    if total > 100:
        total *= 0.9  # Aplica 10% de desconto
        print("voce ganhou 10% de desconto")
        print(f"o valor final é R${total:.2f}")
    else:
        print(f"o valor final é R${total:.2f}")
print("Obrigado por comprar conosco!")
# Teste o código com diferentes números de produtos e preços para garantir que o desconto seja aplicado corretamente.