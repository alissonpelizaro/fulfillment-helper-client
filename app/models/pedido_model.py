from app.models.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class Pedido(BaseModel):

    __tablename__ = 'pedido'

    idpedido = Column(Integer, primary_key = True)
    produto = Column(String)
    quantidade = Column(Integer)
    idcliente = Column(String)

    def __init__(self, **kargs):
        self.idpedido = kargs.get('idpedido')
        self.produto = kargs.get('produto')
        self.quantidade = kargs.get('quantidade')
        self.idcliente = kargs.get('idcliente')