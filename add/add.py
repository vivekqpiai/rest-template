from flask import Blueprint, request, Response
import json

add_blueprint = Blueprint('add_api', __name__)

# specifying the type of request we can make
# two major ones are GET and POST
# read more https://restfulapi.net/http-methods/

@add_blueprint.route('/add', methods=["POST", "GET"])
def main_route():
  # we are sending raw json from frontend
  arguments = request.get_json()
  first_num = arguments['firstNum']
  sec_num = arguments['secNum']
  sumup = add(first_num, sec_num)
  sumObj = {
    'sum': sumup
  }
  # serializing the python object to json
  # read more @ https://realpython.com/python-json/
  json_resp = json.dumps(sumObj)
  return json_resp

def add(x, y):
  return x + y