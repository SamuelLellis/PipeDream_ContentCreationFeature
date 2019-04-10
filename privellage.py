import mysql.connector
from getter import *
from connect import connect

mydb = connect()
mycursor = mydb.cursor()

everyone = ['reader', 'contributor']
desk = ['desk editor','desk head']
copy = ['copy editor','assistant copy chief','copy chief','editor in chief']

def editCheck(id,role,user,section):
    if(role in everyone):
        if(getStage(id) == desk or getStage(id) == copy):
            return false
        elif(getAuthor(id) != user):
            return fasle
        else:
            return true
    elif(role in desk):
        if(getStage(id) == copy):
            return false
        elif(getSection(id) != section):
            return false
    else:
        return true
