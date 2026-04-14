# Sistema de Pedidos - Estilo iFood

menu = {
    1: {"nome": "Hamburguer", "preco": 15.00},
    2: {"nome": "Pizza", "preco": 30.00},
    3: {"nome": "Refrigerante", "preco": 5.00},
    4: {"nome": "Batata Frita", "preco": 10.00}
}

carrinho = []

def mostrar_menu():
    print("\n--- CARDÁPIO ---")
    for key, item in menu.items():
        print(f"{key} - {item['nome']} | R${item['preco']:.2f}")

def adicionar_item():
    try:
        escolha = int(input("Escolha o item: "))
        if escolha in menu:
            carrinho.append(menu[escolha])
            print(f"{menu[escolha]['nome']} adicionado ao carrinho!")
        else:
            print("Item inválido!")
    except:
        print("Erro! Digite um número.")

def ver_carrinho():
    print("\n--- SEU CARRINHO ---")
    total = 0
    for item in carrinho:
        print(f"{item['nome']} - R${item['preco']:.2f}")
        total += item['preco']
    print(f"Total: R${total:.2f}")

def finalizar_pedido():
    if not carrinho:
        print("Carrinho vazio!")
        return
    ver_carrinho()
    print("\nPedido finalizado com sucesso!")
    carrinho.clear()

def sistema():
    while True:
        print("\n1 - Ver menu")
        print("2 - Adicionar item")
        print("3 - Ver carrinho")
        print("4 - Finalizar pedido")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            mostrar_menu()
        elif opcao == "2":
            adicionar_item()
        elif opcao == "3":
            ver_carrinho()
        elif opcao == "4":
            finalizar_pedido()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

sistema()
