import sqlite3

# cria ou conecta ao banco
conn = sqlite3.connect("pedidos.db")

cursor = conn.cursor()

# cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    itens TEXT,
    total REAL
)
""")

conn.commit()

print("Banco criado com sucesso!")

conn.close()