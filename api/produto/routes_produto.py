from flask import Blueprint, request, jsonify
from config import db
from produto.model_produto import Produto

produtos_blueprint = Blueprint('produtos', __name__)

@produtos_blueprint.route('/', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.to_dict() for produto in produtos])

@produtos_blueprint.route('/<int:id_produto>', methods=['GET'])
def obter_produto(id_produto):
    produto = Produto.query.get_or_404(id_produto)
    return jsonify(produto.to_dict())

@produtos_blueprint.route('/', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    novo_produto = Produto(
        nome=dados['nome'],
        tipo=dados['tipo'],
        preco=dados['preco'],
        quantidade=dados['quantidade']
    )
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify(novo_produto.to_dict()), 201

@produtos_blueprint.route('/<int:id_produto>', methods=['PUT'])
def atualizar_produto(id_produto):
    produto = Produto.query.get_or_404(id_produto)
    dados = request.get_json()
    produto.nome = dados.get('nome', produto.nome)
    produto.tipo = dados.get('tipo', produto.tipo)
    produto.preco = dados.get('preco', produto.preco)
    produto.quantidade = dados.get('quantidade', produto.quantidade)
    db.session.commit()
    return jsonify(produto.to_dict())

@produtos_blueprint.route('/<int:id_produto>', methods=['DELETE'])
def deletar_produto(id_produto):
    produto = Produto.query.get_or_404(id_produto)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto deletado com sucesso'})
