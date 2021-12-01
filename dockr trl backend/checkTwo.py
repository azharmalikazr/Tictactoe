import random
from flask import Flask, request, json
import tkinter as tk
import time
import random




def checkTwo(check, tracker):
    if tracker[4] == '✓'and tracker[8] == '✓' :
        print("hello")
    possibleMove=[]
    isMoved = False

    if (tracker[1] and tracker[3] == '✓'):
        tracker[0] = 'X'
        return 0
    elif (tracker[1] and tracker[5] == '✓'):
        tracker[2] = 'X'
        return 2
    elif tracker[3] and tracker[7] == '✓':
        tracker[6] = 'X'
        return 6

    elif tracker[5] and tracker[7] == '✓':
        tracker[8] = 'X'
        return 8

    elif (tracker[0] and tracker[4] == '✓'
          or tracker[2] and tracker[4] == '✓'
          or tracker[6] and tracker[4] == '✓'
          or tracker[8] and tracker[4] == '✓'):
        #print("hello1")

        for zer in range(0, 9, 2):
            if tracker[zer] == None:
                possibleMove.append(zer)
        #print (possibleMove , "Possible Move For two")
        while isMoved == False:
            possibleMoveIndex = random.randint(0, 1)
            #print(possibleMoveIndex)
            if (tracker[possibleMove[possibleMoveIndex]] == None):
                tracker[possibleMove[possibleMoveIndex]] = 'X'
                isMoved = True
        return possibleMove[possibleMoveIndex]
    else:

        while isMoved == False:
            possibleMoveIndex = random.randint(0, 8)
            #print(possibleMoveIndex , "ye lo")
            if tracker[possibleMoveIndex] == None:
                tracker[possibleMoveIndex] = 'X'
                isMoved = True
                return possibleMoveIndex
        
        return possibleMove[possibleMoveIndex]
