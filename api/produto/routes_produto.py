from flask import Blueprint, request, jsonify
from config import db                                                   #LEMBRAR DE COLOCAR UM EXCEPTION NO MODEL E TRY EXCEPT NO ROUTES(TRATAMENTO DE ERRO)
from model_produto import Produto
from estoque.model_estoque import Estoque


produtos_blueprint = Blueprint('produtos', __name__)


@produtos_blueprint.route('/produtos', methods=['GET'])#lista todos os produtos
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.to_dict() for produto in produtos])

@produtos_blueprint.route('/produtos/<int:id_produto>', methods=['GET'])#obtem detalhes de um produto especifico
def obter_produto(id_produto):
    produto = Produto.query.get(id_produto)
    return jsonify(produto.to_dict()) if produto else (jsonify({'erro': 'Produto não encontrado'}), 404)

@produtos_blueprint.route('/produtos', methods=['POST'])#adiciona um novo produto
def criar_produto():
    dados = request.get_json()
    novo_produto = Produto(**dados)
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify(novo_produto.to_dict()), 201

@produtos_blueprint.route('/produtos/<int:id_produto>', methods=['PUT'])#atualiza informações de um produto
def atualizar_produto(id_produto):
    produto = Produto.query.get(id_produto)
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    dados = request.get_json()
    for chave, valor in dados.items():
        setattr(produto, chave, valor)
    db.session.commit()
    return jsonify(produto.to_dict())

@produtos_blueprint.route('/produtos/<int:id_produto>', methods=['DELETE'])#remove um produto
def deletar_produto(id_produto):
    produto = Produto.query.get(id_produto)
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto deletado com sucesso'})

@produtos_blueprint.route('/produtos/<int:id_produto>/estoque', methods=['GET'])#obtém a quantidade disponivel do produto no estoque
def obter_estoque_produto(id_produto):
    produto = Produto.query.get(id_produto)
    
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    
    estoque = Estoque.query.filter_by(id_produto=id_produto).first()
    
    if not estoque:
        return jsonify({"erro": "Estoque não encontrado para este produto"}), 404

    return jsonify({
        "id_produto": produto.id,
        "nome": produto.nome,
        "quantidade_disponivel": estoque.quantidade_produtos
    }), 200