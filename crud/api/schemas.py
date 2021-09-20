from marshmallow import Schema, fields

class VillainSchema(Schema):
    villain_id = fields.Integer(description="Id do Vilão", required=True)
    nome = fields.String(description="Nome do Vilão", required=True)
    idade = fields.Integer(description="Idade do Vilão", required=True)
    criador = fields.String(description="Criador do Vilão", required=True)
