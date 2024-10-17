from fastapi.testclient import TestClient
from main import app, courses_db, uuid

client = TestClient(app)

# * This is the model for tests
testingCourseData = {
    "name": "TEST",
    "description": "Testing",
    "level": "Testing",
    "duration": 1
}

# * Clean all the courses for testing
def setup_function():
    courses_db.clear()
    
def test_getAllCourses():
    response = client.get("/courses/")
    assert response.status_code == 200 # ? Verify code 200
    assert response.json() == [] # ? After the clean this must be empty
    
def test_createCourse():
    response = client.post("/courses/", json=testingCourseData)
    assert response.status_code == 200
    
    # ? Get the respond data
    response_data = response.json()
    
    # ? Verify matches
    assert response_data["name"] == testingCourseData["name"]
    assert response_data["description"] == testingCourseData["description"]
    assert response_data["level"] == testingCourseData["level"]
    assert response_data["duration"] == testingCourseData["duration"]
    
    # ? Verify valid ID
    try:
        uuid_obj = uuid.UUID(response_data["id"])
        assert str(uuid_obj) == response_data["id"]  
    except ValueError:
        assert False, "Invalid ID (No UUID)"
        
# * Create a Course to the next tests
def testing_course():
    response = client.post("/courses", json=testingCourseData)
    assert response.status_code == 200
    return response.json()

def test_readCourse():
    createdCourse = testing_course()
    
    # ? get request
    response = client.get(f"/courses/{createdCourse['id']}")
    
    # ? Verifiy code 200
    assert response.status_code == 200
    
    # ? Get data
    response_data = response.json()
    
    # ? Verify data
    assert response_data["id"] == createdCourse["id"]
    assert response_data["name"] == createdCourse["name"]
    assert response_data["description"] == createdCourse["description"]
    assert response_data["level"] == createdCourse["level"]
    assert response_data["duration"] == createdCourse["duration"]

def test_updateCourse():
    created_course = testing_course()
    
    # ? The testing course for the update
    updated_data = {
        "name": "UPDATED TEST",
        "description": "Updated Testing",
        "level": "Updated Testing",
        "duration": 2,
    }
    
    # ? Put Request
    response = client.put(f"/courses/{created_course['id']}", json=updated_data)
    
    # ? Verifiy code 200
    assert response.status_code == 200
    
    # ? Get data
    response_data = response.json()
    
    # ? Verify matches
    assert response_data["id"] == created_course["id"]
    assert response_data["name"] == updated_data["name"]
    assert response_data["description"] == updated_data["description"]
    assert response_data["level"] == updated_data["level"]
    assert response_data["duration"] == updated_data["duration"] 

def test_deleteCourse():
    created_course = testing_course()
    
    # ? Delete request
    response = client.delete(f"/courses/{created_course['id']}") 
    assert response.status_code == 200
    
    # ? Get data
    response_data = response.json()
    
    # ? Verify matches
    assert response_data["id"] == created_course["id"]
    assert response_data["name"] == created_course["name"]
    assert response_data["description"] == created_course["description"]
    assert response_data["level"] == created_course["level"]
    assert response_data["duration"] == created_course["duration"] 
    
    # ? Re try to find the deleted course
    response = client.get(f"/courses/{created_course['id']}")
    
    # ? Verify code 404
    assert response.status_code == 404