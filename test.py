import unittest


class Pessoa:
    def __init__(self, id, cpf, nome, idade, email, cep, telefone):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cep = cep
        self.telefone = telefone


class Funcionario(Pessoa):
    def __init__(self, id, cpf, nome, idade, email, cep, telefone, salario):
        super().__init__(id, cpf, nome, idade, email, cep, telefone)
        self.salario = salario


class Produto:
    def __init__(self, id, nome, tipo, preco):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.preco = preco


class Pedido:
    def __init__(self, id, cliente, produto, valor_total, data_pedido):
        if not isinstance(cliente, Pessoa):
            raise TypeError("cliente deve ser uma instância da classe Pessoa")
        if not isinstance(produto, Produto):
            raise TypeError("produto deve ser uma instância da classe Produto")

        self.id = id
        self.cliente = cliente
        self.produto = produto
        self.valor_total = valor_total
        self.data_pedido = data_pedido


class Estoque:
    def __init__(self, id, nome, quant_produto):
        if not isinstance(id, int):
            raise TypeError("Id deve ser um número inteiro")
        if not isinstance(nome, str):
            raise TypeError("Nome deve ser uma string")
        if not isinstance(quant_produto, int) or quant_produto < 0:
            raise ValueError("Quantidade deve ser um número inteiro não negativo")

        self.id = id
        self.nome = nome
        self.quant_produto = quant_produto


class TestSistema(unittest.TestCase):

    def test_pessoa_valid(self):
        try:
            pessoa = Pessoa(2000, '36499815802', 'Bruno', 30, 'bruno@example.com.br', '05868020', '11947071056')
            self.assertEqual(pessoa.id, 2000)
            self.assertEqual(pessoa.cpf, '36499815802')
            self.assertEqual(pessoa.nome, 'Bruno')
            self.assertEqual(pessoa.idade, 30)
            self.assertEqual(pessoa.email, 'bruno@example.com.br')
            self.assertEqual(pessoa.cep, '05868020')
            self.assertEqual(pessoa.telefone, '11947071056')
        except Exception as e:
            self.fail(f"Erro inesperado ao cadastrar cliente: {e}")

    def test_funcionario_valid(self):
        try:
            funcionario = Funcionario(2000, '36499815802', 'Bruno', 30, 'bruno@example.com.br', '05868020', '11947071056', 2000.00)
            self.assertEqual(funcionario.id, 2000)
            self.assertEqual(funcionario.cpf, '36499815802')
            self.assertEqual(funcionario.nome, 'Bruno')
            self.assertEqual(funcionario.idade, 30)
            self.assertEqual(funcionario.email, 'bruno@example.com.br')
            self.assertEqual(funcionario.cep, '05868020')
            self.assertEqual(funcionario.telefone, '11947071056')
            self.assertEqual(funcionario.salario, 2000.00)
        except Exception as e:
            self.fail(f"Erro inesperado ao cadastrar funcionário: {e}")

    def test_produto_valid(self):
        try:
            produto = Produto(500, 'RayBan', 'Óculos de Grau', 1000.00)
            self.assertEqual(produto.id, 500)
            self.assertEqual(produto.nome, 'RayBan')
            self.assertEqual(produto.tipo, 'Óculos de Grau')
            self.assertEqual(produto.preco, 1000.00)
        except Exception as e:
            self.fail(f"Erro inesperado ao cadastrar Produto: {e}")

    def test_estoque_valid(self):
        try:
            estoque = Estoque(500, 'RayBan', 10)
            self.assertEqual(estoque.id, 500)
            self.assertEqual(estoque.nome, 'RayBan')
            self.assertEqual(estoque.quant_produto, 10)
        except Exception as e:
            self.fail(f"Erro inesperado ao cadastrar Estoque: {e}")


if __name__ == "__main__":
    unittest.main()
