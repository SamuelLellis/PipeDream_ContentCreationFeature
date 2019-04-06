def checkID(num):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID FROM contentcreation")

    myresult = mycursor.fetchall()

    for x in myresult:
        if x[0] == num:
            print("ID taken")
        else:
            print("ID available")

    
