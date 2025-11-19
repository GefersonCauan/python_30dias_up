# Simulador de Multas
# Pede:
# velocidade do carro
# limite da via
# Lógica:
# Se velocidade <= limite → “Dentro do limite”
# Se velocidade até 10% acima → “Atenção: leve excesso”
# Se velocidade até 30% acima → “Multa média”
# Se velocidade > 30% acima → “Multa gravíssima!”
# 👉 Treina: comparações com cálculos e operadores matemáticos

velocidade = float(input("Digite a velocidade do carro (km/h): "))
limite = float(input("Digite o limite de velocidade da via (km/h): "))
excesso = velocidade - limite
percentual_excesso = (excesso / limite) * 100
if velocidade <= limite:
    print("Dentro do limite")
elif percentual_excesso <= 10:
    print("Atenção: leve excesso")
elif percentual_excesso <= 30:
    print("Multa média")
else:
    print("Multa gravíssima!")
    