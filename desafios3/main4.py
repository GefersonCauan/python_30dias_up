# Criar um mini RPG de texto no terminal onde o jogador:
# Entra em um mundo com inimigos aleatórios,
# Faz escolhas (lutar, fugir, curar),
# # Ganha experiência, sobe de nível e pode morrer 😬
# O jogador tem:
# vida = 100
# ataque = 10
# nivel = 1
# xp = 0
# Cada turno, aparece um inimigo aleatório (ex: “Goblin”, “Lobo”, “Orc”) com vida e ataque aleatórios.
# O jogador pode:
# 1 - Lutar
# 2 - Fugir
# 3 - Usar poção (cura 30 de vida)
# Se o jogador vence, ganha XP e pode subir de nível (cada 50 XP = +1 nível e +5 de ataque).
# Se morrer, o jogo acaba com uma mensagem tipo: “💀 Você lutou bravamente, mas caiu em batalha!”

import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.ataque = 10
        self.nivel = 1
        self.xp = 0
        self.pocoes = 3

    def atacar(self, inimigo):
        dano = random.randint(self.ataque - 2, self.ataque + 2)
        inimigo.vida -= dano
        print(F"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")
            self.ganhar_xp(20)
            return True
        return False
    
    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"{self.nome} ganhou {quantidade} de XP!")
        if self.xp >= 50:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.ataque += 5
        self.xp = 0
        print(f"Parabéns {self.nome}! Você subiu para o nível {self.nivel}!")

    def usar_pocao(self):
        if self.pocoes > 0:
            self.vida += 30
            if self.vida > 100:
                self.vida = 100
            self.pocoes -= 1
            print(f"{self.nome} usou uma poção e recuperou vida! Vida atual: {self.vida}")
        else:
            print("Você não tem poções!")

class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, personagem):
        dano = random.randint(self.ataque - 2, self.ataque + 2)
        personagem.vida -= dano
        print(f"{self.nome} atacou {personagem.nome} causando {dano} de dano!")
        if personagem.vida <= 0:
            print(f"💀 {personagem.nome} lutou bravamente, mas caiu em batalha!")
            return True
        return False
def gerar_inimigo():
    tipos_inimigos = [
        ("Goblin", 30, 5),
        ("Lobo", 40, 7),
        ("Orc", 50, 10)
    ]
    tipo = random.choice(tipos_inimigos)
    return Inimigo(tipo[0], tipo[1], tipo[2])
def jogo():
    nome = input("Digite o nome do seu personagem: ")
    jogador = Personagem(nome)

    while jogador.vida > 0:
        inimigo = gerar_inimigo()
        print(f"\nUm {inimigo.nome} apareceu! (Vida: {inimigo.vida}, Ataque: {inimigo.ataque})")

        while inimigo.vida > 0 and jogador.vida > 0:
            print(f"\n{jogador.nome} - Vida: {jogador.vida}, Ataque: {jogador.ataque}, Nível: {jogador.nivel}, XP: {jogador.xp}, Poções: {jogador.pocoes}")
            print("Escolha uma ação:")
            print("1 - Lutar")
            print("2 - Fugir")
            print("3 - Usar poção")
            escolha = input("Digite o número da ação desejada: ")

            if escolha == "1":
                if jogador.atacar(inimigo):
                    break
                if inimigo.atacar(jogador):
                    return
            elif escolha == "2":
                print(f"{jogador.nome} fugiu da batalha!")
                break
            elif escolha == "3":
                jogador.usar_pocao()
            else:
                print("Ação inválida! Tente novamente.")

    print("Fim de jogo!")

if __name__ == "__main__":
    jogo()