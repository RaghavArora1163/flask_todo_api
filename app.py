from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# In-memory user storage for authentication
users = {
    "admin": generate_password_hash("password")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

# Database model for Todo item
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.strftime('%Y-%m-%d'),
            "completed": self.completed
        }

# Routes

# Add a new to-do item
@app.route('/todos', methods=['POST'])
@auth.login_required
def add_todo():
    data = request.get_json()
    try:
        new_todo = Todo(
            title=data['title'],
            description=data.get('description', ''),
            due_date=datetime.strptime(data['due_date'], '%Y-%m-%d')
        )
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"message": "To-do item created successfully.", "todo": new_todo.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Retrieve all to-do items
@app.route('/todos', methods=['GET'])
@auth.login_required
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos]), 200

# Retrieve a single to-do item by ID
@app.route('/todos/<int:id>', methods=['GET'])
@auth.login_required
def get_todo_by_id(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo.to_dict()), 200

# Update an existing to-do item by ID
@app.route('/todos/<int:id>', methods=['PUT'])
@auth.login_required
def update_todo(id):
    data = request.get_json()
    todo = Todo.query.get_or_404(id)
    try:
        todo.title = data.get('title', todo.title)
        todo.description = data.get('description', todo.description)
        todo.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d') if 'due_date' in data else todo.due_date
        todo.completed = data.get('completed', todo.completed)
        db.session.commit()
        return jsonify({"message": "To-do item updated successfully.", "todo": todo.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete a to-do item by ID
@app.route('/todos/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "To-do item deleted successfully."}), 200

# Mark a to-do item as completed
@app.route('/todos/<int:id>/complete', methods=['PATCH'])
@auth.login_required
def complete_todo(id):
    todo = Todo.query.get_or_404(id)
    try:
        todo.completed = True
        db.session.commit()
        return jsonify({"message": "To-do item marked as completed.", "todo": todo.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
