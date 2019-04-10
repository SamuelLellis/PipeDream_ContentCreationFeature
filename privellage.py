import mysql.connector
import json
from getter import *
from connect import connect

mydb = connect()
mycursor = mydb.cursor()

everyone = ['reader', 'contributor']
desk = ['desk editor','desk head']
copy = ['copy editor','assistant copy chief','copy chief','editor in chief']

def editCheck(id,user):
    if(role in everyone):
        if(getStage(id) == desk or getStage(id) == copy):
            return 'Cannot edit'
        elif(getAuthor(id) != user):
            return 'Cannot edit'
        else:
            return getContent(id)
    elif(role in desk):
        if(getStage(id) == copy):
            return 'Cannot edit'
        elif(getSection(id) != section):
            return 'Cannot edit'
    else:
        return getContent(id)
