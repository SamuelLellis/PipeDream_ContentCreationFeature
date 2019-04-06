import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "mydatabase"
)

mycursor = mydb.cursor()

def display():
    mycursor.execute("SELECT * FROM contentcreation")


    myresult = mycursor.fetchall()

    print("Total number of rows in current article database:", mycursor.rowcount)
    print()
    for row in myresult:
        print("Id = ", row[0], )
        print("Content = ", row[1])
        print()
        
def checkID(num):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID FROM contentcreation")

    myresult = mycursor.fetchall()

    
def delete(num):
#this doesn't quite work yet

    sql = "DELETE FROM contentcreation WHERE ID == num"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
    

def addNew(id, content):

    sql = "INSERT INTO contentcreation (ID, Content) VALUES (%s,%s)"
    val = (id, content)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount,"record inserted")

def main():
    display()
    #delete(1)
    



main()
#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
   # print(x)
