# crie um quiz de futebol com python
# lista uma lista perguntas sobre jogadores com mais bolas de ouro da historia
# a lista tersa messi com 8, cr7 com 5, neymar com 0
# devera ter errou e tente novamnete 2 chances pra cada pergunta

def quiz_futebol():
    perguntas = {
        "Quantas bolas de ouro Lionel Messi tem? ": 8,
        "Quantas bolas de ouro Cristiano Ronaldo tem? ": 5,
        "Quantas bolas de ouro Neymar tem? ": 0
    }

    for pergunta, resposta_correta in perguntas.items():
        tentativas = 2
        while tentativas > 0:
            resposta_usuario = input(pergunta)
            if resposta_usuario.isdigit() and int(resposta_usuario) == resposta_correta:
                print("Resposta correta!")
                break
            else:
                tentativas -= 1
                if tentativas > 0:
                    print(f"Resposta incorreta. Tente novamente. Você tem {tentativas} tentativa(s) restante(s).")
                else:
                    print(f"Resposta incorreta. A resposta correta é {resposta_correta}.")
# quiz_futebol()
quiz_futebol()