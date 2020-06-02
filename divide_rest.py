from flask import Blueprint, request, Response
from divide.divide import divide
import json

divide_blueprint = Blueprint('divide_api', __name__)

@divide_blueprint.route('/divide', methods=["POST", "GET"])
def main_route():
  # we are sending raw json from frontend
  arguments = request.get_json()
  first_num = arguments['firstNum']
  sec_num = arguments['secNum']
  result = divide(first_num, sec_num)
  resultObj = {
    'result': result
  }
  json_resp = json.dumps(resultObj)
  return json_resp