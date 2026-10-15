from datetime import datetime
import sqlite3


def criar_tabela():
    conexao = sqlite3.connect("monitoramento.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS checagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            status TEXT,
            data_hora TEXT
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_checagem(nome, status):
    conexao = sqlite3.connect("monitoramento.db")
    cursor = conexao.cursor()

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO checagens (nome, status, data_hora) VALUES (?, ?, ?)",
        (nome, status, agora)
    )

    conexao.commit()
    conexao.close()


def listar_checagens():
    conexao = sqlite3.connect("monitoramento.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM checagens")
    resultados = cursor.fetchall()

    conexao.close()
    return resultados


if __name__ == "__main__":
    criar_tabela()
    salvar_checagem("Google", "UP | 180 ms")
    checagens = listar_checagens()
    print(checagens)
