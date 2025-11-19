import json

estoque = []
id_counter = 1

def adicionar_produto(nome, quantidade, preco):
    global id_counter
    produto = {
        "id": id_counter,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    estoque.append(produto)
    id_counter += 1
    print(f"✅ Produto '{nome}' adicionado com sucesso!")

def remove_produto(id_produto):
    global estoque
    for produto in estoque:
        if produto["1"] == id_produto:
            estoque.remove(produto)
            print(f"🗑️ Produto '{produto['nome']}' removido com sucesso!")
            return
    print("Produto não foi encontrado!")

def atualizar_quantide(id_produto, nova_qtd):
    for produto in estoque:
        if produto["id"] == id_produto:
            produto["quantidade"] = nova_qtd
            print(f"🔄 Quantidade do produto '{produto['nome']}' atualizada para {nova_qtd}.")
            return
    print("Produto não foi encontrado!")    

def lista_produtos():
    if not estoque:
        print("📭 estoque vazio.")
        return
    print("\n--- LISTA DE PRODUTOS ---")
    print(f"{'ID': <5} {'Nome':<20} {'QTD':<10} {'Preço'}")
    print("-" * 50)
    for produto in estoque:
         print(f"{produto['id']:<5} {produto['nome']:<20} {produto['quantidade']:<10} {produto['preco']:<10.2f}")

def gerar_relatorios():
    if not estoque:
        print("📭 Estoque vazio.")
        return

    valor_total = sum(p["quantidade"] * p["preco"] for p in estoque)
    produto_caro = max(estoque, key=lambda p: p["preco"])
    produto_qtd = max (estoque, key=lambda p: p["quantidade"])
    
    print("\n--- RELATORIOS ---")
    print(f"💰 Valor total do estoque: R$ {valor_total:.2f}")
    print(f"💎 Produto mais caro: {produto_caro['nome']} (R$ {produto_caro['preco']:.2f})")
    print(f"📦 Produto com maior quantidade: {produto_qtd['nome']} ({produto_qtd['quantidade']} unidades)")

def salvar_estoque():
    with open("estoque.json", "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)
    print("💾 Estoque salvo em 'estoque.json'")

def carregar_estoque():
    global estoque, id_counter
    try:
        with open("estoque.json", "r", encoding="utf-8") as f:
            estoque = json.load(f)
        if estoque:
            id_counter = max([p["id"] for p in estoque]) + 1
        print("📂 Estoque carregado com sucesso!")
    except  FileNotFoundError:
        print("⚠️ Nenhum arquivo encontrado, estoque vazio.")

def menu():
    carregar_estoque()
    while True:
        print("\n--- MENU ESTOQUE ---")
        print("1. Adicionar Produto")
        print("2. Remove produto")
        print("3. Atualizar quantidade")
        print("4. Listar produtos")
        print("5. Relatorio")
        print("6. Salvar e sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade: "))
            preco = float(input("preço: "))
            adicionar_produto(nome, qtd, preco)

        elif opcao == "2":
            id_produto = int(input("ID do produto a remover: "))
            remove_produto(id_produto)

        elif opcao == "3":
            id_produto = int(input("ID do Produto: "))
            nova_qtd = int(input("Nova quantidade: "))
            atualizar_quantide(id_produto, nova_qtd)

        elif opcao == "4":
            lista_produtos()

        elif  opcao == "5":
            gerar_relatorios()

        elif opcao == "6":
            salvar_estoque()
            print("👋 Saindo...")
            break

        else: 
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    menu()           