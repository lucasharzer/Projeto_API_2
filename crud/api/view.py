from crud.api.schemas import VillainSchema
from flask_restplus import Resource, Namespace, fields
from flask import request
from crud.api.registration import Villain
import logging

log = logging.getLogger(__name__)
api = Namespace('Vilão', description='Manutenção de dados de vilões')

modelo = api.model('VillainModel', {
    'villain_id': fields.Integer,
    'nome': fields.String,
    'idade': fields.Integer,
    'criador': fields.String,
})

@api.route('/')
class VillainView(Resource):
    @api.response(200, 'Busca realizada com sucesso!')
    def get(self):
        return Villain.listar(), 200
    
    @api.expect(modelo)
    @api.expect(VillainSchema(), validate=True)
    def post(self):
        return Villain.cadastrar(request.json), 201

@api.route('/<villain_id>')
class VilãoIdView(Resource):
    @api.response(200, 'Busca realizada com sucesso!')
    def get(self, villain_id:int):
        return Villain.listar(int(villain_id)), 200

    @api.response(200, 'Busca realizada com sucesso!')
    @api.param('nome', 'Nome do Vilão')
    @api.param('idade', 'idade do Vilão')
    @api.param('criador', 'Criador do Vilão')
    def put(self, villain_id:int):
        return Villain.atualizar(int(villain_id), request.json), 201

    def delete(self, villain_id:int):
        return Villain.deletar(int(villain_id)), 200