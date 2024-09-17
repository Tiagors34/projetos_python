import sqlite3

class SistemaEstoque:
    def __init__(self):
        self.conn = sqlite3.connect('estoque.db')
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        # Criação da tabela de mercadorias
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mercadorias (
                codigo INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                localizacao TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def adicionar_mercadoria(self, codigo, nome, quantidade, localizacao):
        # Adiciona uma nova mercadoria ao banco de dados
        try:
            self.cursor.execute('''
                INSERT INTO mercadorias (codigo, nome, quantidade, localizacao)
                VALUES (?, ?, ?, ?)
            ''', (codigo, nome, quantidade, localizacao))
            self.conn.commit()
            print(f"Mercadoria {nome} adicionada com sucesso!")
        except sqlite3.IntegrityError:
            print("Código já existente no estoque!")

    def consultar_localizacao(self, codigo):
        # Consulta a localização de uma mercadoria pelo código
        self.cursor.execute('''
            SELECT nome, localizacao FROM mercadorias WHERE codigo = ?
        ''', (codigo,))
        resultado = self.cursor.fetchone()
        if resultado:
            nome, localizacao = resultado
            return f"Mercadoria: {nome}, Localização: {localizacao}"
        else:
            return "Mercadoria não encontrada!"

    def listar_mercadorias(self):
        # Lista todas as mercadorias cadastradas
        self.cursor.execute('''
            SELECT codigo, nome, quantidade, localizacao FROM mercadorias
        ''')
        mercadorias = self.cursor.fetchall()
        if not mercadorias:
            print("Nenhuma mercadoria cadastrada.")
        else:
            for codigo, nome, quantidade, localizacao in mercadorias:
                print(f"Código: {codigo}, Nome: {nome}, Quantidade: {quantidade}, Localização: {localizacao}")

    def fechar_conexao(self):
        # Fecha a conexão com o banco de dados
        self.conn.close()


# Exemplo de uso do sistema
def main():
    sistema = SistemaEstoque()

    # Adicionando mercadorias ao sistema
    sistema.adicionar_mercadoria(101, "Teclado", 50, "A1")
    sistema.adicionar_mercadoria(102, "Monitor", 30, "B2")
    sistema.adicionar_mercadoria(103, "Mouse", 100, "A3")

    # Consultando a localização de uma mercadoria
    print(sistema.consultar_localizacao(102))

    # Listando todas as mercadorias
    sistema.listar_mercadorias()

    # Fechar a conexão com o banco de dados
    sistema.fechar_conexao()

if __name__ == "__main__":
    main()
