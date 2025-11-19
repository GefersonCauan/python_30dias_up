import random

numero_secreto = random.randint(1, 10)

tentativas = 3

print("🎲 Bem-vindo ao jogo de adivinhação!")
print("tente adivinhar um n umero de 1 a 10")

while tentativas > 0:
    try:

        chute = int(input("digite seu palpíte: "))
    except:

        print("isso nao e um numero valido")
        continue

    if chute == numero_secreto:
        print("acertou continue")
        break
    elif  chute > numero_secreto:
        print("numero secreto e menor") 
    else:
        print("numero secreto e maior")

    tentativas -= 1
    print(f"vc ainda tem {tentativas} tentativa(s).")

else:
    print("acabaram a chances")
    print(f"o numero secreto era {numero_secreto}")