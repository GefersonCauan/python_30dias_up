# Simulador de Clima Inteligente
# Pede
# temperatura (°C)
# condição do céu (“sol”, “chuva”, “nublado”)
# Lógica:
# Se chuva e temp < 15: "Pegue um casaco e um guarda-chuva!"
# Se sol e temp > 30: "Dia perfeito pra praia!"
# Se nublado e temp entre 20–25: "Tempo ótimo pra caminhar!"
# Caso contrário: "Clima indeciso hoje..."
# 👉 Treina: uso de and/or + faixas numéricas + elif múltiplos

def simulador_clima(temperatura, condicao):
    if condicao == "chuva" and temperatura < 15:
        print("pegue um casaco e um guarda-chuva!")
    elif condicao == "sol" and temperatura < 30:
        print("Dia perfeito para Praia!")
    elif condicao == "nublado" and temperatura <= 25:
        print("tempo otimo para caminhar")
    else:
        print("clima indeciso")

if __name__ == "__main__":
    temp = float(input("Digite a temperatura em °C: "))
    cond = input("Digite a condição do céu (sol, chuva, nublado): ").lower()
    simulador_clima(temp, cond)
