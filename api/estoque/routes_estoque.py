from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from config import db
from estoque.model_estoque import Estoque

estoque_blueprint = Blueprint('estoque', __name__)


@estoque_blueprint.route('/atualizar/<int:id_produto>', methods=['PUT'])
def atualizar_estoque(id_produto):
    estoque = Estoque.query.filter_by(id_produto=id_produto).first()
    if not estoque:
        return jsonify({'erro': 'Produto não encontrado no estoque'}), 404
    dados = request.get_json()
    estoque.quantidade_produtos = dados.get('quantidade', estoque.quantidade_produtos)
    db.session.commit()
    return jsonify({'mensagem': 'Estoque atualizado com sucesso', 'quantidade_atualizada': estoque.quantidade_produtos})