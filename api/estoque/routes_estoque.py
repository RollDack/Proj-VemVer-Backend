from flask import Blueprint, request, jsonify
from config import db
from model_estoque import Estoque

estoque_blueprint = Blueprint('estoque', __name__)


@estoque_blueprint.route('/estoque/<int:id_produto>', methods=['PUT'])
def atualizar_estoque(id_produto):
    estoque = Estoque.query.filter_by(id_produto=id_produto).first()
    if not estoque:
        return jsonify({'erro': 'Produto não encontrado no estoque'}), 404
    dados = request.json()
    estoque.quantidade_produtos = dados.get('quantidade', estoque.quantidade_produtos)
    db.session.commit()
    return jsonify({'mensagem': 'Estoque atualizado com sucesso', 'quantidade_atualizada': estoque.quantidade_produtos})