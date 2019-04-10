# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api
import mysql.connector
from connect import connect
# # from flask_sqlalchemy import SQLAlchemy
import datetime
# # import json
#
mydb = connect()
mycursor = mydb.cursor()
#
# app = Flask(__name__)
# api = Api(app)
#
# # class Content(Resource):
# @app.route('/get', methods=['GET'])
# def get(self, id): #Gets content from database
#     mycursor.execute("select * from mydatabase")
#     records = mycursor.fetchall()
#     for row in records:
#         if(row[0]== id):
#             content = row[1]
#             break
#     return jsonify({'content':content})
#
# @app.route('/add', methods=['POST'])
# def add(self, data):
#     content = data.get_json()
#     now = datetime.datetime.now()
#
#     mycursor.execute('''
#         INSERT INTO localhost.mydatabase.mydatabase (id,content,author,data/time)
#         VALUES
#         (id,data,author,now
#         ''')
#     mydb.commit()
#     return jsonify({'result':'Sucess'})
#
#     # def edit(self, id):
#
# api.add_resource(Content, '/content/<string:name>')

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
    return 'clip'
