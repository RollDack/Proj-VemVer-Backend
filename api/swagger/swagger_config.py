from . import api
from swagger.namespaces.produto_namespace import produto_ns
from swagger.namespaces.pedido_namespace import pedido_ns
from swagger.namespaces.funcionario_namespace import funcionario_ns
from swagger.namespaces.cliente_namespace import cliente_ns

def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(produto_ns, path="/produto")
    api.add_namespace(pedido_ns, path="/pedido")
    api.add_namespace(funcionario_ns, path="/funcionario")
    api.add_namespace(cliente_ns, path="/cliente")
    api.mask_swagger = False