from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

#Ejemplo de https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
#referencia virtualenv http://docs.python-guide.org/en/latest/dev/virtualenvs/

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

#Ruta Status actual

class Status(Resource):
    def get(self):
        conn = db_connect.connect()
        base = 0
        if conn:
        	base = 1
        result = {'estado': 1, 'base_de_datos': base, 'sensores': 0, 'alarma': 0, 'video': 1}
        return jsonify(result)
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

api.add_resource(Status, '/status') # Status actual del dispositivo


if __name__ == '__main__':
     app.run(port='5002')