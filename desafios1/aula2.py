# Desafio 5 — “Batalha de Dados” (Mini Game Estratégico)
# 🧩 Situação:
# Dois jogadores rolam dados. Quem tirar o maior número vence.
# Mas:
# O jogador 1 ganha 1 ponto por vitória.
# O jogo vai até alguém atingir 3 pontos.
# 💡 Pense antes:
# Como repetir rodadas até alguém chegar a 3 vitórias?
# Como comparar os resultados de cada rodada?
# Onde armazenar os pontos?
# 👉 Esse treino junta laços, comparações, controle de estado e condições compostas.

import random
from time import sleep
from emoji import emojize
from rich import print
from rich.console import Console

console = Console()
console.clear()
print(emojize(":crossed_swords: [bold red] Batalha de dados [/bold red] :crossed_swords:"))

pontos_jogador1 = 0
pontos_jogador2 = 0

while True:
    console.rule("[bold blue] Nova Rodada [/bold blue]")
    input("pressione [bold green] ENTER [/bold green] para rolar os dados...")

    dado_jogador1 = random.randint(1, 6)
    dado_jogador2 = random.randint(1, 6)
    print(f"Jogador 1 tirou: [bold yellow]{dado_jogador1}[/bold yellow]")
    print(f"Jogador 2 tirou: [bold yellow]{dado_jogador2}[/bold yellow]")
    sleep(1)

    if dado_jogador1 > dado_jogador2:
        pontos_jogador1 += 1
        print(emojize(":trophy: [bold green] Jogador 1 vence a rodada! [/bold green] :trophy:"))
    elif dado_jogador2 > dado_jogador1:
        pontos_jogador2 += 1
        print(emojize(":trophy: [bold green] Jogador 2 vence a rodada! [/bold green] :trophy:"))
    else:
        print(emojize(":handshake: [bold yellow] Empate! Niguem pontura. [/bold yellow] :handshake:"))
        print("Vamos para a proxima rodada...")

    print(f"Pontos: Jogador 1 = [bold cyan]{pontos_jogador1}[/bold cyan] | Jogador 2 = [bold cyan]{pontos_jogador2}[/bold cyan]")

    if pontos_jogador1 == 3:
        print(emojize(":conffetti_ball: [bold magenta] Jogador 1 é o grande campeão! [/bold magenta] :confetti_ball:"))
        break

    if pontos_jogador2 == 3:
        print(emojize(":conffetti_ball: [bold magenta] Jogador 2 é o grande campeão! [/bold magenta] :confetti_ball:"))
        break

console.rule("[bold red] Fim de Jogo [/bold red]")

# Obs: esse código não trata valores inválidos (ex: 125)



