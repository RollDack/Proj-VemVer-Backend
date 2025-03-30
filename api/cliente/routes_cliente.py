from flask import Blueprint, request, jsonify
from config import db
from model_cliente import Cliente

cliente_blueprint = Blueprint('clientes', __name__)

@cliente_blueprint.route("/clientes", methods=['GET']) #lista todos os clientes

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['GET']) #obtém detalhes de um cliente específico

@cliente_blueprint.route('/clientes', methods=['POST']) #cria um novo cliente

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['PUT']) #atualiza informações de um cliente

@cliente_blueprint.route('/clientes/<id:id_cliente>', methods=['DELETE']) #remove um cliente

@cliente_blueprint.route('/clientes/<int:id_cliente>/pedidos', methods=['GET']) #lista todos os pedidos de um cliente