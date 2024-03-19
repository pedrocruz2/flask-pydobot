from flask import Flask
from functions import *
from robo import Robo
app = Flask(__name__)
robo = Robo('/dev/ttyUSB0')
@app.route("/")
def hello_world():
    return robo.move_robo_r(100)

if __name__ == "__main__":
    app.run()
