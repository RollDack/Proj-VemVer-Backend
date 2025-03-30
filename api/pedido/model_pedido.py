from config import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.Date, nullable=False)