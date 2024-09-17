import tkinter as tk
from tkinter import messagebox

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

    def adicionar_mercadoria(self, codigo, nome, quantidade, localizacao):
        if codigo not in self.estoque:
            mercadoria = Mercadoria(codigo, nome, quantidade, localizacao)
            self.estoque[codigo] = mercadoria
            return True
        else:
            return False

    def consultar_localizacao(self, codigo):
        if codigo in self.estoque:
            mercadoria = self.estoque[codigo]
            return f"Mercadoria: {mercadoria.nome}, Localização: {mercadoria.localizacao}"
        else:
            return None

    def listar_mercadorias(self):
        if not self.estoque:
            return "Nenhuma mercadoria cadastrada."
        else:
            mercadorias_list = ""
            for codigo, mercadoria in self.estoque.items():
                mercadorias_list += (f"Código: {codigo}, Nome: {mercadoria.nome}, "
                                     f"Quantidade: {mercadoria.quantidade}, Localização: {mercadoria.localizacao}\n")
            return mercadorias_list

# Interface gráfica usando Tkinter
class EstoqueApp:
    def __init__(self, root):
        self.sistema = SistemaEstoque()
        
        root.title("Sistema de Estoque")
        root.geometry("500x400")

        # Labels e entradas
        tk.Label(root, text="Código").grid(row=0, column=0)
        tk.Label(root, text="Nome").grid(row=1, column=0)
        tk.Label(root, text="Quantidade").grid(row=2, column=0)
        tk.Label(root, text="Localização").grid(row=3, column=0)

        self.codigo_entry = tk.Entry(root)
        self.nome_entry = tk.Entry(root)
        self.quantidade_entry = tk.Entry(root)
        self.localizacao_entry = tk.Entry(root)

        self.codigo_entry.grid(row=0, column=1)
        self.nome_entry.grid(row=1, column=1)
        self.quantidade_entry.grid(row=2, column=1)
        self.localizacao_entry.grid(row=3, column=1)

        # Botões
        tk.Button(root, text="Adicionar Mercadoria", command=self.adicionar_mercadoria).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Consultar Localização", command=self.consultar_localizacao).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Listar Mercadorias", command=self.listar_mercadorias).grid(row=6, column=0, columnspan=2, pady=10)

        # Área de exibição de resultados
        self.resultado_text = tk.Text(root, height=10, width=50)
        self.resultado_text.grid(row=7, column=0, columnspan=2, pady=10)

    def adicionar_mercadoria(self):
        codigo = self.codigo_entry.get()
        nome = self.nome_entry.get()
        quantidade = self.quantidade_entry.get()
        localizacao = self.localizacao_entry.get()

        if codigo and nome and quantidade and localizacao:
            if self.sistema.adicionar_mercadoria(codigo, nome, quantidade, localizacao):
                messagebox.showinfo("Sucesso", "Mercadoria adicionada com sucesso!")
            else:
                messagebox.showwarning("Erro", "Código já existente no estoque.")
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

    def consultar_localizacao(self):
        codigo = self.codigo_entry.get()
        if codigo:
            resultado = self.sistema.consultar_localizacao(codigo)
            if resultado:
                self.resultado_text.delete(1.0, tk.END)
                self.resultado_text.insert(tk.END, resultado)
            else:
                messagebox.showwarning("Erro", "Mercadoria não encontrada!")
        else:
            messagebox.showwarning("Erro", "Por favor, insira o código da mercadoria.")

    def listar_mercadorias(self):
        resultado = self.sistema.listar_mercadorias()
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, resultado)

# Função principal para rodar o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()
