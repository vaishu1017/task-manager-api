 Task Manager API 
This is a simple Task Manager API built using Flask and SQLite.  
It allows users to create, view, update, and delete tasks.

 Technologies Used
 Python
 Flask
 SQLite
 SQLAlchemy

 Setup Instructions

1. Clone the repository:
   git clone <your-repo-link>

2. Navigate to project folder:
   cd task-manager

3. Install dependencies:
   pip install flask flask_sqlalchemy

4. Run the application:
   python app.py

API Endpoints

 1. Add Task
 URL: /add_task
 Method: POST
 Body (JSON):
{
  "title": "Task Name",
  "description": "Task Description",
  "status": "pending"
}

 2. Get All Tasks
 URL: /tasks
 Method: GET

 3. Update Task
URL: /update_task/<id>
Method: PUT

4. Delete Task
URL: /delete_task/<id>
Method: DELETE
 
 Features
 Add new tasks
View all tasks
Update task details
 Delete tasks
