# Classe para armazenar as informações de cada mercadoria
class Mercadoria:
    def __init__(self, codigo, nome, quantidade, localizacao):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.localizacao = localizacao

# Classe para gerenciar o armazenamento e consulta das mercadorias
class SistemaEstoque:
    def __init__(self):
        self.estoque = {}

    # Método para adicionar uma nova mercadoria
    def adicionar_mercadoria(self, codigo, nome, quantidade, localizacao):
        if codigo not in self.estoque:
            mercadoria = Mercadoria(codigo, nome, quantidade, localizacao)
            self.estoque[codigo] = mercadoria
            print(f"Mercadoria {nome} adicionada com sucesso!")
        else:
            print("Código já existente no estoque!")

    # Método para consultar a localização de uma mercadoria pelo código
    def consultar_localizacao(self, codigo):
        if codigo in self.estoque:
            mercadoria = self.estoque[codigo]
            return f"Mercadoria: {mercadoria.nome}, Localização: {mercadoria.localizacao}"
        else:
            return "Mercadoria não encontrada!"

    # Método para listar todas as mercadorias
    def listar_mercadorias(self):
        if not self.estoque:
            print("Nenhuma mercadoria cadastrada.")
        else:
            for codigo, mercadoria in self.estoque.items():
                print(f"Código: {codigo}, Nome: {mercadoria.nome}, Quantidade: {mercadoria.quantidade}, Localização: {mercadoria.localizacao}")

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

if __name__ == "__main__":
    main()
