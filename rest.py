from flask import Flask, request, Response
import json

from add.add import add_blueprint
from divide_rest import divide_blueprint
from subtract import sub

app = Flask(__name__)
app.register_blueprint(add_blueprint, url_prefix='/calculator')
app.register_blueprint(divide_blueprint, url_prefix='/calculator')


@app.route('/')
def index():
  return 'hello'

@app.route('/sub')
def subtract():
  arguments = request.args
  first_num = arguments.get('firstNum', default=0, type=int)
  sec_num = arguments.get('secNum', default=0, type=int)
  result = sub(first_num, sec_num)
  resultObj = {
    'result': result
  }
  json_resp = json.dumps(resultObj)
  return json_resp



if __name__ == '__main__':
  app.run(debug=True, port=5002)