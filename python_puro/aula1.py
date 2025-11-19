# crie um sistema de saque, deposito

saldo = 1000

while True:
    print("1. depositar")
    print("2. sacar")
    print("3. ver saldo")
    print("4. sair")

    escolha = int(input("escolhar uma opção: "))

    if escolha == 1:
        valor = float(input("Qual valor deseja depositar? "))
        saldo += valor
        print("saldo depositado...")

    elif escolha == 2:
        valor = int(input("Quanto deseja sacar?" ))
        saldo -= valor
        print("valor sacado com sucesso! ")

    elif escolha == 3:
        print(f"seu saldo e de {saldo}")

    elif escolha == 4:
        print("saindo...")
        break
