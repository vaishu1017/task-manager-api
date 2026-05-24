from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODEL
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    status = db.Column(db.String(20))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

# HOME ROUTE
@app.route('/')
def home():
    return "Working"

# ADD TASK API
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()

    new_task = Task(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'pending')
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task added successfully"})

# GET ALL TASKS API
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    
    result = []
    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "created_date": str(t.created_date)
        })
    
    return jsonify(result)
@app.route('/update_task/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"message": "Task not found"})

    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)

    db.session.commit()

    return jsonify({"message": "Task updated successfully"})
@app.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"message": "Task not found"})

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"})
if __name__ == '__main__':
    app.run(debug=True)