# Crie um programa com:
# Lista de mesas [1, 2, 3, 4, 5]
# Função reservar_mesa(numero)
# Função cancelar_reserva(numero)
# Função listar_reservas()
# Mostre mensagens de erro se a mesa já estiver ocupada

mesas = [1, 2, 3, 4, 5]

reservas = []

def reservar_mesa(numero):
    if numero in reservas:
        print(f"Mesa {numero}")
        print("Erro: Mesa ja esta ocupada.")
    elif numero in mesas:
        reservas.append(numero)
        print(f"Mesa {numero} reservada com sucesso.")
    else:
        print(f"Mesa {numero} nao existe.")

def cancelar_reserva(numero):
    if numero in reservas:
        reservas.remove(numero)
        print(f"mesa {numero} cancelada com sucesso.")
    else:
        print(f"Erro: Mesa {numero} não esta reservada.")

def listar_resevas():
    if reservas:
        print("Mesas reservadas:", reservas)
    else:
        print("Nenhuma mesa reservada.")
# Exemplo de uso
reservar_mesa(2)
cancelar_reserva(2)
listar_resevas()