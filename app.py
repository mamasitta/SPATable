from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from db import db
from manajers.filter_manajers import FilterManagers
from models.models import TableItem

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']
CORS(app)
# TODO remove after check
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ozujwmqruykefz:73d2fc9b6b9254ee557f7bb7832093d3954227c4abd3150ac0b46aa5fb3bd3b8@ec2-52-21-0-111.compute-1.amazonaws.com:5432/dek6ac7dov2gjb" #TODO CHANGE
db.init_app(app)


def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def main():
    result = TableItem.query.all()
    return render_template('main.html', table_items=result)


@app.route('/api/filter', methods=['GET'])
def api_filter():
    column = request.args.get('column')
    condition = request.args.get('condition')
    user_input = request.args.get('user_input')
    result = {}
    if column is None or condition is None or user_input is None:
        result['error'] = 'Not valid parameters'
        status = 403
        data = jsonify(result)
        return data, status
    if condition == 'include':
        items_list = FilterManagers.get_table_items_include_user_input(user_input=user_input, column=column)
    else:
        items_list = FilterManagers.get_table_items_with_condition(user_input=user_input, column=column,
                                                                       condition=condition)
    result['data'] = items_list
    data = jsonify(result)
    status = 200
    return data, status

