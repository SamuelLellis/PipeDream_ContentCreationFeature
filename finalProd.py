from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import mysql.connector
from connect import connect
from flask_sqlalchemy import SQLAlchemy
import datetime

mydb = connect()
mycursor = mydb.cursor()

app = Flask(__name__)
api = Api(app)

class Content(Resource):
    @app.route('/get', methods=['GET'])
    def get(self, id): #Gets content from database
        mycursor.execute("select * from mydatabase")
        records = mycursor.fetchall()
        for row in records:
            if(row[0]== id):
                content = row[1]
                break
        return jsonify({'content':content})

    @app.route('/add', methods=['POST'])
    def add(self, id, content):
        data = content.get_json()
        now = datetime.datetime.now()

        mycursor.execute('''
            INSERT INTO localhost.mydatabase.mydatabase (id,content,author,data/time)
            VALUES
            (id,data,author,now
            ''')
        mydb.commit()
        return jsonify({'result':'Sucess'})

    def edit(self, id):

api.add_resource(Content, '/content/<string:name>')
