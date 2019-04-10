import mysql.connector

mydb = connect()
mycursor = mydb.cursor()
roles = {
'0':'Everyone',
'1':'Reader',
'2':'Contributor',
'3':'Desk',
'4':'Desk Editor',
'5':'Desk Head',
'6':'Copy',
'7':'Assistant Copy Chief',
'8':'Copy Chief',
'9':'Editor in Chief'
}
def checkPriv(userRole, id):
    if(userRole == roles[1]):
        return  
