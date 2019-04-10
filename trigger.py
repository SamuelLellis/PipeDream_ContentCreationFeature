import mysql.connector
from connect import connect
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "mydatabase"
)

mycursor = mydb.cursor()


def displayAll():
    mydb = connect()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT *  FROM contentcreation")

    myresult = mycursor.fetchall()

    print("Total number of rows in current article database:", mycursor.rowcount)
    print()
    for row in myresult:
        print("Id = ", row[0], )
        print("Content = ", row[1])
        print()

def insert(num, content):
    mydb = connect()
    mycursor = mydb.cursor()

    CREATE TRIGGER record BEFORE INSERT ON contentcreation FOR EACH ROW
    sql = "INSERT INTO contentcreation (ID, Content) VALUES (%s,%s)"
    val = (id, content)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount,"record inserted")

def insertRecords(num, content)
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "INSERT INTO contentcreation (ID, Content) VALUES (%s,%s)"
    val = (id, content)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount,"history updated")

def main():
    displayAll()

main()
