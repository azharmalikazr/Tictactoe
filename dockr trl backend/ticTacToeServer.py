from os import ftruncate
from flask import Flask, request, json
import tkinter as tk
import time
import random

from pymongo import database
from checkOne import checkOne
from myAiBot import myAiBot
from checkTwo import checkTwo
from checkRand import checkRand
import copy
from flask_cors import CORS
from checkIfWinner import checkIfWinner
from database import result

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
    output = request.get_json()
    
    #print("output", output['num1'])
    #print("output", output['num2'])
    calculator = {}

    check=output['check']
    tracker=output['tracker']
    print(check,tracker)

    newcheck = checkIfWinner(1,tracker)
    print (newcheck , "rand")
    calculator ['WinnerCheckHuman'] = newcheck
    
    if (newcheck == 9999):
        if check<10:

            if check == 1:
                newcheck=checkOne(check, tracker)
                print(newcheck,"ye 1 tha")
                calculator ['PossibleIndex'] = newcheck

            else:
                newcheck = myAiBot(check, tracker)
                
                #  print (newcheck , 'az')
                if newcheck != 22:
                    print(newcheck, "AiBot")
                    calculator ['PossibleIndex'] = newcheck

                elif check == 2:
                    newcheck =checkTwo(check, tracker)
                    print (newcheck , 2)
                    calculator ['PossibleIndex'] = newcheck

                elif check < 5:                        
                    newcheck = checkRand(tracker)
                    print (newcheck , "rand123")
                    calculator ['PossibleIndex'] = newcheck
        
        newcheck = checkIfWinner(1,tracker)
        #print (newcheck , "rand")
        calculator ['WinnerCheckComp'] = newcheck
        


 
    return calculator
    
        


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port= 9090)


    