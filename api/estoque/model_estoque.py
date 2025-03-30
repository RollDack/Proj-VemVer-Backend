from config import db


class Estoque(db.Model):
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"), primary_key=True)
    quantidade_produtos = db.Column(db.Integer, nullable=False)