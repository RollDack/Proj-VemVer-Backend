from flask import Blueprint, request, jsonify
from config import db
from model_funcionario import Funcionario

funcinario_blueprint = Blueprint('funcionarios', __name__)

@funcinario_blueprint.route('/funcionarios', methods=['GET']) #lista todos os funcionarios
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([func.to_dict() for func in funcionarios])

@funcinario_blueprint.route('/funcionarios/<int:id_funcionario>', methods=['GET']) #obtém informações de um funcionario específico
def obter_funcionario(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    return jsonify(funcionario.to_dict()) if funcionario else (jsonify({'erro': 'Funcionário não encontrado'}), 404)


@funcinario_blueprint.route('/funcionarios', methods=['POST']) #adiciona um novo funcionario
def criar_funcionario():
    dados = request.get_json()
    novo_funcionario = Funcionario(**dados)
    db.session.add(novo_funcionario)
    db.session.commit()
    return jsonify(novo_funcionario.to_dict()), 201

@funcinario_blueprint.route('/funcionarios/<int:id_funcionario>', methods=['PUT'])#atualiza informações de um funcionário
def atualizar_funcionario(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    if not funcionario:
        return jsonify({'erro': 'Funcionário não encontrado'}), 404
    dados = request.get_json()
    for chave, valor in dados.items():
        setattr(funcionario, chave, valor)
    db.session.commit()
    return jsonify(funcionario.to_dict())


@funcinario_blueprint.route('/funcionarios/<int:id_funcionario>', methods=['DELETE'])#deleta um funcionario
def deletar_funcionario(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    if not funcionario:
        return jsonify({'erro': 'Funcionário não encontrado'}), 404
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({'mensagem': 'Funcionário deletado com sucesso'})