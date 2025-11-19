# Desafio: Sistema de Login Simples (modo local)
# Você vai criar um programa que:
# Pede usuário e senha.
# Verifica se estão corretos.
# Se estiverem certos, mostra “Login bem-sucedido!”.
# Se estiverem errados, mostra “Usuário ou senha incorretos” e permite tentar novamente.
# Usa função pra organizar a lógica
# Usa loop pra permitir múltiplas tentativas

def sistema_login():
    usuario_correto = "admin"
    senha_correta = "senha123"
    tentativas = 3
    while tentativas > 0:
        usuario = input("Digite um usuario: ")
        senha = input("Digite a senha: ")
        if usuario == usuario_correto and senha == senha_correta:
            print("Login bem-sucedido!")
            return
        else:
            tentativas -= 1
            print(f"usuario ou senha incorretos. Tentativas restantes: {tentativas}")
    print("Número máximo de tentativas atingido. Acesso bloqueado.")
sistema_login()
