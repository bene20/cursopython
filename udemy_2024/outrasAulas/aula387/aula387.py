import sqlite3
import os

ROOT_DIR = os.path.dirname(__file__)
DB_FILE = ROOT_DIR + '/db.sqlite3'

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Criando a minha tabela
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS customers('
        ' id INTEGER PRIMARY KEY AUTOINCREMENT,'
        ' name TEXT ,'
        ' weight REAL'
        ')'
    )

    # Removendo todos os dados na tabela
    cursor.execute('DELETE FROM customers')

    # Inserindo dados na tabela
    # cursor.execute(
    #     'INSERT INTO customers (name, weight) VALUES (?, ?)',
    #     ['Bruna', 35.9]
    # )

    # Inserindo dados na tabela
    cursor.executemany(
        'INSERT INTO customers (name, weight) VALUES (?, ?)',
        (('Bruna', 35.9), ('Caio', 22.3), ('Davi', 17), ('Enio', 5.2))
    )

    # Comitando minhas transações
    conn.commit()
finally:
    cursor.close()
    conn.close()