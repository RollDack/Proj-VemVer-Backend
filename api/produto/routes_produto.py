

produtos_blueprint = Blueprint('produtos', __name__)


@produtos_blueprint.route('/produtos', methods=['GET'])#lista todos os produtos

@produtos_blueprint.route('/produtos/<int:id_produto>', methods=['GET'])#obtem detalhes de um produto especifico

@produtos_blueprint.route('/produtos', methods=['POST'])#adiciona um novo produto

@produtos_blueprint.route('/produtos/<int:id_produto>', methods=['PUT'])#atualiza informações de um produto

@produtos_blueprint.route('/produtos/<int:id_produto>', methods=['DELETE'])#remove um produto

@produtos_blueprint.route('/produtos/<int:id_produto>/estoque', methods=['GET'])#obtém a quantidade disponivel do produto no estoque