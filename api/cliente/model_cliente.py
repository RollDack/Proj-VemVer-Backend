from datetime import date

class Cliente:
    def __init__(self, id, cpf, nome, idade, email, cep, telefone):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cep = cep
        self.telefone = telefone

    def atualizar_email(self, novo_email):
        self.email = novo_email

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

class Funcionario:
    def __init__(self, id, cpf, nome, idade, email, cep, telefone, salario):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cep = cep
        self.telefone = telefone
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

class produto:
    def __init__(Self, id, id_cliente, id_produto, valor_produto, data_pedido=None):
        self.id = id
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.valor_total = valor_total
        self.valor_produto = valor_produto
        self.data_pedido = data_pedido if data_pedido else date.today()

    def atualizar_valor_total(Self, novo_valor):
        self.valor_total = novo_valor

class Estoque:
    def __init__(self, id_produto, nome_produto, quantidade_produtos):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.quantidade_produtos = quantidade_produtos

    def adicionar_produtos(self, quantidade):
        self.quantidade_produtos += quantidade

    def remover_produtos(self, quantidade):
        if quantidade <= self.quantidade_produtos:
            self.quantidade_produtos -= quantidade
        else:
            raise ValueError("Quantidade insuficiente em estoque")