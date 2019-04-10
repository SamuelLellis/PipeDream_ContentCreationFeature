from flask import Flask, request, jsonify
import mysql.connector
from connect import connect
import datetime

mydb = connect()
mycursor = mydb.cursor()


from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
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

@app.route('/',methods=['GET'])
def get_request():
    id = request.args.get('id')
    mycursor.execute("select * from mydatabase where id = {0}".format(id))
    content = mycursor.fetchone()
    return jsonify({'result':content[1]})
