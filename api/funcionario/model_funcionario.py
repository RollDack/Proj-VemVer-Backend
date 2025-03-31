from config import db


class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    telefone= db.Column(db.String(11), nullable=False)
    salario = db.Column(db.Float, nullable=False)