from config import db
from datetime import datetime, date

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.Date, nullable=False)

    def __init__(self, id_cliente, id_produto, valor_total, data_pedido):
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.valor_total = valor_total #provavelmente terá um método pra calcular isso
        self.data_pedido = data_pedido #outro método provavelmente

    def to_dict(self):
        return{'id': self.id, 'id_cliente': self.id_cliente, 'id_produto': self.id_produto, 'valor_total': self.valor_total, 'data_pedido': self.data_pedido}    