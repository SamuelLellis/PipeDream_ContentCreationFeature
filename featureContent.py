import mysql.connector

def connect ():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
    )
    return mydb
mydb = connect()
mycursor = mydb.cursor()

def display():
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM contentcreation")


    myresult = mycursor.fetchall()

    print("Total number of rows in current article database:", mycursor.rowcount)

    for row in myresult:
        print("Id = ", row[0], )
        print("Content = ", row[1])
        print("Timestamp = ", row[3])


def checkID(num):
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID FROM contentcreation")

    myresult = mycursor.fetchall()

def addNew(id, content):
    mydb = connect()
    mycursor = mydb.cursor()

    sql = "INSERT INTO contentcreation (ID, Content) VALUES (%s,%s)"
    val = (id, content)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount,"record inserted")

def main():
    display()
    checkID(1)
