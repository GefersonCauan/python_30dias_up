# — O Cofrinho Inteligente
# 💰 Objetivo:
# Crie um programa que:
# Peça valores de depósitos até o usuário digitar “sair”.
# Mostre o total guardado e quantas vezes o usuário depositou.
# 💡 Pistas:
# while True: pra repetir até digitar “sair”.
# input() pra receber o valor.
# break pra sair do loop.
# += pra somar o total.

total = 0.0 

contador = 0

while True:
    entrada = input("Digite o valor do deposito ou 'sair' para encontrar:")
    if entrada.lower() == "sair":
        break
    try:
        valor = float(entrada)
        total += valor
        contador += 1
        print(f"voce depositou R${valor:.2f} no cofrinho. Total atual: R${total:.2f}")
    except ValueError:
        print("por favor, digite um valor valido ou 'sair'.")
        print(f"voçe fez {contador} depositos e tem R${total:.2f} no cofrinho.")

print("Obrigado por usar o cofrinho inteligente!")
