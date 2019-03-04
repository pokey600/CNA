from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class search(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from search")  # This line performs query and returns json result
        return {'search': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID


class update(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(search, '/search')  # Route_1
api.add_resource(update, '/update')  # Route_2


if __name__ == '__main__':
    app.run(port='5000')