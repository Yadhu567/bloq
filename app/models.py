from datetime import datetime
from bson.objectid import ObjectId
from app import db

def user_schema(user):
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"]
    }

def project_schema(project):
    return {
        "id": str(project["_id"]),
        "title": project["title"],
        "description": project["description"],
        "creation_date": project["creation_date"],
        "tasks": project["tasks"]
    }

def task_schema(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "status": task["status"],
        "due_date": task["due_date"]
    }
