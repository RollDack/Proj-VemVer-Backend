from config import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, tipo, preco, quantidade):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return{'id': self.id, 'nome': self.nome, 'tipo': self.tipo, 'preco': self.preco, 'quantidade': self.quantidade}


class ProdutoNaoEncontrado(Exception):
  pass