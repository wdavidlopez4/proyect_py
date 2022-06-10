from flask import Blueprint, request, jsonify
from src.BLL.services.PublicationsServices import PublicationsServices
from flask_login import login_required

publications_rout = Blueprint('publications', __name__)


@login_required
@publications_rout.route('/add', methods=['POST'])
def add():
    objectJSON = {'title': request.json['title'],
                  'description': request.json['description'],
                  'priority': request.json['priority'],
                  'user_id': request.json['user_id']}

    service = PublicationsServices
    result = service.add(objectJSON)

    return jsonify(result)


@login_required
@publications_rout.route('/postMessage', methods=['POST'])
def postMessage():
    objectJSON = {'id': request.json['id']}

    service = PublicationsServices
    result = service.postMessage(objectJSON)

    return jsonify(result)


@login_required
@publications_rout.route('/update', methods=['POST'])
def update():
    objectJSON = {'id': request.json['id'],
                  'title': request.json['title'],
                  'description': request.json['description'],
                  'priority': request.json['priority']}

    service = PublicationsServices
    result = service.postMessage(objectJSON)

    return jsonify(result)


@login_required
@publications_rout.route('/delete', methods=['POST'])
def delete():
    objectJSON = {'id': request.json['id']}

    service = PublicationsServices
    result = service.delete(objectJSON)

    return jsonify(result)


@login_required
@publications_rout.route('/get/<id>', methods=['GET'])
def get(id):
    service = PublicationsServices
    result = service.get(id)

    return jsonify(result)
