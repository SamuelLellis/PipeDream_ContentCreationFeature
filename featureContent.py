import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "mydatabase"
)


mycursor = mydb.cursor()

def display():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "mydatabase"
)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM contentcreation")


    myresult = mycursor.fetchall()

    print("Total number of rows in current article database:", mycursor.rowcount)

    for row in myresult:
        print("Id = ", row[0], )
        print("Content = ", row[1])
        print("Timestamp = ", row[3])


def checkID(num):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "mydatabase"
)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID FROM contentcreation")

    myresult = mycursor.fetchall()

    

    
            
    

def addNew(id, content):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "mydatabase"
)
    mycursor = mydb.cursor()

    sql = "INSERT INTO contentcreation (ID, Content) VALUES (%s,%s)"
    val = (id, content)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount,"record inserted")

def main():
    display()
    checkID(1)



main()
#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
   # print(x)
