from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from config import db
from funcionario.model_funcionario import Funcionario

funcinario_blueprint = Blueprint('funcionarios', __name__)

@funcinario_blueprint.route('/', methods=['GET']) 
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([func.to_dict() for func in funcionarios])

@funcinario_blueprint.route('/obter/<int:id_funcionario>', methods=['GET']) 
def obter_funcionario_id(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    return jsonify(funcionario.to_dict()) if funcionario else (jsonify({'erro': 'Funcionário não encontrado'}), 404)


@funcinario_blueprint.route('/criar_funcionario', methods=['POST']) 
def criar_funcionario():
    dados = request.get_json()
    novo_funcionario = Funcionario(**dados)
    db.session.add(novo_funcionario)
    db.session.commit()
    return jsonify(novo_funcionario.to_dict()), 201

@funcinario_blueprint.route('/atualizar/<int:id_funcionario>', methods=['PUT'])
def atualizar_funcionario(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    if not funcionario:
        return jsonify({'erro': 'Funcionário não encontrado'}), 404
    dados = request.get_json()
    for chave, valor in dados.items():
        setattr(funcionario, chave, valor)
    db.session.commit()
    return jsonify(funcionario.to_dict())


@funcinario_blueprint.route('/deletar/<int:id_funcionario>', methods=['DELETE'])
def deletar_funcionario(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    if not funcionario:
        return jsonify({'erro': 'Funcionário não encontrado'}), 404
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({'mensagem': 'Funcionário deletado com sucesso'})