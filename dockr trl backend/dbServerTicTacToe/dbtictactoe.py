from os import ftruncate
from flask import Flask, request, json


from pymongo import database

import copy
from flask_cors import CORS


import pymongo


app = Flask(__name__)
CORS(app)
cors = CORS(app,resource={
    r"/*":{
        "origins" : "*"
    }
})
@app.route("/findMove", methods=["POST", "GET"])
def findMove():
    print(123)
    output = request.json
    print(output)
    # check=output['check']
    # tracker=output['tracker']
    # print(tracker)
    # print(check)
    calculator = {}
    calculator ['PossibleIndex : 1 '] = 1
    calculator ['PossibleIndex : 2 '] = 2
    calculator ['PossibleIndex : 3 '] = 3
    calculator ['PossibleIndex : 4 '] = 4
    calculator ['PossibleIndex : 5 '] = 5
    calculator ['PossibleIndex : 6 '] = 6


        


 
    return json.dumps(calculator)

    
        


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)


    