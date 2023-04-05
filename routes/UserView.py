from flask import Blueprint

User_blueprint = Blueprint('User_blueprint', __name__)

@User_blueprint.route('/user')
def index():
    return "This is an example app"