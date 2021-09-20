import logging
import os
from jsonschema import FormatChecker

from flask_restplus import Api as ApiVillain
from werkzeug.exceptions import HTTPException


log = logging.getLogger(__name__)
comando = os.popen('git log | head -n 1')
commit = comando.read().replace("commit", "")

api = ApiVillain(version=f'0.1#{commit}', default="", doc="/inimigos", title='Projeto Api de Vilões', description='Api Python Flask com Swagger', format = FormatChecker())

@api.errorhandler
def default_error_hajndler(e):
  if isinstance(e, HTTPException):
    response = {"message": e.description}
    status_code = e.code
  else:
    response = {"message": "Unhandled Exception"}
    status_code = 500

  log.exception(e)
  return response, status_code 
