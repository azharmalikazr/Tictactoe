import random
from flask import Flask, request, json
import tkinter as tk
import time
import random




def checkOne(check, tracker):
    possibleMove=[]
    isMoved = False
    if tracker[4] == None:
        tracker[4] = 'X'
        isMoved = True
        
        return 4

    else:
        for zer in range(0,9, 2):
            if tracker[zer] == None:
                possibleMove.append(zer)
                #print(zer)

                
        # print(tracker)
        # print(possibleMove)


        while isMoved == False:
            possibleMoveIndex = random.randint(0, 3)
            if tracker[possibleMove[possibleMoveIndex]] == None:
                # print( possibleMoveIndex)
                # print( possibleMove[possibleMoveIndex])
                isMoved=True
                return possibleMove[possibleMoveIndex]
                
    
