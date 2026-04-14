import tkinter as tk
from tkinter import messagebox

menu = {
    "Hamburguer": 15.00,
    "Pizza": 30.00,
    "Refrigerante": 5.00,
    "Batata Frita": 10.00
}

carrinho = []

def adicionar_item(item):
    carrinho.append(item)
    atualizar_carrinho()

def remover_item():
    try:
        selecionado = lista.curselection()[0]
        carrinho.pop(selecionado)
        atualizar_carrinho()
    except:
        messagebox.showwarning("Aviso", "Selecione um item para remover")

def limpar_carrinho():
    carrinho.clear()
    atualizar_carrinho()

def atualizar_carrinho():
    lista.delete(0, tk.END)
    total = 0
    for item in carrinho:
        lista.insert(tk.END, f"{item} - R${menu[item]:.2f}")
        total += menu[item]
    label_total.config(text=f"Total: R${total:.2f}")

def finalizar():
    if not carrinho:
        messagebox.showwarning("Aviso", "Carrinho vazio!")
        return
    messagebox.showinfo("Pedido", "Pedido finalizado com sucesso!")
    carrinho.clear()
    atualizar_carrinho()

janela = tk.Tk()
janela.title("Sistema de Delivery")
janela.geometry("350x550")
janela.configure(bg="#f5f5f5")

tk.Label(janela, text="Cardápio", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)

for item in menu:
    tk.Button(
        janela,
        text=f"{item} - R${menu[item]:.2f}",
        width=25,
        bg="#4CAF50",
        fg="white",
        command=lambda i=item: adicionar_item(i)
    ).pack(pady=3)

tk.Label(janela, text="\nCarrinho", font=("Arial", 14, "bold"), bg="#f5f5f5").pack()

lista = tk.Listbox(janela, width=40, height=10)
lista.pack(pady=5)

label_total = tk.Label(janela, text="Total: R$0.00", font=("Arial", 12, "bold"), bg="#f5f5f5")
label_total.pack(pady=5)

tk.Button(janela, text="Remover Item", bg="#f44336", fg="white", command=remover_item).pack(pady=2)
tk.Button(janela, text="Limpar Carrinho", bg="#ff9800", fg="white", command=limpar_carrinho).pack(pady=2)
tk.Button(janela, text="Finalizar Pedido", bg="#2196F3", fg="white", command=finalizar).pack(pady=10)

janela.mainloop()

