# To-Do API Documentation

## Introduction
This To-Do API allows users to create, retrieve, update, delete, and mark to-do items as completed. It also includes basic authentication for secure access to the endpoints.

---

## Prerequisites

### System Requirements:
- Python 3.8 or later
- Postman or cURL for testing endpoints

### Install Required Python Libraries:
Run the following command to install dependencies:
bash
pip install flask flask_sqlalchemy flask_httpauth werkzeug


---

## Project Setup

### Step 1: Clone the Repository
Download or clone the project files to your local system.

### Step 2: Initialize the Database
The project uses SQLite for database management. The database file (todos.db) will be automatically created during the first run.

### Step 3: Run the Application
Run the application using the following command:
bash
python app.py

The API will start running at http://127.0.0.1:5000.

---

## Authentication
This API uses Basic Authentication.
- *Username*: admin
- *Password*: password

You must include these credentials in the Authorization header for every request.

---

## API Endpoints

### 1. Add a New To-Do
*URL*: /todos
*Method*: POST

*Headers:*
- Content-Type: application/json
- Authorization: Basic Auth

*Body (JSON):*
json
{
    "title": "Complete Flask API",
    "description": "Finish creating and testing the Flask API project",
    "due_date": "2024-12-20"
}


*Response:*
json
{
    "message": "To-do item created successfully.",
    "todo": {
        "id": 1,
        "title": "Complete Flask API",
        "description": "Finish creating and testing the Flask API project",
        "due_date": "2024-12-20",
        "completed": false
    }
}


---

### 2. Get All To-Do Items
*URL*: /todos
*Method*: GET

*Headers:*
- Authorization: Basic Auth

*Response:*
json
[
    {
        "id": 1,
        "title": "Complete Flask API",
        "description": "Finish creating and testing the Flask API project",
        "due_date": "2024-12-20",
        "completed": false
    }
]


---

### 3. Get a Single To-Do
*URL*: /todos/<id>
*Method*: GET

*Headers:*
- Authorization: Basic Auth

*Response:*
json
{
    "id": 1,
    "title": "Complete Flask API",
    "description": "Finish creating and testing the Flask API project",
    "due_date": "2024-12-20",
    "completed": false
}


---

### 4. Update a To-Do
*URL*: /todos/<id>
*Method*: PUT

*Headers:*
- Content-Type: application/json
- Authorization: Basic Auth

*Body (JSON):*
json
{
    "title": "Complete Flask API Project",
    "description": "Updated description",
    "due_date": "2024-12-25",
    "completed": true
}


*Response:*
json
{
    "message": "To-do item updated successfully.",
    "todo": {
        "id": 1,
        "title": "Complete Flask API Project",
        "description": "Updated description",
        "due_date": "2024-12-25",
        "completed": true
    }
}


---

### 5. Delete a To-Do
*URL*: /todos/<id>
*Method*: DELETE

*Headers:*
- Authorization: Basic Auth

*Response:*
json
{
    "message": "To-do item deleted successfully."
}


---

### 6. Mark a To-Do as Completed
*URL*: /todos/<id>/complete
*Method*: PATCH

*Headers:*
- Authorization: Basic Auth

*Response:*
json
{
    "message": "To-do item marked as completed.",
    "todo": {
        "id": 1,
        "title": "Complete Flask API Project",
        "description": "Finish creating and testing the Flask API project",
        "due_date": "2024-12-25",
        "completed": true
    }
}


---

## Bonus Features
### Authentication
The API uses HTTPBasicAuth for secure access. All endpoints require valid credentials.

### Marking as Completed
Added a PATCH endpoint to specifically mark a to-do item as completed.

---

## Testing in Postman
1. Open Postman and create a new request.
2. Set the *Authorization* tab to Basic Auth and provide:
   - Username: admin
   - Password: password
3. Use the respective endpoints listed above.
4. For POST, PUT, or PATCH requests, go to the *Body* tab and select raw with JSON format.
5. Execute the requests to test the API functionality.

---

## Notes
- The database file (todos.db) will be created in the project directory automatically.
- Ensure you have proper Python and library versions installed.

If you encounter any issues, feel free to reach out for support!
