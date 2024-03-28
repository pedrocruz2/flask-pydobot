from flask import Flask, jsonify, request
from functions import *
from robo import Robo
app = Flask(__name__)
robo = Robo('COM5')
@app.route("/")
def hello_world():
    return 'fodase'
@app.route('/home', methods=['GET'])
def returnhome():
    #return robo.origem_global()
    return None
@app.route('/move', methods=['POST'])
def move_to_specific():
    data = request.get_json()
    print(data)
    xaxis = data.get('xaxis')
    yaxis = data.get('yaxis')
    zaxis = data.get('zaxis')
    print(xaxis,yaxis,zaxis)
    return None


if __name__ == "__main__":
    app.run()
