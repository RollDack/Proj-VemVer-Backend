from flask import Blueprint, request, jsonify
from config import db
from pedido.model_pedido import Pedido
from produto.model_produto import Produto
from datetime import datetime

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

    try:
        id_cliente = dados['id_cliente']
        id_produto = dados['id_produto']
        valor_total = dados['valor_total']
        data_pedido_str = dados['data_pedido']
        data_pedido = datetime.strptime(data_pedido_str, "%Y-%m-%d").date()
    except KeyError as e:
        return jsonify({'erro': f'Campo obrigatório ausente: {e.args[0]}'}), 400

    produto = Produto.query.get(id_produto)
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    if produto.quantidade <= 0:
        return jsonify({'erro': 'Estoque insuficiente'}), 400

    novo_pedido = Pedido(
        id_cliente=id_cliente,
        id_produto=id_produto,
        valor_total=valor_total,
        data_pedido=data_pedido
    )

    produto.quantidade -= 1
    db.session.add(novo_pedido)
    db.session.commit()

    return jsonify(novo_pedido.to_dict()), 201

@pedidos_blueprint.route('/<int:id_pedido>', methods=['PUT'])
def atualizar_pedido(id_pedido):
    pedido = Pedido.query.get_or_404(id_pedido)
    dados = request.get_json()

    if 'valor_total' in dados:
        pedido.valor_total = dados['valor_total']
    if 'data_pedido' in dados:
        try:
            pedido.data_pedido = datetime.strptime(dados['data_pedido'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({'erro': 'Formato de data inválido. Use YYYY-MM-DD.'}), 400

    db.session.commit()
    return jsonify(pedido.to_dict())

@pedidos_blueprint.route('/<int:id_pedido>', methods=['DELETE'])
def deletar_pedido(id_pedido):
    pedido = Pedido.query.get_or_404(id_pedido)
    produto = Produto.query.get(pedido.id_produto)
    if produto:
        produto.quantidade += 1  

    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'mensagem': 'Pedido cancelado e estoque atualizado'})
