from app.models.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class Response(BaseModel):

    __tablename__ = 'response'

    idresponse = Column(Integer, primary_key = True)
    message = Column(String)

    def __init__(self, idresponse, message):
        self.idresponse = idresponse
        self.message = message