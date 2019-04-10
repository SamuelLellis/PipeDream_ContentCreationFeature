import mysql.connector
from connect import connect

mydb = connect()
mycursor = mydb.cursor()

def getContent(id):
    mycursor.execute("select * from mydatabase")
    records = mycursor.fetchall()
    for row in records:
        if(row[0] == id):
            content = row[1]
            break
    return content

def getAuthor(id):
    mycursor.execute("select * from mydatabase")
    records = mycursor.fetchall()
    for row in records:
        if(row[0] == id):
            author = row[4]
            break
    return author

def getDT(id):
    mycursor.execute("select * from mydatabase")
    records = mycursor.fetchall()
    for row in records:
        if(row[0] == id):
            dt = row[2]
            break
    return dt

def getState(id):
    mycursor.execute("select * from mydatabase")
    records = mycursor.fetchall()
    for row in records:
        if(row[0] == id):
            state = row[4]
            break
    return state
def getSection(id):
    mycursor.execute("select * from mydatabase")
    records = mycursor.fetchall()
    for row in records:
        if(row[0] == id):
            state = row[5]
            break
    return state
