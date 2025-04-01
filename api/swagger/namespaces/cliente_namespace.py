from flask_restx import Namespace, fields, Resource
from cliente.routes_cliente import listar_clientes, obter_cliente_id, criar_cliente, atualizar_cliente, deletar_cliente


cliente_ns = Namespace("cliente", description="Gerenciamento de clientes")


cliente_model = cliente_ns.model("Cliente", {
    "cpf": fields.String(required=True, description="CPF do cliente"),
    "nome": fields.String(required=True, description="Nome completo do cliente"),
    "idade": fields.Integer(required=True, description="Idade do cliente"),
    "email": fields.String(required=True, description="Email do cliente"),
    "cep": fields.String(required=True, description="CEP do cliente"),
    "telefone": fields.String(required=True, description="Telefone do cliente")
})

cliente_model = cliente_ns.model("ClienteOutput", {
    "id": fields.Integer(readonly=True, description="ID do cliente"),
    "cpf": fields.String(required=True, description="CPF do cliente"),
    "nome": fields.String(required=True, description="Nome completo do cliente"),
    "idade": fields.Integer(required=True, description="Idade do cliente"),
    "email": fields.String(required=True, description="Email do cliente"),
    "cep": fields.String(required=True, description="CEP do cliente"),
    "telefone": fields.String(required=True, description="Telefone do cliente")
})

@cliente_ns.route('/')
class ClienteList(Resource):
    @cliente_ns.marshal_with(cliente_model, as_list=True)
    def get(self):
        """Lista todos os clientes"""
        return listar_clientes()

    @cliente_ns.expect(cliente_model)
    def post(self):
        """Cria um novo cliente"""
        return criar_cliente()


@cliente_ns.route('/<int:id_cliente>')
class ClienteDetail(Resource):
    @cliente_ns.marshal_with(cliente_model)
    def get(self, id_cliente):
        """Obtém um cliente por ID"""
        return obter_cliente_id(id_cliente)

    @cliente_ns.expect(cliente_model)
    def put(self, id_cliente):
        """Atualiza um cliente por ID"""
        return atualizar_cliente(id_cliente)

    def delete(self, id_cliente):
        """Deleta um cliente por ID"""
        return deletar_cliente(id_cliente)
