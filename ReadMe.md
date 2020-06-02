# Python Flask Template

## Running Project

1. Clone the project locally

    ```
    git clone https://github.com/vivekqpiai/rest-template.git
    ```
2. Install dependencies (flask)
    ```
    pip install flask (windows)
    pip3 install flask (macOS)
    ```

3. goto directory and run the rest.py file

    ```
    cd rest-template
    python rest.py (windows)
    python3 rest.py (macOS)
    ```

## Explanation


rest.py is the root file that starts the server.

We need to create an instance of `Flask` to be able to define the routes.

```python
from flask import Flask,
app = Flask(__name__)
```

To define the route we use that instance `app` and define the function that needs to be called when a request comes to that route (aka endpoint)

```python
@app.route('/')
def function():
    return 'Welcome to flask template'
```

* Reading request data
  
  There are different ways to read request data based on how it is sent.

  1. `GET` Request - in this case we pass the arguements as _query strings_

      ```python
      # http://127.0.0.1:5002/sub?firstNum=10
        arguments = request.args
        first_num = arguments.get('firstNum', default=0, type=int)
      ```
  2. `POST` Request - we can get data in different ways (JSON, form, url-encoded-form, etc). JSON is one of the common ways to send/rcv the data

      ```python
              arguments = request.get_json()
              first_num = arguments['firstNum']
              sec_num = arguments['secNum']
      ```

* Sending response (JSON) - after performing various operations by using the request data, we need to return the response back to client (front-end). To do that we need to create a dictionary that stores the response and then serialize it to json.


    ```python
        sumObj = {
          'sum': sumup
        }
        # serializing the python object to json
        # read more @ https://realpython.com/python-json/
        json_resp = json.dumps(sumObj)
        return json_resp
    ```
    read more at [Python JSON](https://realpython.com/python-json "Realpython JSON Guide")

___

Additional resources

[Flask Blueprints](https://realpython.com/flask-blueprint  "Flask Blueprints")

[Flask OSS](https://flask.palletsprojects.com/en/1.1.x/  "Flask OSS")

[Understanding HTTP methods - GET POST etc](https://restfulapi.net/http-methods  "Understanding HTTP methods")