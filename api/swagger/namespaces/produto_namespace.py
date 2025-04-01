from flask_restx import Namespace, fields, Resource
from produto.model_produto import Produto
from estoque.model_estoque import Estoque
from produto.routes_produto import listar_produtos, obter_produto_id, criar_produto, atualizar_produto, deletar_produto, obter_estoque_produto


produto_ns = Namespace('produtos', description='Operações relacionadas a produtos')

produto_model = produto_ns.model('Produto', {
    'nome': fields.String(required=True, description='Nome do produto'),
    'tipo': fields.String(required=True, description='Tipo do produto'),
    'preco': fields.Float(required=True, description='Preço do produto')
})


produto_model = produto_ns.model("ProdutoOutput", {
    "id": fields.Integer(readonly=True, description="ID do produto"),
    "nome": fields.String(required=True, description="Nome do produto"),
    "tipo": fields.String(required=True, description="Tipo do produto"),
    "preco": fields.Float(required=True, description="Preço do produto"),
    "quantidade_produtos": fields.Integer(readonly=True, description="Quantidade em estoque")
})

@produto_ns.route('/')
class ProdutoList(Resource):
    @produto_ns.marshal_with(produto_model, as_list=True)
    def get(self):
        """Lista todos os produtos"""
        return listar_produtos()

    @produto_ns.expect(produto_model)
    def post(self):
        """Cria um novo produto"""
        return criar_produto()


@produto_ns.route('/<int:id_produto>')
class ProdutoDetail(Resource):
    @produto_ns.marshal_with(produto_model)
    def get(self, id_produto):
        """Obtém um produto pelo ID"""
        return obter_produto_id(id_produto)

    @produto_ns.expect(produto_model)
    def put(self, id_produto):
        """Atualiza um produto pelo ID"""
        return atualizar_produto(id_produto)

    def delete(self, id_produto):
        """Exclui um produto pelo ID"""
        return deletar_produto(id_produto)


@produto_ns.route('/<int:id_produto>/estoque')
class ProdutoEstoque(Resource):
    def get(self, id_produto):
        """Obtém a quantidade do produto em estoque pelo id"""
        return obter_estoque_produto(id_produto)

