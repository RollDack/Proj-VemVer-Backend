from swagger.swagger_config import configure_swagger
from config import app,db
from cliente.routes_cliente import cliente_blueprint
from funcionario.routes_funcionario import funcinario_blueprint
from pedido.routes_pedido import pedidos_blueprint
from produto.routes_produto import produtos_blueprint

configure_swagger(app)

with app.app_context():
    db.create_all()

app.register_blueprint(cliente_blueprint, url_prefix='/clientes')
app.register_blueprint(funcinario_blueprint, url_prefix='/funcionarios')
app.register_blueprint(pedidos_blueprint, url_prefix='/pedidos')
app.register_blueprint(produtos_blueprint, url_prefix='/produtos')


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )

#print(app.url_map)