from config import db


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    pedidos = db.relationship("Pedido", backref="cliente", lazy=True)

    def __init__(self, id, cpf, nome, idade, email, cep, telefone):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cep = cep
        self.telefone = telefone