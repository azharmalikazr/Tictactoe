from flask import Flask, request, json
import tkinter as tk
import time
import random




def checkRand( tracker):

    isMoved = False
    if (tracker[7] == None):
        tracker[7] = 'X'
        isMoved = True
        return 7


    
    while isMoved == False:
        possibleMoveIndex = random.randint(0, 8)
        #print(possibleMoveIndex , "ye lo")
        if tracker[possibleMoveIndex] == None:
            tracker[possibleMoveIndex] = 'X'
            isMoved = True
            return possibleMoveIndex

    return 22
