from flask import Blueprint, request, jsonify
from config import db
from pedido.model_pedido import Pedido
from produto.model_produto import Produto

pedidos_blueprint = Blueprint('pedidos', __name__)

@pedidos_blueprint.route('/', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([pedido.to_dict() for pedido in pedidos])

@pedidos_blueprint.route('/<int:id_pedido>', methods=['GET'])
def obter_pedido(id_pedido):
    pedido = Pedido.query.get_or_404(id_pedido)
    return jsonify(pedido.to_dict())

@pedidos_blueprint.route('/', methods=['POST'])
def criar_pedido():
    dados = request.get_json()
    produto = Produto.query.get(dados['id_produto'])
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    if produto.quantidade < dados['quantidade']:
        return jsonify({'erro': 'Estoque insuficiente'}), 400

    novo_pedido = Pedido(
        id_cliente=dados['id_cliente'],
        id_produto=dados['id_produto'],
        quantidade=dados['quantidade'],
        status=dados.get('status', 'pendente')
    )
    produto.quantidade -= dados['quantidade']
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify(novo_pedido.to_dict()), 201

@pedidos_blueprint.route('/<int:id_pedido>', methods=['PUT'])
def atualizar_pedido(id_pedido):
    pedido = Pedido.query.get_or_404(id_pedido)
    dados = request.get_json()
    nova_quantidade = dados.get('quantidade', pedido.quantidade)

    if nova_quantidade != pedido.quantidade:
        produto = Produto.query.get(pedido.id_produto)
        diferenca = nova_quantidade - pedido.quantidade
        if produto.quantidade < diferenca:
            return jsonify({'erro': 'Estoque insuficiente'}), 400
        produto.quantidade -= diferenca

    pedido.quantidade = nova_quantidade
    pedido.status = dados.get('status', pedido.status)
    db.session.commit()
    return jsonify(pedido.to_dict())

@pedidos_blueprint.route('/<int:id_pedido>', methods=['DELETE'])
def deletar_pedido(id_pedido):
    pedido = Pedido.query.get_or_404(id_pedido)
    produto = Produto.query.get(pedido.id_produto)
    produto.quantidade += pedido.quantidade
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'mensagem': 'Pedido cancelado e estoque atualizado'})
