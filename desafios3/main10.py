# Você é responsável por um sistema que decide qual veículo será usado pra entregar um pedido, baseado no peso.
# 🎯 Regras:
# Se o peso for até 10kg → moto 🏍️
# Se for até 20kg → carro 🚗
# Se for até 100kg → caminhão 🚚
# Se for maior que 100kg → “Carga muito pesada!”
# 🧠 Treino lógico:
# Receber o peso (input).
# Comparar o peso com os limites.
# Exibir o tipo de veículo
# 💡 Pense antes de digitar:
# Como eu garanto que apenas uma condição é verdadeira por vez?
# 👉 Dica: if / elif / else serve pra isso.

peso = float(input("Digite o peso da carga em kg: "))
if peso <= 10:
    print("voçe tem que ir de moto!")
elif peso <= 20:
    print("voce tem que ir de carro!")
elif peso <= 100:
    print("vote tem que ir de caminhao")       