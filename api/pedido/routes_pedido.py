

pedidos_blueprint = Blueprint('pedidos', __name__)


@pedidos_blueprint.route('/pedidos', methods=['GET'])#lista todos os pedidos

@pedidos_blueprint.route('/pedidos/<int:id_pedido>', methods=['GET'])#obtém detalhes de um pedido específico

@pedidos_blueprint.route('/pedidos', methods=['POST'])#cria um novo pedido

@pedidos_blueprint.route('/pedidos/<int:id_pedido>', methods=["PUT"])#atauliza informações de um pedido

@pedidos_blueprint.route('/pedidos/<int:id_pedido>', methods=['DELETE'])#cancela pedido