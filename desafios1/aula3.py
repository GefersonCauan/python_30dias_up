# Simula um semáforo:
# Pergunta a cor atual: verde, amarelo ou vermelho.
# Retorna o que o motorista deve fazer.
# verde → “Pode seguir”
# amarelo → “Atenção!”
# vermelho → “Pare!”
# 👉 Dica: usa .lower() pra tratar letras maiúsculas/minúsculas.

cor = input("Digite a cor do semafaro (verde, amarelo, vermelho):").lower()
if cor == "verde":
    print("Pode seguir")
elif cor == "amarelo":
    print("Atenção!")
elif cor == "vermelho":
    print("Pare!")
else:
    print("Cor inválida! Por favor, digite verde, amarelo ou vermelho.")