from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from config import db                                                   #LEMBRAR DE COLOCAR UM EXCEPTION NO MODEL E TRY EXCEPT NO ROUTES(TRATAMENTO DE ERRO)
from produto.model_produto import Produto
from estoque.model_estoque import Estoque


produtos_blueprint = Blueprint('produtos', __name__)


@produtos_blueprint.route('/', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([
        {**produto.to_dict(), 'quantidade_estoque': Estoque.query.filter_by(id_produto=produto.id).first().quantidade_produtos 
         if Estoque.query.filter_by(id_produto=produto.id).first() else 0} 
        for produto in produtos
    ])

@produtos_blueprint.route('/obter/<int:id_produto>', methods=['GET'])
def obter_produto_id(id_produto):
    produto = Produto.query.get(id_produto)
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    estoque = Estoque.query.filter_by(id_produto=id_produto).first()
    return jsonify({**produto.to_dict(), 'quantidade_estoque': estoque.quantidade_produtos if estoque else 0})

@produtos_blueprint.route('/criar_produto', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    novo_produto = Produto(**dados)
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify(novo_produto.to_dict()), 201

@produtos_blueprint.route('/atualizar/<int:id_produto>', methods=['PUT'])
def atualizar_produto(id_produto):
    produto = Produto.query.get(id_produto)
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    dados = request.get_json()
    for chave, valor in dados.items():
        setattr(produto, chave, valor)
    db.session.commit()
    return jsonify(produto.to_dict())

@produtos_blueprint.route('/deletar/<int:id_produto>', methods=['DELETE'])
def deletar_produto(id_produto):
    produto = Produto.query.get(id_produto)
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto deletado com sucesso'})

@produtos_blueprint.route('/obter/<int:id_produto>/estoque', methods=['GET'])
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