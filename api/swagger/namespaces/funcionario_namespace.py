from flask_restx import Namespace, Resource, fields
from funcionario.routes_funcionario import listar_funcionarios,obter_funcionario_id,criar_funcionario,atualizar_funcionario,deletar_funcionario



funcionario_ns = Namespace("funcionario", description="Gerenciamento de funcionários")


funcionario_model = funcionario_ns.model("Funcionario", {
    "cpf": fields.String(required=True, description="CPF do funcionário"),
    "nome": fields.String(required=True, description="Nome completo do funcionário"),
    "idade": fields.Integer(required=True, description="Idade do funcionário"),
    "email": fields.String(required=True, description="Email do funcionário"),
    "cep": fields.String(required=True, description="CEP do funcionário"),
    "telefone": fields.String(required=True, description="Telefone do funcionário"),
    "salario": fields.Float(required=True, description="Salário do funcionário")
})


funcionario_model = funcionario_ns.model("FuncionarioOutput", {
    "id": fields.Integer(readonly=True, description="ID do funcionário"),
    "cpf": fields.String(required=True, description="CPF do funcionário"),
    "nome": fields.String(required=True, description="Nome completo do funcionário"),
    "idade": fields.Integer(required=True, description="Idade do funcionário"),
    "email": fields.String(required=True, description="Email do funcionário"),
    "cep": fields.String(required=True, description="CEP do funcionário"),
    "telefone": fields.String(required=True, description="Telefone do funcionário"),
    "salario": fields.Float(required=True, description="Salário do funcionário")
})

@funcionario_ns.route('/')
class FuncionarioList(Resource):
    @funcionario_ns.marshal_with(funcionario_model, as_list=True)
    def get(self):
        """Lista todos os funcionários"""
        return listar_funcionarios()

    @funcionario_ns.expect(funcionario_model)
    def post(self):
        """Cria um novo Funcionário"""
        return criar_funcionario()


@funcionario_ns.route('/<int:id_funcionario>')
class FuncionarioDetail(Resource):
    @funcionario_ns.marshal_with(funcionario_model)
    def get(self, id_funcionario):
        """Obtém um funcionário por ID"""
        return obter_funcionario_id(id_funcionario)

    @funcionario_ns.expect(funcionario_model)
    def put(self, id_funcionario):
        """Atualiza um funcionário por ID"""
        return atualizar_funcionario(id_funcionario)

    def delete(self, id_funcionario):
        """Deleta um funcionário por ID"""
        return deletar_funcionario(id_funcionario)
