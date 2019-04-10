import mysql.connector
from connect import connect
<<<<<<< HEAD

def displayAll(id,role):
=======
from getter import *
mydb = connect()
mycursor = mydb.cursor()


def displayAll():
>>>>>>> bcf29695352585925fe13bb2ba8f4f55b26d1289
    mydb = connect()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM mydatabase")

    myresult = mycursor.fetchall()

    print("Total number of rows in current article database:", mycursor.rowcount)

    for row in myresult:
        print("Content = ", row[1])

def checkID(num):
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID FROM contentcreation")
    myresult = mycursor.fetchall()

def addNew(id, content):
    mydb = connect()
    mycursor = mydb.cursor()

    foo = open(content)
    data = foo.read()
    fdata = json.loads(data)
    dataString = json.dumps(fdata)
    foo.close()

    sql = "INSERT INTO contentcreation (ID, Content) VALUES (%d,%s)"
    val = (id, dataSring)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount,"record inserted")
<<<<<<< HEAD

print('this works')
addNew(1, 'content')
display()
checkID(1)
=======
>>>>>>> bcf29695352585925fe13bb2ba8f4f55b26d1289
