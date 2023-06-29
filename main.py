import sqlite3

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print("Nome: ", self.nome)
        print("Email: ", self.email)

    def salvar_no_banco(self):
        conexao = sqlite3.connect("banco_de_dados.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)",
                       (self.nome, self.email))
        conexao.commit()
        conexao.close()


class Administrador(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Cargo: ", self.cargo)


# Criação do banco de dados
conexao = sqlite3.connect("banco_de_dados.db")
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, email TEXT)")
conexao.close()

# Exemplo de uso
usuario = Usuario("João", "joao@example.com")
usuario.exibir_informacoes()
usuario.salvar_no_banco()

administrador = Administrador("Maria", "maria@example.com", "Gerente")
administrador.exibir_informacoes()
administrador.salvar_no_banco()
