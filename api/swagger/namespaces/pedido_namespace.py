from flask_restx import Namespace, Resource, fields
from pedido.routes_pedido import listar_pedidos,obter_pedido_id,criar_pedido,atualizar_pedido,cancelar_pedido



pedido_ns = Namespace("pedido", description="Gerenciamento de pedidos")


pedido_model = pedido_ns.model("Pedido", {
    "id_cliente": fields.Integer(required=True, description="ID do cliente relacionado ao pedido"),
    "id_produto": fields.Integer(required=True, description="ID do produto relacionado ao pedido"),
})


pedido_model = pedido_ns.model("PedidoOutput", {
    "id": fields.Integer(readonly=True, description="ID do pedido"),
    "id_cliente": fields.Integer(required=True, description="ID do cliente relacionado ao pedido"),
    "id_produto": fields.Integer(required=True, description="ID do produto relacionado ao pedido"),
    "valor_total": fields.Float(readonly=True, description="Valor total do pedido"),
    "data_pedido": fields.String(required=True, description="Data do pedido no formato AAAA-MM-DD")
})

@pedido_ns.route('/')
class PedidoList(Resource):
    @pedido_ns.marshal_with(pedido_model, as_list=True)
    def get(self):
        """Lista todos os pedidos"""
        return listar_pedidos()

    @pedido_ns.expect(pedido_model)
    def post(self):
        """Cria um novo pedido"""
        return criar_pedido()


@pedido_ns.route('/<int:id_pedido>')
class PedidoDetail(Resource):
    @pedido_ns.marshal_with(pedido_model)
    def get(self, id_pedido):
        """Obtém um pedido por ID"""
        return obter_pedido_id(id_pedido)

    @pedido_ns.expect(pedido_model)
    def put(self, id_pedido):
        """Atualiza um pedido por ID"""
        return atualizar_pedido(id_pedido)

    def delete(self, id_pedido):
        """Cancela um pedido por ID"""
        return cancelar_pedido(id_pedido)
