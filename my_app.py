import os
from assistant_fulfillment_helper import FulfillmentHelper, FulfillmentHelperResponse
from app.controllers.pedidos import PedidosController
from dotenv import load_dotenv

load_dotenv()

fh = FulfillmentHelper()

fh.registerIntent(
    callback=PedidosController.listar_pedidos,
    webhook_token=os.getenv('WH_PEDIDOS_VER_PEDIDOS'),
    node_name="Pedido - Ver pedidos"
)

fh.registerIntent(
    callback=PedidosController.cancelar_pedido,
    webhook_token=os.getenv('WH_PEDIDOS_CANCELAR_PEDIDO'),
    node_name="Pedido - Cancelar Pedido"
)

fh.registerIntent(
    callback=PedidosController.novo_pedido,
    webhook_token=os.getenv('WH_PEDIDOS_NOVO_PEDIDO'),
    node_name="Pedido - Novo pedido"
)

fh.registerIntent(
    callback=PedidosController.ver_pedido,
    webhook_token=os.getenv('WH_PEDIDOS_VER_PEDIDO'),
    node_name="Pedido - Ver pedido"
)

fh.start(
    debug=True
)