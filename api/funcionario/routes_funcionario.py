

funcinario_blueprint = Blueprint('funcionarios', __name__)

@funcinario_blueprint.route('/funcionarios', methods=['GET']) #lista todos os funcionarios

@funcinario_blueprint.route('/funcionarios/<int:id_funcionario>', methods=['GET']) #obtém informações de um funcionario específico

@funcinario_blueprint.route('/funcionarios', methods=['POST']) #adiciona um novo funcionario

@funcinario_blueprint.route('/funcionarios/<int:id_funcionario>', methods=['PUT'])#atualiza informações de um funcionário

@funcinario_blueprint.route('/funcionarios/<int:id_funcionario>', methods=['DELETE'])#deleta um funcionario