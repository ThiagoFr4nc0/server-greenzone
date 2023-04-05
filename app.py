from flask import Flask
from routes.UserView import User_blueprint

app = Flask(__name__)
app.register_blueprint(User_blueprint)
