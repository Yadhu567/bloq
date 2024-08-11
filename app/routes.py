from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
from app import app, db
from app.models import project_schema, task_schema

@app.route('/projects', methods=['POST','GET'])
@jwt_required()
def create_project():
    data = request.get_json()
    project = {
        "title": data['title'],
        "description": data['description'],
        "creation_date": datetime.utcnow(),
        "tasks": []
    }
    db.projects.insert_one(project)
    return jsonify(project_schema(project)), 201

@app.route('/projects/<project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    project = db.projects.find_one({"_id": ObjectId(project_id)})
    return jsonify(project_schema(project)), 200


