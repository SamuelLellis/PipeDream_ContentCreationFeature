import mysql.connector
from connect import connect

mydb = connect()
mycursor = mydb.cursor()

def displayAll(id,role):
    mydb = connect()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM contentcreation")

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

def main():
    display()
    checkID(1)
