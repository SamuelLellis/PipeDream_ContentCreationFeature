from flask import Flask, request, jsonify
import mysql.connector
from connect import connect
import datetime
from privellage import *

mydb = connect()
mycursor = mydb.cursor()


from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def post_request():
    now = datetime.datetime.now()
    jfile = request.get_json()
    id = jfile['id']
    content = jfile['content']
    author = jfile['author']
    mycursor.execute('''
             INSERT INTO mydatabase (id,content,author,dt)
             VALUES
             ({0},'{1}','{2}','{3}');
             '''.format(id, content, author, now))
    mydb.commit()
    return 'Successfully added contents'

@app.route('/',methods = ['GET'])
def get_request():
    id = request.args.get('id')
    mycursor.execute("select * from mydatabase where id = {0};".format(id))
    content = mycursor.fetchone()
    return jsonify({'result':content[1]})

@app.route('/', methods=['PATCH'])
def patch_request(): #currently still debugging
    id = request.args.get('id')
    mycursor.execute("select uuid,content,author,MAX(version),edits from mydatabase where id = {0};".format(id))
    print('*********************'+content)
    content = mycursor.fetchone()
    print(content)
    uuid = content[0]
    sentcontent = content[1]
    dt = datetime.datetime.now()
    author = content[2]
    version = content[3]
    version += 1
    print(version)
    edits = content[4]
    print('***************'+content)
    mycursor.execute('''
             INSERT INTO mydatabase (uuid,content,dt,author,version,edits)
             VALUES
             ('{0}','{1}','{2}','{3}',{4},'{5}');
             '''.format(uuid, sentcontent, dt,author,version,edits))
    mydb.commit()
    return 'Successfully added edits'
