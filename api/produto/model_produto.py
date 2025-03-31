from config import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.relationship("Estoque", backref="produto", lazy=True)

    def __init__(self, nome, tipo, preco):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

    def to_dict(self):
        return{'id': self.id, 'nome': self.nome, 'tipo': self.tipo, 'preco': self.preco}    