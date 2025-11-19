lista = []

while True:

    print("1- Adicionar item")
    print("2- remover item")
    print("3- consultar lista")
    print("4- Saindo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item a ser adiconado: ")
        lista.append(item)

    elif opcao == "2":
        item = input("Digite o item  a ser removido: ")
        if item in lista:
            lista.remove(item)
        else:
            print("item nao encontrado")

    elif opcao == "3":
        print(lista)

    elif opcao == "4":
        print("saindo...")
        break    


    # essa eu conseguir