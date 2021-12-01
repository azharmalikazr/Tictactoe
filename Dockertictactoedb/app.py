from os import ftruncate
from flask import Flask, request, json
from pymongo import database
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app)
cors = CORS(app,resource={
    r"/*":{
        "origins" : "*"
    }
})

number = 1

@app.route("/", methods = ["POST", "GET"])
def result():

    
    output = request.get_json()
    print(output)
    dbData = []

    totalGames=output['GameNo']
    humanWon=output['Human Won']
    computerWon=output['Computer Won']
    draw=output['Draw']
    copyBoard=output['Copy Of Board']
    statusOfThisGame=output['Status of this game']
    left=output['Left']
    myclient = pymongo.MongoClient("mongodb+srv://test:asaass121122@textnews.dlpgl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = myclient["mydatabase"]
    mycol = mydb["Azhar"]
    calculator = {}
    


    for x in mycol.find():
        dbData.append(x)
    if len(dbData) is not 0 and totalGames is -1:
        calculator ['GameNo'] = len(dbData)
        calculator ['HumanWon'] = dbData[-1]["Human Won"]
        calculator ['ComputerWon'] = dbData[-1]["Computer Won"]
        calculator ['Draw'] = dbData[-1]["Draw"]
        calculator ['Left'] = dbData[-1]["Left"]
    elif totalGames is not -1:

        mydict = { "Game No": totalGames, "Human Won": humanWon,"Left": left, "Computer Won": computerWon, "Draw": draw, "Copy Of Board": copyBoard, "Status of this game": statusOfThisGame  }
        mycol.insert_one(mydict)
        dbData = []
        for x in mycol.find():
            dbData.append(x)
        calculator ['GameNo'] = dbData[-1]["Game No"]
        calculator ['HumanWon'] = dbData[-1]["Human Won"]
        calculator ['ComputerWon'] = dbData[-1]["Computer Won"]
        calculator ['Draw'] = dbData[-1]["Draw"]
        calculator ['Left'] = dbData[-1]["Left"]
    else :
        calculator ['GameNo'] = totalGames
        calculator ['HumanWon'] = humanWon
        calculator ['ComputerWon'] = computerWon
        calculator ['Draw'] = draw
        calculator ['Left'] = left
		
		
		
        
    
    return calculator
    
        


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=7070)


    