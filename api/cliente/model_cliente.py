from config import db


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    pedidos = db.relationship("Pedido", backref="cliente", lazy=True)

    def __init__(self, cpf, nome, senha, idade, email, cep, telefone):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.idade = idade
        self.email = email
        self.cep = cep
        self.telefone = telefone

    def to_dict(self):
        return{'id': self.id, 'cpf': self.cpf, 'nome': self.nome, 'senha': self.senha, 'idade': self.idade, 'email': self.email, 'cep': self.cep, 'telefone': self.telefone}


class ClienteNaoEncontrado(Exception):
  pass
       