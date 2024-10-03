# FastAPI Course Management API

A simple API to manage courses, built with FastAPI. This API allows you to create, read, update, and delete courses (CRUD operations).

## Features

- **Create a Course**: Add a new course to the database.
- **Read Courses**: Retrieve all courses or get a specific course by its ID.
- **Update a Course**: Update the information of an existing course.
- **Delete a Course**: Delete a specific course from the database.

## Technologies

- **Python 3.7+**
- **FastAPI**: For building the API.
- **UUID**: For generating unique course IDs.
- **Pydantic**: For data validation.

## Endpoints

### 1. Get All Courses

- **URL**: `/courses/`
- **Method**: `GET`
- **Response**: Returns a list of all courses.

### 2. Get Course by ID

- **URL**: `/courses/{searched_id}`
- **Method**: `GET`
- **Path Parameter**:
  - `searched_id` (str): The ID of the course to retrieve.
- **Response**: Returns the course with the specified ID.
- **Error**: Returns a 404 error if the course is not found.

### 3. Create a Course

- **URL**: `/courses/`
- **Method**: `POST`
- **Request Body**:
  - `nombre` (str): Name of the course.
  - `description` (str, optional): Description of the course.
  - `level` (str): Level of the course (e.g., Beginner, Intermediate, Advanced).
  - `duration` (int): Duration of the course in hours.
- **Response**: Returns the created course.

### 4. Update a Course

- **URL**: `/courses/{searched_id}`
- **Method**: `PUT`
- **Path Parameter**:
  - `searched_id` (str): The ID of the course to update.
- **Request Body**:
  - `nombre` (str): Updated name of the course.
  - `description` (str, optional): Updated description of the course.
  - `level` (str): Updated level of the course.
  - `duration` (int): Updated duration of the course in hours.
- **Response**: Returns the updated course.
- **Error**: Returns a 404 error if the course is not found.

### 5. Delete a Course

- **URL**: `/courses/{searched_id}`
- **Method**: `DELETE`
- **Path Parameter**:
  - `searched_id` (str): The ID of the course to delete.
- **Response**: Returns the deleted course.
- **Error**: Returns a 404 error if the course is not found.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/course-management-api.git
    ```
    
2. Navigate to the project directory:
 
```bash
cd course-management-api
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

5. Install the dependencies:

```bash
pip install fastapi uvicorn
```

### Running the API
Run the following command to start the server:

```bash
uvicorn main:app --reload
```

or 
```bash
python -m uvicorn main:app --reload
```


After running the command, the API will be available at http://127.0.0.1:8000.

### Testing the Endpoints
You can use tools like Postman to test the API endpoints.