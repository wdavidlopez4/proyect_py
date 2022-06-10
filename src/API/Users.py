from flask import Blueprint, request, jsonify
from src.BLL.services.UsersServices import UsersServices
from flask_login import login_required

users_rout = Blueprint('users', __name__)


@login_required
@users_rout.route('/add', methods=['POST'])
def add():
    objectJSON = {'name': request.json['name'],
                  'mail': request.json['mail'],
                  'password': request.json['password']}

    service = UsersServices
    result = service.add(objectJSON)

    return jsonify(result)


@login_required
@users_rout.route('/update', methods=['POST'])
def update():
    objectJSON = {'id': request.json['id'],
                  'name': request.json['name'],
                  'password': request.json['password']}

    service = UsersServices
    result = service.postMessage(objectJSON)

    return jsonify(result)


@login_required
@users_rout.route('/delete', methods=['POST'])
def delete():
    objectJSON = {'id': request.json['id']}

    service = UsersServices
    result = service.delete(objectJSON)

    return jsonify(result)


@login_required
@users_rout.route('/get/<id>', methods=['GET'])
def get(id):
    service = UsersServices
    result = service.get(id)

    return jsonify(result)


@users_rout.route('/login/<id>', methods=['GET'])
def Login(id):
    service = UsersServices
    result = service.login(id)
    return jsonify(result)


@login_required
@users_rout.route('/logout/<id>', methods=['GET'])
def Logout(id):
    service = UsersServices
    result = service.logout(id)
    return jsonify(result)
