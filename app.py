import sqlite3

carrinho = []

menu = {
    "Hamburguer": 15,
    "Pizza": 30,
    "Refrigerante": 5
}

def adicionar(item):
    carrinho.append(item)
    print(f"{item} adicionado!")

def ver_carrinho():
    total = 0
    print("\nCarrinho:")
    
    if not carrinho:
        print("Carrinho vazio!")
        return 0

    for item in carrinho:
        print(f"- {item} R${menu[item]}")
        total += menu[item]

    print(f"Total: R${total}")
    return total

def finalizar():
    if not carrinho:
        print("Carrinho vazio!")
        input("\nPressione ENTER para continuar...")
        return

    total = ver_carrinho()

    conn = sqlite3.connect("pedidos.db")
    cursor = conn.cursor()

    itens_str = ", ".join(carrinho)

    cursor.execute(
        "INSERT INTO pedidos (itens, total) VALUES (?, ?)",
        (itens_str, total)
    )

    conn.commit()
    conn.close()

    print("\nPedido salvo no banco!")

    carrinho.clear()

    input("\nPressione ENTER para continuar...")

def ver_pedidos():
    conn = sqlite3.connect("pedidos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()

    print("\n📦 Histórico de pedidos:\n")

    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        for pedido in pedidos:
            print(f"ID: {pedido[0]}")
            print(f"Itens: {pedido[1]}")
            print(f"Total: R${pedido[2]}")
            print("-" * 20)

    conn.close()

    input("\nPressione ENTER para continuar...")

while True:
    print("\n===== MENU =====")
    print("1 - Hamburguer")
    print("2 - Pizza")
    print("3 - Refrigerante")
    print("4 - Ver carrinho")
    print("5 - Finalizar pedido")
    print("6 - Ver histórico de pedidos")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        adicionar("Hamburguer")
    elif op == "2":
        adicionar("Pizza")
    elif op == "3":
        adicionar("Refrigerante")
    elif op == "4":
        ver_carrinho()
        input("\nPressione ENTER para continuar...")
    elif op == "5":
        finalizar()
    elif op == "6":
        ver_pedidos()
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")