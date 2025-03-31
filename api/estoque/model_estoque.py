from config import db


class Estoque(db.Model):
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"), primary_key=True)
    quantidade_produtos = db.Column(db.Integer, nullable=False)

    def __init__(self, id_produto, quantidade_produto):
        self.id_produto = id_produto
        self.quantidade_produtos = quantidade_produto

    def to_dict(self):
        return{'id_produto': self.id_produto, 'quantidade_produto': self.quantidade_produtos}    