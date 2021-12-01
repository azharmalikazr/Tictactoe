from flask import Flask, request, json
import tkinter as tk
import time
import random
from checkIfWinner import checkIfWinner
import copy



def myAiBot(check, tracker):
    possibleMove = []
    isMoved = False

    for i in range(9):

        if tracker[i] == None:
            possibleMove.append(i)

    #print(possibleMove)

    for j in range(len(possibleMove)):

        copytracker= copy.deepcopy(tracker)
        # print(tracker)
        # print(copytracker)
        copytracker[possibleMove[j]] = 'X'
        if checkIfWinner(17, copytracker) == 1:
            tracker[possibleMove[j]] = 'X'
            isMoved = True
            #print (tracker ,possibleMove[j] , j)
            return possibleMove[j]
        copytracker[possibleMove[j]] = None

    for k in range(len(possibleMove)):
        copytracker=copy.deepcopy(tracker)
        copytracker[possibleMove[k]] = '✓'
        if checkIfWinner(17, copytracker) == 1:
            tracker[possibleMove[k]] = 'X'
            #print (tracker , possibleMove[k] , k)
            return possibleMove[k]

        #copytracker[possibleMove[k]] = None

    return 22