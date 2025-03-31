from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from config import db
from api.pedido.model_pedido import Pedido
from api.cliente.model_cliente import Cliente
from api.produto.model_produto import Produto
from api.estoque.model_estoque import Estoque

pedidos_blueprint = Blueprint('pedidos', __name__)


@pedidos_blueprint.route('/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([pedido.to_dict() for pedido in pedidos])


@pedidos_blueprint.route('/pedidos/<int:id_pedido>', methods=['GET'])
def obter_pedido(id_pedido):
    pedido = Pedido.query.get(id_pedido)
    return jsonify(pedido.to_dict()) if pedido else (jsonify({'erro': 'Pedido não encontrado'}), 404)

@pedidos_blueprint.route('/pedidos', methods=['POST'])
def criar_pedido():
    dados = request.get_json()
    id_cliente = dados.get('id_cliente')
    id_produto = dados.get('id_produto')
    
    cliente = Cliente.query.get(id_cliente)
    produto = Produto.query.get(id_produto)
    estoque = Estoque.query.filter_by(id_produto=id_produto).first()
    
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    if not estoque or estoque.quantidade_produtos <= 0:
        return jsonify({'erro': 'Produto sem estoque disponível'}), 400
    
    novo_pedido = Pedido(**dados)
    estoque.quantidade_produtos -= 1  
    
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify(novo_pedido.to_dict()), 201

@pedidos_blueprint.route('/pedidos/<int:id_pedido>', methods=["PUT"])
def atualizar_pedido(id_pedido):
    pedido = Pedido.query.get(id_pedido)
    if not pedido:
        return jsonify({'erro': 'Pedido não encontrado'}), 404
    
    dados = request.get_json()
    id_produto = dados.get('id_produto')
    if id_produto:
        produto = Produto.query.get(id_produto)
        estoque = Estoque.query.filter_by(id_produto=id_produto).first()
        
        if not produto:
            return jsonify({'erro': 'Produto não encontrado'}), 404
        if not estoque or estoque.quantidade_produtos <= 0:
            return jsonify({'erro': 'Produto sem estoque disponível'}), 400
        
        pedido.id_produto = id_produto
        estoque.quantidade_produtos -= 1  
    
    for chave, valor in dados.items():
        if chave != 'id_produto':  
            setattr(pedido, chave, valor)
    
    db.session.commit()
    return jsonify(pedido.to_dict())

@pedidos_blueprint.route('/pedidos/<int:id_pedido>', methods=['DELETE'])
def cancelar_pedido(id_pedido):
    pedido = Pedido.query.get(id_pedido)
    if not pedido:
        return jsonify({'erro': 'Pedido não encontrado'}), 404
    
    
    for item in pedido.itens:
        estoque = Estoque.query.filter_by(id_produto=item.id_produto).first()
        if estoque:
            estoque.quantidade_produtos += item.quantidade  
    
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'mensagem': 'Pedido cancelado com sucesso'})