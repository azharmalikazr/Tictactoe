from flask import Flask,request,json
import tkinter as tk
import time
import pymongo

from bson import json_util , ObjectId





def result():
   
    myclient = pymongo.MongoClient("mongodb+srv://test:asaass121122@textnews.dlpgl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = myclient["new"]
    mycol = mydb["new 2"]
    mylist = [{ "Title": 12, "Text": 34, "Author": 56, "Summary": 77}]
    x = mycol.insert_many(mylist)
    print(x)