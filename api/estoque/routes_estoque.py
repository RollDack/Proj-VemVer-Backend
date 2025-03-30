

estoque_blueprint = Blueprint('estoque', __name__)


@estoque_blueprint.routes('/estoque', methods=['GET'])#lista todos os itens no estoque

@estoque_blueprint.route('/estoque/<int:id_produto>', methods=['GET'])#obtem informações de um produto especifico no estoque

@estoque_blueprint.route('/estoque', methods=['POST'])#adiciona um novo item no estoque

@estoque_blueprint.route('/estoque/<int:id_produto>', methods=['PUT'])#atualiza a quantidade de um produto no estoque

@estoque_blueprint.route('/estoque/<int:id_produto>', methods=['DELETE'])#remove um item do estoque