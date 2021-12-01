from flask import Flask, request, json
import tkinter as tk
import time
import random
import checkOne
import myAiBot
import checkTwo
import checkRand
import checkIfWinner




def checkIfWinner(check, tracker):
    if check == 17:
        if (tracker[0] == tracker[1] and tracker[0] == tracker[2] and tracker[0] is not None
            or tracker[3] == tracker[4] and tracker[3] == tracker[5] and tracker[3] is not None
            or tracker[6] == tracker[7] and tracker[6] == tracker[8] and tracker[6] is not None
            or tracker[0] == tracker[3] and tracker[0] == tracker[6] and tracker[0] is not None
            or tracker[1] == tracker[4] and tracker[1] == tracker[7] and tracker[1] is not None
            or tracker[2] == tracker[5] and tracker[2] == tracker[8] and tracker[2] is not None
            or tracker[0] == tracker[4] and tracker[0] == tracker[8] and tracker[0] is not None
            or tracker[2] == tracker[4] and tracker[2] == tracker[6] and tracker[2] is not None):
            return 1
    else:
        if (tracker[0] == tracker[1] and tracker[0] == tracker[2] and tracker[0] is not None
            or tracker[3] == tracker[4] and tracker[3] == tracker[5] and tracker[3] is not None
            or tracker[6] == tracker[7] and tracker[6] == tracker[8] and tracker[6] is not None
            or tracker[0] == tracker[3] and tracker[0] == tracker[6] and tracker[0] is not None
            or tracker[1] == tracker[4] and tracker[1] == tracker[7] and tracker[1] is not None
            or tracker[2] == tracker[5] and tracker[2] == tracker[8] and tracker[2] is not None
            or tracker[0] == tracker[4] and tracker[0] == tracker[8] and tracker[0] is not None
            or tracker[2] == tracker[4] and tracker[2] == tracker[6] and tracker[2] is not None):
            return 99
        elif (tracker[0] is not None and tracker[1] is not None
              and tracker[2] is not None
              and tracker[3] is not None
              and tracker[4] is not None
              and tracker[5] is not None
              and tracker[6] is not None
              and tracker[7] is not None
              and tracker[8] is not None):
            return 999
        return 9999