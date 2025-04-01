from flask_restx import Namespace, Resource, fields
from estoque.routes_estoque import atualizar_estoque

estoque_ns = Namespace("estoque", description="Gerenciamento de estoque")


estoque_model = estoque_ns.model("Estoque", {
    "id_produto": fields.Integer(readonly=True, description="ID do produto relacionado"),
})

estoque_model = estoque_ns.model("EstoqueOutput", {
    "id_produto": fields.Integer(readonly=True, description="ID do produto relacionado"),
    "nome": fields.String(readonly=True, description="Nome do produto"),
    "tipo": fields.String(readonly=True, description="Tipo do produto"),
    "preco": fields.Float(readonly=True, description="Preço do produto"),
    "quantidade_produtos": fields.Integer(readonly=True, description="Quantidade em estoque")
})

@estoque_ns.route('/<int:id_produto>')
class EstoqueDetail(Resource):
    @estoque_ns.expect(estoque_model)
    def put(self, id_produto):
        """Atualiza a quantidade em estoque de um produto por ID"""
        return atualizar_estoque(id_produto)


