from app.config.constants import ROW_BREAK
from assistant_fulfillment_helper import FulfillmentHelperResponse
from app.config.database import db
from app.models.pedido_model import Pedido

class PedidosController:

    def ver_pedido(data):
        id_pedido = data['parameters'].get('id_pedido')
        user_id = data['parameters'].get('user_id')

        pedido = db.get(Pedido, id_pedido)
        if pedido and pedido.idcliente == user_id:
            message_str = f"Informações do Pedido <b>{id_pedido}</b>:{ROW_BREAK}{ROW_BREAK}"
            message_str = f"{message_str}{ROW_BREAK}- <b>Produto</b>: {pedido.produto}"
            message_str = f"{message_str}{ROW_BREAK}- <b>Quantidade</b>: {pedido.quantidade}"
        else :
            message_str = "Não encontrei nenhum pedido em aberto com o ID informado."

        return FulfillmentHelperResponse(
            message=message_str,
            jump_to='Pedido'
        )

    def novo_pedido(data):

        produto = data['parameters'].get('nome_produto')
        quantidade = data['parameters'].get('quantidade_produto')
        user_id = data['parameters'].get('user_id')

        db.add(Pedido(
            produto = produto,
            quantidade = quantidade,
            idcliente = user_id
        ))
        db.commit()

        return FulfillmentHelperResponse(
            message="Ok, seu pedido foi adicionado!",
            jump_to="Pedido"
        )

    def cancelar_pedido(data):
        id_pedido = data['parameters'].get('id_pedido')
        user_id = data['parameters'].get('user_id')

        pedido = db.get(Pedido, id_pedido)
        if pedido and pedido.idcliente == user_id:
            db.delete(pedido)
            db.commit()
            message_str = f"Certo, o pedido {id_pedido} foi cancelado."
        else :
            message_str = "Não encontrei nenhum pedido em aberto com o ID informado."

        return FulfillmentHelperResponse(
            message=message_str,
            jump_to='Pedido'
        )

    def listar_pedidos(data):
        id_user = data['parameters'].get('user_id')
        pedidos_str = ''
        pedidos_list = db.query(Pedido).filter(
            Pedido.idcliente==id_user
        )

        for pedido in pedidos_list:
            pedidos_str = pedidos_str + ROW_BREAK
            pedidos_str = pedidos_str + f"<b>ID: {pedido.idpedido}</b> - {pedido.produto} - Qtd: {pedido.quantidade}"

        if pedidos_str == '':
            message_ret = 'Parece que você não tem nenhum pedido em aberto'
        else:
            message_ret = f"Aqui estão seus pedidos:{ROW_BREAK}{pedidos_str}"

        return FulfillmentHelperResponse(
            message=message_ret,
            jump_to='Pedido'
        )

        