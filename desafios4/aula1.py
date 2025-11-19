# Desafio real
# Crie um sistema de inventário de loja:
# Cada produto tem nome, preço e estoque
# O usuário pode adicionar, remover, atualizar e listar produtos
# Use dicionários e listas

inventario = []
def adicionar_produto(nome, preco, estoque):
    produto = {
        'nome': nome,
        'preco': preco,
        'estoque': estoque
    }

    inventario.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def remover_produto(nome):
    for produto in inventario:
        if produto['nome'] == nome:
            inventario.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado.")

def atualizar_produto(nome, preco=None, estoque=None):
    for produto in inventario:
        if produto['nome'] == nome:
            if preco is not None:
                produto['preco'] = preco
                if estoque is not None:
                    produto['estoque'] = estoque
            print(f"Produto '{nome}' atualizado com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado.")

def listar_produtos():
    for produto in inventario:
     if not inventario:
        print("Nenhum produto no inventario. ")
        print(F"Nome: {produto['nome']}, Preço: {produto['preco']}, Estoque: {produto['estoque']}")
    else:
        for produto in inventario:
            print(F"Nome: {produto['nome']}, Preço: {produto['preco']}, Estoque: {produto['estoque']}") 
# Exemplo de uso
adicionar_produto("Camisa", 29.99, 100)
adicionar_produto("Calça", 49.99, 50)
listar_produtos()