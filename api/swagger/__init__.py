from flask_restx import Api

api = Api(
    version='1.0',
    title='API de uma loja de ótica',
    description='Documentação da API para Cliente, Estoque, Funcionário, Pedido e Produto',
    doc='/docs',
    mask_swagger=False,
    prefix='/api'
)