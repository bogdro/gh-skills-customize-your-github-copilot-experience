# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a REST API using the FastAPI framework in Python. You'll build endpoints to handle HTTP requests and responses for a simple task management application.

## 📝 Tasks

### 🛠️	Set up FastAPI Application

#### Description
Install FastAPI and create a basic application structure with a root endpoint.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a main.py file with FastAPI app
- Include a GET endpoint at "/" that returns a welcome message
- Run the server and verify it works

### 🛠️	Create Task Management Endpoints

#### Description
Implement CRUD operations for tasks: Create, Read, Update, Delete.

#### Requirements
Completed program should:

- POST /tasks - Create a new task
- GET /tasks - List all tasks
- GET /tasks/{id} - Get a specific task by ID
- PUT /tasks/{id} - Update a task
- DELETE /tasks/{id} - Delete a task
- Use Pydantic models for request/response validation
- Store tasks in memory (list or dict)