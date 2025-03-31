from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from config import db
from api.cliente.model_cliente import Cliente
from api.pedido.model_pedido import Pedido

cliente_blueprint = Blueprint('clientes', __name__)

@cliente_blueprint.route("/clientes", methods=['GET']) 
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['GET']) 
def obter_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    return jsonify(cliente.to_dict()) if cliente else (jsonify({'erro': 'Cliente não encontrado'}), 404)


@cliente_blueprint.route('/clientes', methods=['POST']) 
def criar_cliente():
    dados = request.get_json()
    novo_cliente = Cliente(**dados)
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify(novo_cliente.to_dict()), 201

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['PUT']) 
def atualizar_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    dados = request.get_json()
    for chave, valor in dados.items():
        setattr(cliente, chave, valor)
    db.session.commit()
    return jsonify(cliente.to_dict())

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['DELETE']) 
def deletar_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensagem': 'Cliente deletado com sucesso'})

@cliente_blueprint.route('/clientes/<int:id_cliente>/pedidos', methods=['GET']) 
def listar_pedidos_cliente(id_cliente):
    pedidos = Pedido.query.filter_by(id_cliente=id_cliente).all()
    return jsonify([pedido.to_dict() for pedido in pedidos])
